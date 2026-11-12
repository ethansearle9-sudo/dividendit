#!/usr/bin/env python3
"""Audit every live page against HubSpot Academy's AEO Content Optimization
Checklist (AEO Fundamentals certification, 2026).

The checklist has eight sections. Not every item can be judged by a machine —
"reflects genuine expertise" needs a human — so this checks the ~20 that can be
measured objectively and reports the rest as manual.

Run:  python3 tools/aeo_audit.py
"""
import re, pathlib, collections, json, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

VAGUE_HEADINGS = {
    'overview', 'timeline', 'introduction', 'summary', 'details', 'background',
    'benefits', 'features', 'about', 'how it works', 'what you get', 'the problem',
    'next steps', 'conclusion', 'our approach', 'results', 'pricing', 'faqs', 'faq',
}
TRANSITIONS = [
    'as mentioned above', 'as mentioned earlier', 'as we discussed',
    'building on the previous', 'as noted above', 'as described above',
    'in the previous section', 'as stated earlier',
]


def strip_tags(h):
    h = re.sub(r'<(script|style).*?</\1>', ' ', h, flags=re.S | re.I)
    h = re.sub(r'<[^>]+>', ' ', h)
    for a, b in [('&nbsp;', ' '), ('&amp;', '&'), ('&rsquo;', "'"), ('&mdash;', '—'), ('&#x27;', "'")]:
        h = h.replace(a, b)
    return re.sub(r'\s+', ' ', h).strip()


def body_only(h):
    for a, b in [('<!-- shell:nav -->', '<!-- /shell:nav -->'),
                 ('<!-- shell:footer -->', '<!-- /shell:footer -->')]:
        h = re.sub(re.escape(a) + r'.*?' + re.escape(b), ' ', h, flags=re.S)
    return h


# Heading words that mean the page actually contrasts options, which is the
# condition HubSpot attaches to the comparison-table item.
COMPARATIVE = (' vs ', ' vs.', 'versus', 'compare', 'comparison', 'compared',
               'difference between', 'which is better', 'alternative',
               'instead of', 'or rent', 'or buy', 'in-house or')

# Pages with no audience content: the editorial checks do not apply.
UTILITY = {'privacy', 'terms', 'cookie-policy', 'thank-you', '404'}


def first_answer(body_html):
    """Text of the first substantive paragraph after the H1."""
    m = re.search(r'</h1>(.*)', body_html, re.S)
    tail = m.group(1) if m else body_html
    for p in re.findall(r'<p[^>]*>(.*?)</p>', tail, re.S):
        t = strip_tags(p)
        if len(t.split()) >= 8:
            return t
    return ''


def audit_page(slug, html):
    b = body_only(html)
    txt = strip_tags(b)
    low = txt.lower()

    title = re.search(r'<title>(.*?)</title>', html, re.S)
    title = strip_tags(title.group(1)) if title else ''
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', b, re.S)
    h1 = strip_tags(h1.group(1)) if h1 else ''
    h2s = [strip_tags(x) for x in re.findall(r'<h2[^>]*>(.*?)</h2>', b, re.S)]
    h3s = [strip_tags(x) for x in re.findall(r'<h3[^>]*>(.*?)</h3>', b, re.S)]
    desc = re.search(r'<meta name="description" content="(.*?)"', html, re.S)
    desc = desc.group(1) if desc else ''

    ans = first_answer(b)
    ans_words = len(ans.split())
    # HubSpot's checklist scopes the comparison-table item: "Comparison tables
    # are used WHERE THE CONTENT evaluates or contrasts two or more options,
    # tools, or approaches." Scoring every page against it invents a gap and
    # pushes tables onto pages that compare nothing. A page counts as
    # comparative only if its own headings say so.
    heads = ' '.join([h1] + h2s + h3s).lower() if (h1 or h2s or h3s) else ''
    comparative = any(t in heads for t in COMPARATIVE)
    # Utility pages (privacy, terms) carry no audience content, so the
    # editorial checks do not apply to them.
    utility = slug in UTILITY
    q_heads = [x for x in h2s + h3s if x.strip().endswith('?')]
    vague = [x for x in h2s if x.strip().lower().rstrip(':') in VAGUE_HEADINGS]
    imgs = re.findall(r'<img[^>]*>', b)

    return {
        'slug': slug,
        # 1. Answer-first structure
        'answer_40_60': 40 <= ans_words <= 60,
        'answer_words': ans_words,
        # 2. Headers and page structure
        'title_60': 0 < len(title) <= 60,
        'has_h1': bool(h1),
        'h2_not_vague': not vague,
        'vague_h2': vague,
        'question_heads': len(q_heads),
        'has_question_head': utility or bool(q_heads),
        'hierarchy_ok': not (h3s and not h2s),
        # 3. Section independence
        'no_transitions': not any(t in low for t in TRANSITIONS),
        'n_h2': len(h2s),
        # 4. Query fan-out
        'has_faq': utility or ('FAQPage' in html),
        'n_faq': len(re.findall(r'<details', b)),
        # 5. Definitions, lists, scannable
        'has_list': utility or bool(re.search(r'<(ul|ol)\b', b)),
        # n/a on non-comparative pages, per the checklist's own wording.
        'has_table': (not comparative) or bool(re.search(r'<table\b', b)),
        'comparative': comparative,
        'utility': utility,
        # 6. Credibility and information gain
        'has_author': bool(re.search(r'\bauthor\b|\bbyline\b|itemprop="author"|"author"', html, re.I)),
        'has_outbound_citation': bool(re.search(r'href="https?://(?!(?:www\.)?dividendit\.com)', b)),
        # 7. Freshness
        'has_published_date': bool(re.search(r'datePublished|<time', html)),
        'has_modified_date': bool(re.search(r'dateModified', html)),
        # 8. Audience alignment
        'desc_present': bool(desc),
        'imgs': len(imgs),
        'imgs_with_alt': len([i for i in imgs if re.search(r'alt="[^"]+"', i)]),
    }


