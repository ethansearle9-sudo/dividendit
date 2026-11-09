#!/usr/bin/env python3
"""Rebuild sitemap.xml from the pages that are actually live and indexable.

A page is listed when it has the shared shell, a canonical link and no
noindex tag. Existing lastmod dates are kept; pass page slugs as arguments
(or --all) to stamp them with today's date.

Run:  python3 tools/sitemap.py [slug ...]
"""
import datetime, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = 'https://dividendit.com'
today = datetime.date.today().isoformat()
touch = set(sys.argv[1:])

old = {}
sm = ROOT / 'sitemap.xml'
if sm.exists():
    for loc, mod in re.findall(r'<loc>([^<]+)</loc>\s*(?:<lastmod>([^<]+)</lastmod>)?', sm.read_text()):
        old[loc] = mod

PRIORITY = {'': '1.0', 'guide': '0.9', 'outsourced-cyber': '0.9', 'outsourced-it': '0.9', 'services': '0.8', 'insights': '0.8'}
rows = []
for f in sorted(ROOT.glob('*.html')):
    s = f.read_text(encoding='utf-8')
    if '<!-- shell:nav -->' not in s or re.search(r'name="robots"[^>]*noindex', s) or f.name.startswith('_'):
        continue
    m = re.search(r'rel="canonical" href="([^"]+)"', s)
    if not m:
        print('no canonical:', f.name); continue
    slug = '' if f.stem == 'index' else f.stem
    loc = SITE + '/' + slug
    if m.group(1).rstrip('/') != loc.rstrip('/'):
        print('canonical mismatch:', f.name, m.group(1)); continue
    mod = today if ('--all' in touch or slug in touch or (slug == '' and 'index' in touch) or loc not in old or not old[loc]) else old[loc]
    rows.append((loc, mod, PRIORITY.get(slug, '0.6')))

rows.sort(key=lambda r: (-float(r[2]), r[0]))
out = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for loc, mod, pr in rows:
    out.append(f'  <url><loc>{loc}</loc><lastmod>{mod}</lastmod><priority>{pr}</priority></url>')
out.append('</urlset>')
sm.write_text('\n'.join(out) + '\n')
print(f'sitemap: {len(rows)} pages')
