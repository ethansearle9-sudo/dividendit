#!/usr/bin/env python3
"""
Dividend IT page builder.

Service pages, articles and the insights hub are written as plain data in
tools/content/*.py. This script turns them into finished .html pages in the
site root, each carrying the shell markers, so `node tools/shell.js` then
drops in the shared nav and footer.

Run:  python3 tools/build_pages.py && node tools/shell.js
"""
import html, importlib.util, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = 'https://dividendit.com'
CAL = 'https://calendly.com/dividendit/an-honest-read-on-your-it'
TODAY = '2026-11-09'
FAVICON = '<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 64 64\'%3E%3Crect width=\'64\' height=\'64\' rx=\'12\' fill=\'%232d6a4f\'/%3E%3Ctext x=\'32\' y=\'44\' font-family=\'Georgia,serif\' font-size=\'38\' font-weight=\'bold\' fill=\'%23f8f8f6\' text-anchor=\'middle\'%3ED%3C/text%3E%3C/svg%3E" />'

# Pages that exist outside the builder, for related links.
EXTERNAL = {
    'guide': ('Guide', "The Owner's Guide to Outsourced IT Support That Builds Value", 'Ten chapters on making technology decisions that protect and build what the business is worth.'),
    'outsourced-it': ('Overview', 'Outsourced IT Services', 'What you get from an outsourced IT partner and what it costs.'),
    'services': ('Overview', 'How We Work: Secure, Operate, Grow', 'The three service levels and what each one includes.'),
    'exit-value': ('Research', 'Why Most Owners Never Realise Their Value', 'What separates owners who sell well from those who never sell.'),
    'succession': ('Research', 'Family Business Succession', 'Why handovers fail and how to plan one that works.'),
    'startup-survival': ('Research', 'Why Businesses Fail Before Year Five', 'The patterns behind early failure.'),
    'own-vs-rent-compute': ('Research', 'Own vs Rent: The Economics of Your Compute', 'When owning infrastructure beats renting it from the cloud.'),
    'cost-calculator': ('Tool', 'In-House vs Outsourced IT Cost Calculator', 'Compare the full cost of an internal IT hire with an outsourced team.'),
    'value-calculator': ('Tool', 'Exit Value Impact Calculator', 'See what a change in earnings or risk does to enterprise value.'),
}

e = html.escape


def load_content():
    pages = []
    for f in sorted((ROOT / 'tools' / 'content').glob('*.py')):
        spec = importlib.util.spec_from_file_location(f.stem, f)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        pages += getattr(mod, 'PAGES', [])
    return pages


def strip(s):
    return re.sub(r'<[^>]+>', '', s)


def head(p, schema):
    title = p['title']
    desc = p['meta']
    url = SITE + '/' + p['slug']
    robots = '<meta name="robots" content="noindex" />\n  ' if p.get('noindex') else ''
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <!-- Self-exclusion. Visit any page with ?notme=1 to stop this browser being
       measured, ?notme=0 to start again. Survives IP and country changes. -->
  <script>
    (function(){{
      try {{
        var q = new URLSearchParams(location.search);
        if (q.has('notme')) {{
          if (q.get('notme') === '0') localStorage.removeItem('ddit_optout');
          else localStorage.setItem('ddit_optout', '1');
        }}
        var off = localStorage.getItem('ddit_optout') === '1';
        if (off) window['ga-disable-G-NRJXMHZ0N7'] = true;
        // Only when the switch was just used: show a visible confirmation, so it
        // can be checked on a phone where there is no console to read.
        if (q.has('notme')) {{
          document.addEventListener('DOMContentLoaded', function(){{
            var n = document.createElement('div');
            n.setAttribute('role', 'status');
            n.style.cssText = 'position:fixed;left:50%;transform:translateX(-50%);bottom:20px;z-index:99999;'
              + 'max-width:92vw;padding:14px 18px;border-radius:10px;font:600 15px/1.4 system-ui,sans-serif;'
              + 'color:#fff;box-shadow:0 6px 24px rgba(0,0,0,.28);text-align:center;'
              + 'background:' + (off ? '#2d6a4f' : '#8a1c1c');
            n.textContent = off
              ? 'Analytics OFF on this browser. Your visits are no longer counted.'
              : 'Analytics ON for this browser. Your visits are being counted again.';
            document.body.appendChild(n);
            setTimeout(function(){{ n.style.transition = 'opacity .6s'; n.style.opacity = '0'; }}, 6000);
            setTimeout(function(){{ n.remove(); }}, 6800);
          }});
        }}
      }} catch (e) {{}}
    }})();
  </script>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-NRJXMHZ0N7"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-NRJXMHZ0N7');
    // Same helper the hand-built pages use, so event names stay consistent.
    function trackEvent(name, params){{ try {{ gtag('event', name, params || {{}}); }} catch(e){{}} }}
  </script>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{e(title)}</title>
  <meta name="description" content="{e(desc)}" />
  {robots}<link rel="canonical" href="{url}" />
  <meta property="og:title" content="{e(p.get('og_title', title.replace(' | Dividend IT', '')))}" />
  <meta property="og:description" content="{e(desc)}" />
  <meta property="og:type" content="{'article' if p['kind'] == 'article' else 'website'}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="{SITE}/og-image.png" />
  <meta name="twitter:card" content="summary_large_image" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600;9..40,700&display=swap" rel="stylesheet" />
  {FAVICON}
  <link rel="stylesheet" href="/assets/page.css" />
  {''.join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schema)}
