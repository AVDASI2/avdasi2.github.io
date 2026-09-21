# AVDASI 2 docs

Avionics resources for AVDASI 2 (CADE20005, Aerospace Vehicle Design and Systems Integration) at the University of Bristol, published at <https://avdasi2.github.io>.

The site is built with [Zensical](https://zensical.org) in the Bristol Flight Lab theme shared with the CADE30008 Flight Dynamics & Control course. Slides use the [Flight Lab Marp theme](https://github.com/BristolFlightLab/marp-template), pinned to a release tag in `package.json`.

## Quick start

You need Python 3.10 or later.

```bash
git clone --recurse-submodules <this repo>   # the site theme is a submodule
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
npm install                         # only needed to build slides
./scripts/fetch-example-code.sh     # example scripts into docs/code/
npm run serve                       # the in-progress site, at http://localhost:8001
```

## Two sites from one source

**In progress** (`npm run serve`) is everything in `docs/`, and it is local
only. Its site name carries " · in progress" so you can't mistake one for the
other.

Ports are fixed per site, so they can be bookmarked, and don't collide with the
control course's:

| Site | Command | Port |
|---|---|---|
| AVDASI 2, in progress | `npm run serve` | <http://localhost:8001> |
| AVDASI 2, live preview | `npm run preview:live` | <http://localhost:8002> |
| CADE30008, in progress | `npm run serve` in `../aero-control-course` | <http://localhost:8011> |
| CADE30008, live preview | `npm run preview:live` there | <http://localhost:8012> |

Both are meant to be **left running**, so a bookmark just works. Check them with:

```bash
lsof -nP -iTCP -sTCP:LISTEN | grep -E ':(8001|8002)'
```

Each port should appear **twice**, once on `127.0.0.1` and once on `[::1]`.
Anything serving one family only will look down to some clients and fine to
others: on macOS `localhost` resolves to `::1` first, so an IPv4-only listener
fails for a client that doesn't fall back, and vice versa. That's why the live
preview uses `scripts/preview.py` rather than `python -m http.server`, which
binds one family and, without `--bind`, exposes the site to the whole network.

**Live** is <https://avdasi2.github.io>, and shows only the pages listed in
[`publish.yaml`](publish.yaml). `scripts/build_live.py` builds it: pages that
aren't listed are left out, links to them become plain text, anything between
`<!-- in-progress:start -->` and `<!-- in-progress:end -->` is dropped, and the
result's links are checked. Preview it exactly as it will be published with
`npm run preview:live`, on <http://localhost:8002>.

To publish a page: add it to `publish.yaml`, run `npm run preview:live`, look
at it, then commit and push. Pushing to `main` builds the live site and deploys
it (`.github/workflows/ci.yml`); the deploy fails rather than publishing a
broken link.

One-time set-up: this repository is `AVDASI2/avdasi2.github.io`, and its
**Settings › Pages › Source** is set to **GitHub Actions**.

## Layout

| Path | Contents |
|---|---|
| `zensical.toml` | Site configuration and navigation |
| `docs/` | Site pages |
| `theme/` | The [Flight Lab Zensical theme](https://github.com/BristolFlightLab/flightlab-zensical-theme), a submodule pinned to a tag. Don't edit it here |
| `docs/stylesheets/course.css` | AVDASI 2 additions to the theme |
| `docs/code/` | Example code, fetched from [avdasi2-avionics-demo](https://github.com/AVDASI2/avdasi2-avionics-demo) at build time. Not committed |
| `slides/` | Marp deck sources, built into `docs/slides/` with `npm run slides`. Built decks aren't committed; CI builds them |
| `publish.yaml` | What the live site shows |
| `teaching/annual-update.md` | What to update each year, and when |
| `migration/` | The redirect for the old `avdasi2.github.io/docs` site |

## History

These materials were previously published from `AVDASI2/docs` at
`avdasi2.github.io/docs`, built with MkDocs Material. That repository holds the
history and two snapshot tags:

| Tag | What it is |
|---|---|
| `v2025-26-mkdocs` | Source as taught in 2025-26, on MkDocs Material |
| `v2025-26-site` | The `gh-pages` branch as last deployed by MkDocs |

To look at an old version, clone that repository and run
`git switch --detach v2025-26-mkdocs`.
