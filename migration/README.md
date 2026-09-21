# Migration: AVDASI2/docs → AVDASI2/avdasi2.github.io

The site moved from `avdasi2.github.io/docs` to the root of `avdasi2.github.io`. These files keep the old links working.

## The redirect

`docs-redirect/` holds one page, published from the **old** repository (`AVDASI2/docs`). It sends every visitor to <https://avdasi2.github.io/>.

It is published twice, as `index.html` and as `404.html`, because GitHub Pages serves `404.html` for any path it doesn't recognise. That way both the old root and every old sub-page land on the new site's home page:

| Old URL | Served by | Goes to |
|---|---|---|
| `avdasi2.github.io/docs/` | `index.html` | `avdasi2.github.io` |
| `avdasi2.github.io/docs/avionics/stepbystep/01-cube/` | `404.html` | `avdasi2.github.io` |

Sub-pages land on the home page rather than their equivalent new page, which is deliberate: the paths have changed, and one reliable hop beats a table of guesses.

## Publishing it

In a clone of the **old** repository, `AVDASI2/docs`, on the `gh-pages` branch:

```bash
git switch gh-pages
git rm -rq .
cp /path/to/migration/docs-redirect/index.html .
cp index.html 404.html
touch .nojekyll
git add -A && git commit -m "Redirect to avdasi2.github.io"
git push
```

Then, in that repository's settings: leave Pages enabled and serving from `gh-pages`, delete the CI workflow on `main` so it stops rebuilding the old site, and archive the repository once the new site is live.

Keep the repository itself. It holds the history and the snapshot tags `v2025-26-mkdocs` and `v2025-26-site`, which are the only route back to the 2025-26 site.
