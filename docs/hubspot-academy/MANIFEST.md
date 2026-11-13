# HubSpot Academy — ingestion manifest

The full catalogue, enumerated from `academy.hubspot.com/sitemap.xml` on
2026-11-13, so ingestion is resumable across sessions rather than restarted.

## Scale, measured not guessed

| | Count |
|---|---|
| URLs in the Academy sitemap | 1,417 |
| Less certified-trainer profiles | −475 |
| **Academy content URLs** | **942** |
| Less translations (`-ja`, `-fr`, `-de`, `-es`, `-pt`) and localised webinars | −277 |
| **English content items** | **665** |
| Of which are full courses (the rest are individual lessons) | 105 |

The catalogue page itself reports **1,196 courses-and-lessons** and **105**
when filtered to `contentType=COURSE`, which corroborates the sitemap figure.

## Why this cannot be bulk-scraped

Both the public course pages and the logged-in player are client-rendered —
a raw `fetch()` of `academy.hubspot.com/<slug>` returns zero body text. Every
item therefore needs a real browser render, roughly one round trip each, and
video transcripts sit behind the logged-in player as PDFs on
`hubspotusercontent`. The AEO certification (7 lessons) took about 20 tool
calls end to end. 665 items is a multi-session job, which is what this
manifest exists to track.

## Status

- [x] **AEO Fundamentals certification** — 7/7 lessons, full transcripts in
      `docs/hubspot-aeo/`, doctrine distilled to the project playbook.
- [ ] Everything below.

## Priority order

Driven by Dividend IT's two engines: SEO/content, and outbound email.
`crm_ops` (143), `web_cms` (44) and `service` (35) are HubSpot product
training — how to operate the software — and rank last for that reason.

| Priority | Category | Items |
|---|---|---|
| 1 | seo_aeo | 38 |
| 2 | email | 28 |
| 3 | inbound_strategy | 37 |
| 4 | content | 75 |
| 5 | sales | 57 |
| 6 | abm | 10 |
| 7 | ai | 58 |
| 8 | social | 57 |
| 9 | ads_paid | 49 |
| 10 | crm_ops | 143 |
| 11 | web_cms | 44 |
| 12 | service | 35 |
| — | uncategorised | 146 |

---

## 1. seo_aeo (38)

Items already covered by the AEO certification are marked `[done]`.

```
measure-iterate-and-build-a-sustainable-aeo-practice
aeo-fundamentals-certification                                    [done]
seo-reporting
creating-topic-clusters-and-pillar-pages
from-insight-to-action-citations-recommendations-and-content
reading-your-visibility-dashboard-scores-sentiment-and-competitors
planning-content-for-search-and-ai-visibility                     [done]
the-ai-search-shift-why-aeo-matters-now
rethinking-visibility-in-the-age-of-answer-engines                [done]
establishing-your-aeo-foundation                                  [done]
seo-2-technical-seo-indexation-and-page-structure
optimizing-external-signals-for-aeo-off-site
seo-3-content-optimization-structured-data-and-link-building
the-fundamentals-of-an-effective-seo-content-strategy
measuring-what-matters-in-aeo                                     [done]
building-your-own-search-insights-report
seo-in-the-age-of-ai-en
winning-on-answer-engines
seo-training
optimizing-your-website-for-search-engines-in-hubspot
the-new-search-reality-foundational-mindset-shifts
google-seo-tutorial
on-page-technical-seo
getting-started-from-aeo-grader-to-your-live-dashboard
seo-1-how-search-engines-work-and-how-to-define-your-strategy
enhancing-seo-for-a-website
optimizing-for-ai-citation
seo-tutorial
measuring-what-matters-in-ai-driven-search
wordpress-seo
seo-keyword-research
winning-on-googles-ai-powered-serp-optimizing-for-ai-overviews-and-ai-mode
establishing-the-foundations-of-your-aeo-strategy
build-search-insights-report
introduction-to-paid-search-advertising
creating-a-digital-presence-with-content-marketing-and-seo
implementing-aeo-with-hubspot-certification
seo-basics
```

**Highest value here:** `seo-1/2/3` (the three-part SEO series),
`seo-keyword-research`, `creating-topic-clusters-and-pillar-pages` and
`optimizing-external-signals-for-aeo-off-site` — that last one maps directly
to Level 4 of the Hierarchy of AEO Needs, which is our current constraint.

## 2. email (28)