CHECKS = [
    ('answer_40_60',          '1. Opens with a 40-60 word direct answer'),
    ('title_60',              '2. Title tag 60 characters or under'),
    ('h2_not_vague',          '2. H2s descriptive, not vague'),
    ('has_question_head',     '2. At least one question-phrased heading'),
    ('hierarchy_ok',          '2. Heading hierarchy logical'),
    ('no_transitions',        '3. No "as mentioned above" style transitions'),
    ('has_faq',               '4. FAQ section with extractable Q&A'),
    ('has_list',              '5. Uses bulleted or numbered lists'),
    ('has_table',             '5. Uses a comparison table'),
    ('has_author',            '6. Named author with a visible byline'),
    ('has_outbound_citation', '6. Claims linked to an original source'),
    ('has_published_date',    '7. Visible publish date'),
    ('has_modified_date',     '7. Last-updated date'),
    ('desc_present',          '8. Meta description present'),
]

MANUAL = [
    '1. Opening answer is self-contained',
    '1. Supporting detail comes after the answer',
    '3. Each H2 stands alone as an answer',
    '4. Page addresses natural follow-up questions',
    '6. Page carries original value not on competing pages',
    '6. Content reflects genuine expertise',
    '8. Content addresses a clearly defined audience',
]


def main():
    rows = []
    for p in sorted(ROOT.glob('*.html')):
        h = p.read_text(encoding='utf-8')
        if 'noindex' in h:
            continue
        rows.append(audit_page(p.stem, h))

    n = len(rows)
    print(f'HubSpot AEO Content Optimization Checklist — {n} live pages\n')
    print(f'{"check":52s} {"pass":>6s}  {"fail":>5s}')
    print('-' * 68)
    fails = {}
    for key, label in CHECKS:
        bad = [r['slug'] for r in rows if not r[key]]
        fails[key] = bad
        print(f'{label:52s} {n - len(bad):5d}  {len(bad):5d}')

    print('\nWorst gaps:')
    for key, label in sorted(CHECKS, key=lambda kv: -len(fails[kv[0]]))[:6]:
        bad = fails[key]
        if not bad:
            continue
        ex = ', '.join(bad[:5]) + (f' …+{len(bad)-5}' if len(bad) > 5 else '')
        print(f'  {len(bad):3d}/{n}  {label}\n          {ex}')

    alt_missing = sum(r['imgs'] - r['imgs_with_alt'] for r in rows)
    total_imgs = sum(r['imgs'] for r in rows)
    print(f'\n  images sitewide: {total_imgs} ({alt_missing} without alt text)')

    print('\nNot machine-checkable — needs a human pass:')
    for m in MANUAL:
        print(f'  - {m}')

    out = ROOT / 'tools' / '.aeo_audit.json'
    out.write_text(json.dumps({'rows': rows, 'fails': fails}, indent=1), encoding='utf-8')
    return 0


if __name__ == '__main__':
    sys.exit(main())
