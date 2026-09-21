// Build every deck in slides/<deck>/index.md into the site.
//
// Each deck becomes docs/slides/<deck>/index.html plus slides.pdf, inside docs/
// so that `zensical serve` and `zensical build` publish them with everything
// else. Adapted from the CADE30008 control course's build script.
//
// Decks refer to site images as ../../docs/..., which is right for the source
// file and for VS Code's preview. The published deck sits in docs/slides/<deck>/,
// one level nearer the site root, so those paths are rewritten to ../../... in
// the HTML.
import { spawnSync } from "node:child_process";
import { existsSync, mkdirSync, readdirSync, readFileSync, writeFileSync } from "node:fs";
import { join, resolve } from "node:path";

const root = resolve(import.meta.dirname, "..");
const marp = join(root, "node_modules", ".bin", "marp");
const decks = readdirSync(join(root, "slides"), { withFileTypes: true })
  .filter((d) => d.isDirectory() && existsSync(join(root, "slides", d.name, "index.md")))
  .map((d) => d.name);

const only = process.argv.includes("--html-only") ? ["html"] : ["html", "pdf"];
let failed = 0;
for (const deck of decks) {
  const src = join(root, "slides", deck, "index.md");
  const outDir = join(root, "docs", "slides", deck);
  mkdirSync(outDir, { recursive: true });
  for (const kind of only) {
    const out = join(outDir, kind === "html" ? "index.html" : "slides.pdf");
    const r = spawnSync(marp, [src, "--no-stdin", "-o", out], { cwd: root, stdio: ["ignore", "inherit", "inherit"] });
    if (r.status !== 0) { failed++; continue; }
    if (kind === "html") {
      const html = readFileSync(out, "utf8")
        .replace(/((?:src|href)=")\.\.\/\.\.\/docs\//g, "$1../../")
        // CSS background-image paths need the same rewrite. Marp writes its own
        // background images with HTML-escaped quotes - url(&quot;...&quot;) - so
        // match those as well as plain or absent quotes, or they 404 on the site.
        .replace(/(url\((?:&quot;|&#39;|['"])?)\.\.\/\.\.\/docs\//g, "$1../../");
      writeFileSync(out, html);
    }
    console.log(`built docs/slides/${deck}/${kind === "html" ? "index.html" : "slides.pdf"}`);
  }
}
process.exit(failed ? 1 : 0);
