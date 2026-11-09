#!/usr/bin/env node
/*
 * Dividend IT site shell.
 *
 * Every page carries four marker pairs. This script refills them from
 * _shell/ so the nav, footer, shared CSS and shared JS are identical
 * on every page:
 *
 *   <!-- shell:head -->     ...  <!-- /shell:head -->     (just before </head>)
 *   <!-- shell:nav -->      ...  <!-- /shell:nav -->      (top of <body>)
 *   <!-- shell:footer -->   ...  <!-- /shell:footer -->
 *   <!-- shell:scripts -->  ...  <!-- /shell:scripts -->  (just before </body>)
 *
 * Run:  node tools/shell.js         (rewrites pages in place)
 *       node tools/shell.js --check (exit 1 if any page is out of date)
 *
 * Netlify runs it on every deploy (see netlify.toml), so a page can never
 * go live with a stale nav or footer.
 */
const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const read = (p) => fs.readFileSync(path.join(root, p), 'utf8').trim();

const blocks = {
  head: '<link rel="stylesheet" href="/assets/site.css">',
  nav: read('_shell/nav.html'),
  footer: read('_shell/footer.html'),
  scripts: '<script src="/assets/site.js"></script>',
};

const check = process.argv.includes('--check');
let changed = 0, pages = 0;

for (const file of fs.readdirSync(root)) {
  if (!file.endsWith('.html')) continue;
  const full = path.join(root, file);
  const src = fs.readFileSync(full, 'utf8');
  if (!src.includes('<!-- shell:nav -->')) continue;
  pages++;
  let out = src;
  for (const [name, html] of Object.entries(blocks)) {
    const re = new RegExp(`<!-- shell:${name} -->[\\s\\S]*?<!-- /shell:${name} -->`);
    if (!re.test(out)) {
      console.error(`${file}: missing shell:${name} markers`);
      process.exitCode = 1;
      continue;
    }
    out = out.replace(re, () => `<!-- shell:${name} -->\n${html}\n<!-- /shell:${name} -->`);
  }
  if (out !== src) {
    changed++;
    if (check) console.error(`${file}: shell out of date`);
    else fs.writeFileSync(full, out);
  }
}

console.log(`shell: ${pages} pages, ${changed} ${check ? 'out of date' : 'updated'}`);
if (check && changed) process.exitCode = 1;
