# dividendit.com

Static site on Netlify. Every page shares one shell: nav, footer, CSS and JS.

## Change the nav or footer
Edit `_shell/nav.html` or `_shell/footer.html` (styles in `assets/site.css`, behaviour in `assets/site.js`).
Netlify runs `node tools/shell.js` on every deploy, which copies the shell into every page.
Run it locally before committing so the files in the repo match the live site.

## Add a page
1. Copy `_template.html` to `new-page.html`.
2. Fill in the CAPS placeholders and the content inside `<main>`.
3. Remove the `noindex` line and add the URL to `sitemap.xml`.

Never edit content between `<!-- shell:... -->` markers inside a page; it is overwritten on deploy.
