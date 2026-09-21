"""Build the live site: only what publish.yaml lists.

Adapted from the CADE30008 control course's script of the same name.

The in-progress site is docs/ as it stands, built by zensical.toml, and it is
local only. The live site is a filtered copy of it:

  1. docs/ is copied to .live/docs, leaving out every page not listed in
     publish.yaml and every deck not listed under `slides`;
  2. in the pages that remain, <!-- in-progress:start --> ... <!-- in-progress:end -->
     blocks are removed, and any link to a page that was left out becomes plain
     text, so nothing dangles and nothing unfinished is reachable;
  3. .live/zensical.toml is written from zensical.toml, with the nav cut down to
     the published pages, the live site_url, and the "in progress" label taken
     off the site name;
  4. the site is built into .live/site, and every internal link in it is checked.

Exits non-zero if the build fails or any link is broken, so a deploy can't
publish a broken site. Preview the result with `npm run preview:live`.
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tomllib
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

import yaml

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
LIVE = ROOT / ".live"
IN_PROGRESS = " · in progress"

problems: list[str] = []


def published() -> tuple[set[str], set[str], str]:
    cfg = yaml.safe_load((ROOT / "publish.yaml").read_text(encoding="utf-8"))
    pages = set(cfg["pages"])
    decks = set(cfg.get("slides") or [])
    for p in pages:
        if not (DOCS / p).exists():
            problems.append(f"publish.yaml lists {p}, which doesn't exist")
    return pages, decks, cfg["site_url"]


def copy_docs(pages: set[str], decks: set[str]) -> None:
    """Copy docs/ to .live/docs, leaving out unpublished pages and decks."""
    shutil.copytree(DOCS, LIVE / "docs", ignore=shutil.ignore_patterns("slides"))
    out = LIVE / "docs"
    for md in out.rglob("*.md"):
        rel = md.relative_to(out).as_posix()
        if rel.startswith("code/"):
            continue                      # example code, included with --8<--
        if rel not in pages:
            md.unlink()
    # Built decks, for published decks only.
    for deck in sorted(decks):
        src = DOCS / "slides" / deck
        if not src.exists():
            problems.append(f"publish.yaml lists the deck {deck}, which isn't built; run npm run slides")
            continue
        shutil.copytree(src, out / "slides" / deck)


LINK = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)\s]+)([^)]*)\)")


def rewrite_pages() -> None:
    """Strip in-progress blocks, and turn links to unpublished pages into text."""
    out = LIVE / "docs"
    for md in out.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        text = re.sub(r"<!-- in-progress:start -->.*?<!-- in-progress:end -->\n?", "", text, flags=re.S)

        def fix(m: re.Match) -> str:
            label, target = m.group(1), m.group(2)
            if re.match(r"^(https?:|mailto:|#)", target):
                return m.group(0)
            path = target.split("#")[0]
            if not path:
                return m.group(0)
            resolved = (md.parent / unquote(path)).resolve()
            if resolved.exists():
                return m.group(0)
            return label                  # unpublished: keep the words, drop the link

        md.write_text(LINK.sub(fix, text), encoding="utf-8")


def filter_nav(items: list, pages: set[str]) -> list:
    """Keep published pages, and sections that still have something in them."""
    out: list = []
    for item in items:
        if isinstance(item, str):                            # a bare page, e.g. a section index
            if item in pages:
                out.append(item)
        elif isinstance(item, dict) and len(item) == 1:
            (title, value), = item.items()
            if isinstance(value, str):                       # a titled page
                if value in pages:
                    out.append({title: value})
            else:                                            # a section
                children = filter_nav(value, pages)
                if children:
                    out.append({title: children})
    return out


def dump_nav(items: list, depth: int = 1) -> list[str]:
    """Emit a nav list as the TOML lines zensical.toml uses."""
    pad, lines = "  " * depth, []
    for item in items:
        if isinstance(item, str):
            lines.append(f'{pad}"{item}",')
        else:
            (title, value), = item.items()
            if isinstance(value, str):
                lines.append(f'{pad}{{ "{title}" = "{value}" }},')
            else:
                lines.append(f'{pad}{{ "{title}" = [')
                lines += dump_nav(value, depth + 1)
                lines.append(f"{pad}] }},")
    return lines


def write_config(pages: set[str], site_url: str) -> None:
    base = (ROOT / "zensical.toml").read_text(encoding="utf-8")
    nav = tomllib.loads(base)["project"]["nav"]
    start = base.index("nav = [")
    end = base.index("\n]\n", start)
    entries = dump_nav(filter_nav(nav, pages))
    text = base[:start] + "nav = [\n" + "\n".join(entries) + base[end:]
    text = re.sub(r'^site_name = "(.*?)"', lambda m: f'site_name = "{m.group(1).replace(IN_PROGRESS, "")}"', text, count=1, flags=re.M)
    text = re.sub(r'^site_url = ".*?"', f'site_url = "{site_url}"', text, count=1, flags=re.M)
    text = text.replace("[project]\n", '[project]\ndocs_dir = "docs"\nsite_dir = "site"\n', 1)
    # custom_dir resolves against this config's directory, which is .live/, so
    # point it back at the theme submodule in the repository root.
    text = text.replace('custom_dir = "theme/dist"', 'custom_dir = "../theme/dist"')
    tomllib.loads(text)                   # fail here, not in the build, if it's malformed
    (LIVE / "zensical.toml").write_text(text, encoding="utf-8")


class Links(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.refs: list[str] = []

    def handle_starttag(self, tag, attrs):
        for k, v in attrs:
            if k in ("href", "src") and v:
                self.refs.append(v)


def resolves(site: Path, page: Path, ref: str) -> bool:
    u = urlparse(ref)
    if u.scheme or u.netloc or ref.startswith(("#", "mailto:", "data:", "javascript:")):
        return True
    path = unquote(u.path)
    if not path:
        return True
    target = (site / path.lstrip("/")) if path.startswith("/") else (page.parent / path)
    target = target.resolve()
    return target.exists() or (target / "index.html").exists()


def check_links() -> None:
    site = LIVE / "site"
    for page in site.rglob("*.html"):
        parser = Links()
        parser.feed(page.read_text(encoding="utf-8", errors="replace"))
        for ref in parser.refs:
            if not resolves(site, page, ref):
                problems.append(f"broken link in {page.relative_to(site)}: {ref}")


def main() -> None:
    pages, decks, site_url = published()
    if LIVE.exists():
        shutil.rmtree(LIVE)
    LIVE.mkdir()
    copy_docs(pages, decks)
    rewrite_pages()
    write_config(pages, site_url)
    exe = Path(sys.executable).with_name("zensical")
    build = subprocess.run([str(exe), "build", "-f", str(LIVE / "zensical.toml"), "--clean"],
                           cwd=ROOT, capture_output=True, text=True)
    print((build.stdout + build.stderr).strip())
    if build.returncode != 0:
        sys.exit(build.returncode)
    check_links()
    for p in problems:
        print(f"error    {p}")
    print(f"\nlive site: {len(pages)} pages -> .live/site ({'OK' if not problems else f'{len(problems)} problem(s)'})")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