<!-- shell:head -->
<!-- /shell:head -->
</head>
<body>
<!-- shell:nav -->
<!-- /shell:nav -->
<main>
'''


TAIL = '''</main>
<!-- shell:footer -->
<!-- /shell:footer -->
<script>
(function(){
  if (typeof trackEvent !== 'function') return;
  var hit = {};
  window.addEventListener('scroll', function(){
    var d = document.documentElement;
    var h = Math.max(d.scrollHeight, document.body.scrollHeight) - window.innerHeight;
    if (h <= 0) return;
    var pct = (window.scrollY / h) * 100;
    [50, 75, 90].forEach(function(m){
      if (pct >= m && !hit[m]) {
        hit[m] = true;
        trackEvent('scroll_depth', { page_id: location.pathname, percent: m });
      }
    });
  }, { passive: true });
})();
</script>
<!-- shell:scripts -->
<!-- /shell:scripts -->
</body>
</html>
'''


def crumbs_html(trail):
    parts = ['<a href="/">Home</a>']
    for label, href in trail[:-1]:
        parts.append(f'<a href="{href}">{e(label)}</a>')
    parts.append(e(trail[-1][0]))
    return '<div class="crumbs" role="navigation" aria-label="Breadcrumb">' + '<span>/</span>'.join(parts) + '</div>'


def crumbs_schema(trail):
    items = [{'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + '/'}]
    for i, (label, href) in enumerate(trail, start=2):
        items.append({'@type': 'ListItem', 'position': i, 'name': label, 'item': SITE + href})
    return {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': items}


def faq_schema(faqs):
    return {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': strip(q), 'acceptedAnswer': {'@type': 'Answer', 'text': strip(' '.join(a if isinstance(a, list) else [a]))}}
        for q, a in faqs]}


def faq_html(faqs):
    out = ['<div class="faq">']
    for q, a in faqs:
        paras = a if isinstance(a, list) else [a]
        out.append(f'<details><summary>{q}</summary><div class="a">' + ''.join(f'<p>{x}</p>' for x in paras) + '</div></details>')
    out.append('</div>')
    return '\n'.join(out)


def related_html(slugs, cards, heading='Related'):
    items = []
    for s in slugs:
        k, t, d = cards[s]
        items.append(f'<a class="rc" href="/{s}"><span class="rk">{e(k)}</span><span class="rt">{e(t)}</span><span class="rd">{e(d)}</span></a>')
    return f'<div class="rel">{"".join(items)}</div>'


def cta_band(h, p, secondary=None):
    sec = f'<a class="link-arrow" href="{secondary[1]}">{e(secondary[0])}</a>' if secondary else ''
    return f'''<section class="cta-band"><div class="wrap">
  <h2>{h}</h2>
  <p>{p}</p>
  <div class="actions"><a class="btn green" href="{CAL}" target="_blank" rel="noopener">Book a 20-minute call</a>{sec}</div>
</div></section>
'''


AREA_SERVED = [
    {'@type': 'Country', 'name': 'Ireland'},
    {'@type': 'City', 'name': 'Dublin'},
    {'@type': 'Country', 'name': 'United Kingdom'},
]

# Service-area business: no street address, but Google still needs to know
# where we operate. Linked by @id to the Organization node on the homepage.
PROVIDER = {
    '@type': ['Organization', 'ProfessionalService'],
    '@id': SITE + '/#org',
    'name': 'Dividend IT',
    'url': SITE + '/',
    'areaServed': AREA_SERVED,
}


def build_service(p, cards):
    trail = p['trail']
    schema = [
        {'@context': 'https://schema.org', '@type': 'Service', 'name': p['service_name'], 'serviceType': p['service_name'],
         'description': p['meta'], 'url': SITE + '/' + p['slug'],
         'provider': PROVIDER,
         'areaServed': ([{'@type': 'City', 'name': p['city']},
                         {'@type': 'Country', 'name': p['country']}]
                        if p.get('city') else AREA_SERVED),
         'audience': {'@type': 'BusinessAudience', 'name': 'Business owners and shareholders'}},
        crumbs_schema(trail), faq_schema(p['faqs'])]
    o = [head(p, schema)]
    glance = ''.join(f'<dt>{e(k)}</dt><dd>{v}</dd>' for k, v in p['glance'])
    o.append(f'''<section class="sv-hero"><div class="wrap">
  {crumbs_html(trail)}
  <div class="sv-hero-grid">
    <div>
      <div class="label">{e(p['eyebrow'])}</div>
      <h1>{p['h1']}</h1>
      <p class="sv-lead">{p['lead']}</p>
      <div class="actions"><a class="btn" href="{CAL}" target="_blank" rel="noopener">Book a 20-minute call</a><a class="link-arrow" href="#included">See what's included</a></div>
    </div>
    <aside class="glance" aria-label="At a glance"><h2>At a glance</h2><dl>{glance}</dl></aside>
  </div>
