"""Add an FAQ section plus FAQPage schema to a hand-built page.

The generated pages get their FAQ from build_pages.py. The hand-built ones
have no generator, so this applies the identical markup and schema to them,
using build_pages' own faq_html/faq_schema so the two can never drift.

HubSpot's AEO Content Optimization Checklist, section 4: an FAQ gives answer
engines multiple extraction points per page, and each Q&A pair has to stand
on its own as a self-contained answer.

Idempotent: a page that already has an FAQ is left alone.

Usage:
    import add_faq
    add_faq.apply('guide', [('Question?', 'Answer.'), ...])
"""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from build_pages import faq_html, faq_schema  # noqa: E402

ROOT = pathlib.Path(__file__).parent.parent

# The FAQ goes immediately before the closing call to action. Pages without
# one (the research articles and the calculators) end with the cross-links
# instead, so that is the fallback. Order matters: first match wins.
ANCHORS = ('<section class="pl-cta-band">', '<section id="cta">',
           '<section class="xlinks">')


def apply(slug, faqs, heading='Frequently asked questions'):
    p = ROOT / f'{slug}.html'
    s = p.read_text(encoding='utf-8')

    if 'id="faq"' in s:
        print(f'skip {slug}: already has an FAQ')
        return False

    anchor = next((a for a in ANCHORS if a in s), None)
    if anchor is None:
        print(f'ABORT {slug}: no CTA band to insert before')
        return False

    section = (
        f'<section class="band-tight band-paper" id="faq">'
        f'<div class="wrap"><div class="narrow">'
        f'<h2>{heading}</h2>{faq_html(faqs)}'
        f'</div></div></section>\n\n'
    )
    s = s.replace(anchor, section + anchor, 1)

    schema = ('<script type="application/ld+json">'
              + json.dumps(faq_schema(faqs), separators=(',', ':'))
              + '</script>\n')
    if '</head>' not in s:
        print(f'ABORT {slug}: no </head>')
        return False
    s = s.replace('</head>', schema + '</head>', 1)

    p.write_text(s, encoding='utf-8')
    print(f'ok {slug}: {len(faqs)} questions')
    return True