```
understanding-permissions-and-deliverability
improving-your-email-marketing-through-testing
engaging-your-email-deliverability-in-hubspot
email-marketing-strategy-fundamentals
components-of-a-high-performing-email
mapping-your-email-marketing-strategy-through-hubspot-campaigns
email-marketing
connecting-your-email-sending-domain-to-hubspot
creating-and-managing-your-email-marketing-contacts-and-segments-in-hubspot
email-marketing-certification-en
reviewing-email-performance-as-a-business-builder
creating-impactful-emails-in-hubspot
measuring-success-email-marketing-efforts
testing-and-analyzing-your-emails-in-hubspot
designing-emails-in-marketing-hub-starter
design-in-email-marketing
lead-nurturing-with-hubspot-free-email
understanding-lead-nurturing
lead-nurturing-with-hubspot
email-marketing-software
email-marketing-on-the-go-hubspot-mobile-email
analyzing-your-marketing-emails-2023
getting-started-with-email-in-hubspot
beginning-email-marketing-as-a-business-builder
automating-your-email-marketing-in-hubspot
personalizing-your-email-marketing-in-hubspot
creating-a-lead-nurturing-workflow
sustaining-digital-marketing-through-emails
```

**Highest value here:** `email-marketing-certification-en`,
`email-marketing-strategy-fundamentals`, `components-of-a-high-performing-email`,
`understanding-permissions-and-deliverability` and `understanding-lead-nurturing`.
Deliverability matters most for the outbound engine — a cold sequence that
lands in spam is worse than no sequence.

## 3. inbound_strategy (37)

```
creating-content-for-the-buyers-journey
flywheel
customer-journey-map
loop-marketing-fundamentals
customer-journey-mapping
inbound
developing-a-growth-marketing-mindset
the-power-of-personalization-and-automation
customer-journey-analytics
assessing-flywheel-growth-grader
inbound-fundamentals
loop-marketing-fundamentals-en
inbound-marketing-fundamentals-22
using-buyer-personas-in-sales-enablement
applying-revops-to-the-flywheel
introduction-to-ecommerce-inbound-marketing
buyers-journey
using-buyer-personas-in-hubspot
Using-Workflows-to-Power-Your-Inbound-Strategy
setting-up-personal-development-environment
accelerate-growth-flywheel
inbound-marketing-optimization
inbound-marketing
inbound-service-fundamentals
identifying-flywheel-insights
inbound-sales
how-to-create-buyer-personas
creating-memorable-user-experiences-with-website-personalization
getting-started-with-your-ecommerce-inbound-marketing-plan
buyer-personas
flywheel-introduction
google-ads-customer-journey
how-companies-accelerated-growth-flywheel
inbound-sales-fundamentals
delivering-personalized-sales-presentations
creating-your-ecommerce-inbound-marketing-strategy
personalizing-your-email-marketing-in-hubspot
```

**Highest value here:** `inbound-fundamentals`, `inbound-marketing`,
`buyers-journey`, `how-to-create-buyer-personas`, `inbound-sales-fundamentals`
and `loop-marketing-fundamentals` (HubSpot's newer replacement for the
flywheel framing). The e-commerce items do not apply to an MSP.

## 6. abm (10)

```
abm-in-hubspot-for-manufacturing
abm-platforms
get-started-with-abm
abm-campaigns
abm-strategy
abm-statistics
abm-intent-data
account-based-marketing-to-account-based-revops-orchestrated-by-hubspot
account-based-selling
abm-advertising-tools
```

Small but disproportionately relevant: Dividend IT sells to a defined list of
named accounts of 10–150 people, which is account-based selling by definition.
`abm-in-hubspot-for-manufacturing` is directly on-vertical.

---

## Method that works (proven on AEO)

1. Open the lesson in the logged-in player (`app-eu1.hubspot.com/academy/<portal>/tracks/...`).
2. Open its **Resources** tab and read the transcript PDF URL — naming is
   inconsistent, so the URL must be scraped, not guessed.
3. In a tab on a CORS-permissive origin, load pdf.js from cdnjs, `fetch()` the
   PDF, and extract per-page text into a JS variable.
4. Dump that text into `document.body` as a `<pre>` and read it with
   `get_page_text` — `javascript_tool` truncates at roughly 1,000 characters,
   while `get_page_text` handled 31,000.
5. Write the transcript to `docs/hubspot-academy/<category>/<slug>.md`.
6. Distil the doctrine into the project playbook; the transcript is the source
   of record, the playbook is what gets applied.

Constraint worth remembering: the container cannot reach `academy.hubspot.com`
or `hubspotusercontent` directly — everything goes through the browser.