</div></section>
''')
    # problem
    o.append(f'''<section class="blk"><div class="wrap"><div class="narrow prose">
  <div class="label">{e(p.get('problem_label', 'The problem'))}</div>
  <h2 class="h2">{p['problem_h']}</h2>
  {''.join(f'<p>{x}</p>' for x in p['problem'])}
  {f'<div class="pull">{p["quote"]}<span class="by">{p.get("quote_by", "")}</span></div>' if p.get('quote') else ''}
</div></div></section>
''')
    # included
    cards_html = ''.join(f'<div class="card"><span class="tick">&#10003;</span><h3>{h}</h3><p>{d}</p></div>' for h, d in p['included'])
    o.append(f'''<section class="blk alt" id="included"><div class="wrap">
  <div class="label">What's included</div>
  <h2 class="h2">{p.get('included_h', 'What you get')}</h2>
  {f'<p class="intro">{p["included_intro"]}</p>' if p.get('included_intro') else ''}
  <div class="grid3">{cards_html}</div>
</div></section>
''')
    # steps
    n = len(p['steps'])
    steps = ''.join(f'<div class="step"><h3>{h}</h3><p>{d}</p></div>' for h, d in p['steps'])
    o.append(f'''<section class="blk dark"><div class="wrap">
  <div class="label">How it works</div>
  <h2 class="h2">{p.get('steps_h', 'How it works')}</h2>
  <div class="steps{' n3' if n == 3 else ''}">{steps}</div>
</div></section>
''')
    # value
    vl = ''.join(f'<li><strong>{h}</strong>{d}</li>' for h, d in p['value'])
    o.append(f'''<section class="blk alt"><div class="wrap"><div class="split">
  <div><div class="label">What it's worth</div><h2 class="h2">{p['value_h']}</h2><p class="intro">{p['value_intro']}</p></div>
  <ul class="vlist">{vl}</ul>
</div></div></section>
''')
    # fit
    if p.get('fit'):
        yes = ''.join(f'<li>{x}</li>' for x in p['fit'][0])
        no = ''.join(f'<li>{x}</li>' for x in p['fit'][1])
        o.append(f'''<section class="blk"><div class="wrap">
  <div class="label">Is it right for you?</div>
  <h2 class="h2">An honest fit check</h2>
  <div class="fit"><div class="yes"><h3>A good fit if</h3><ul>{yes}</ul></div><div class="no"><h3>Probably not the right fit if</h3><ul>{no}</ul></div></div>
</div></section>
''')
    o.append(f'''<section class="blk{' alt' if p.get('fit') else ''}"><div class="wrap"><div class="narrow">
  <div class="label">Questions owners ask</div>
  <h2 class="h2">Frequently asked questions</h2>
  {faq_html(p['faqs'])}
</div></div></section>
''')
    o.append(f'''<section class="blk{'' if p.get('fit') else ' alt'}"><div class="wrap">
  <div class="label">Keep reading</div>
  <h2 class="h2">Related services and guides</h2>
  {related_html(p['related'], cards)}
