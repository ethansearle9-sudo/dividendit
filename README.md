# dividendit.com

Static site on Netlify. Every page shares one shell: nav, footer, CSS and JS.

## Change the nav or footer
Edit `_shell/nav.html` or `_shell/footer.html` (styles in `assets/site.css`, behaviour in `assets/site.js`).
Netlify runs `node tools/shell.js` on every deploy, which copies the shell into every page.
Run it locally before committing so the files in the repo match the live site.

## Service pages, articles and the insights hub
These are written as plain content in `tools/content/*.py` and turned into pages by the builder,
so every one has the same layout, schema and tracking. Styles are in `assets/page.css`.

    python3 tools/build_pages.py   # rebuild the pages from the content files
    node tools/shell.js            # drop in the shared nav and footer
    python3 tools/sitemap.py SLUG  # rebuild sitemap.xml, stamping SLUG as updated today

To add an article or service page, add an entry to the right content file (copy an existing one),
run the three commands and commit. Do not edit the generated `.html` for these pages by hand:
the next build overwrites it. To list a new article on `/insights`, add its slug in `tools/content/z_insights.py`.

## One-off pages
1. Copy `_template.html` to `new-page.html`.
2. Fill in the CAPS placeholders and the content inside `<main>`.
3. Remove the `noindex` line, then run `python3 tools/sitemap.py new-page`.

Never edit content between `<!-- shell:... -->` markers inside a page; it is overwritten on deploy.

## Housekeeping
- Retired URLs are redirected in `netlify.toml`.
- Old drafts and previews (`v1`, `v2`, `v3`, `old-*`, `*-preview`) carry a `noindex` tag and are not in the sitemap.