</div></section>
''')
    o.append(cta_band(p.get('cta_h', 'Get a straight answer on where you stand.'),
                      p.get('cta_p', 'Twenty minutes, no jargon, no obligation. You will leave knowing what is working, what is exposed, and what it is costing you.'),
                      p.get('cta_secondary')))
    o.append(TAIL)
    return ''.join(o)


def build_article(p, cards):
    url = SITE + '/' + p['slug']
    schema = [
        {'@context': 'https://schema.org', '@type': 'Article', 'headline': strip(p['h1']), 'description': p['meta'],
         'author': {'@type': 'Person', 'name': 'Ethan Searle', 'jobTitle': 'Founder, Dividend IT'},
         'publisher': PROVIDER,
         'datePublished': p.get('published', TODAY), 'dateModified': TODAY, 'mainEntityOfPage': url, 'url': url,
         'image': SITE + '/og-image.png'},
        crumbs_schema(p['trail'])]
    if p.get('faqs'):
        schema.append(faq_schema(p['faqs']))
    if p.get('howto'):
        schema.append({'@context': 'https://schema.org', '@type': 'HowTo', 'name': p['howto']['name'],
                       'step': [{'@type': 'HowToStep', 'name': n, 'text': t} for n, t in p['howto']['steps']]})
    o = [head(p, schema)]
    toc = ''.join(f'<li><a href="#{sid}">{strip(h)}</a></li>' for sid, h, _ in p['sections'])
    urgent = f'<div class="urgent">{p["urgent"]}</div>' if p.get('urgent') else ''
    o.append(f'''<section class="ar-hero"><div class="wrap"><div class="narrow">
  {crumbs_html(p['trail'])}
  <div class="label">{e(p['eyebrow'])}</div>
  <h1>{p['h1']}</h1>
  <p class="ar-sub">{p['sub']}</p>
  <div class="ar-meta"><span>By Ethan Searle, Founder</span><span>&middot;</span><span>{p['read']} min read</span><span>&middot;</span><span>Updated November 2026</span></div>
  {urgent}
  <div class="toc" role="navigation" aria-label="Contents"><h2>In this article</h2><ol>{toc}</ol></div>
</div></div></section>
''')
    for sid, h, body in p['sections']:
        o.append(f'<section class="ar-sec" id="{sid}"><div class="wrap"><div class="narrow">\n<h2>{h}</h2>\n{body}\n</div></div></section>\n')
    if p.get('faqs'):
        o.append(f'<section class="ar-sec" id="faq"><div class="wrap"><div class="narrow"><h2>Frequently asked questions</h2>{faq_html(p["faqs"])}</div></div></section>\n')
    if p.get('sources'):
        src = ''.join(f'<li>{s}</li>' for s in p['sources'])
        o.append(f'<section class="ar-sec"><div class="wrap"><div class="narrow"><h2>Sources</h2><ol class="sources">{src}</ol></div></div></section>\n')
    o.append(f'''<section class="blk alt"><div class="wrap">
  <div class="label">Keep reading</div>
  <h2 class="h2">Related guides and services</h2>
  {related_html(p['related'], cards)}
</div></section>
''')
    o.append(cta_band(p.get('cta_h', 'Want a straight answer on your exposure?'),
                      p.get('cta_p', 'Twenty minutes with someone who will tell you what is working, what is exposed, and what to fix first. No jargon, no obligation.'),
                      p.get('cta_secondary')))
    o.append(TAIL)
    return ''.join(o)


def build_hub(p, cards):
    schema = [{'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': strip(p['h1']), 'url': SITE + '/' + p['slug'], 'description': p['meta']},
              crumbs_schema(p['trail'])]
    o = [head(p, schema)]
    o.append(f'''<section class="ar-hero"><div class="wrap">
  {crumbs_html(p['trail'])}
  <div class="label">{e(p['eyebrow'])}</div>
  <h1>{p['h1']}</h1>
  <p class="ar-sub">{p['sub']}</p>
</div></section>
''')
    for gi, (gh, gp, items) in enumerate(p['groups']):
        tiles = []
        for slug, read, feature in items:
            k, t, d = cards[slug]
            cls = ' class="feature"' if feature else ''
            tiles.append(f'<a href="/{slug}"{cls}><span class="k">{e(k)}</span><span class="t">{e(t)}</span><span class="d">{e(d)}</span><span class="r">{read}</span></a>')
        o.append(f'''<section class="blk{' alt' if gi % 2 == 0 else ''}"><div class="wrap">
  <h2 class="h2">{gh}</h2><p class="intro">{gp}</p>
  <div class="hub">{''.join(tiles)}</div>
</div></section>
''')
    o.append(cta_band('Rather talk it through?', 'Twenty minutes, no jargon, no obligation. Bring the question that is on your mind.'))
    o.append(TAIL)
    return ''.join(o)


def main():
    pages = load_content()
    cards = dict(EXTERNAL)
    for p in pages:
        cards[p['slug']] = (p['card_kind'], p['card_title'], p['card_desc'])
    for p in pages:
        for s in p.get('related', []):
            assert s in cards, f"{p['slug']}: unknown related page {s}"
        fn = {'service': build_service, 'location': build_service, 'article': build_article, 'hub': build_hub}[p['kind']]
        (ROOT / f"{p['slug']}.html").write_text(fn(p, cards), encoding='utf-8')
    print(f'built {len(pages)} pages')


if __name__ == '__main__':
    main()
