# Measuring What Matters in AEO

HubSpot Academy — AEO Fundamentals certification. Transcript of the four videos
in this lesson. Source: HubSpot Academy, © HubSpot. Reference for Dividend IT.

---

## Video: The AEO measurement gap

The traditional SEO metrics — organic traffic, keyword ranking, click-through rate, impressions, conversions — all depend on the same sequence: a person types a query, scans a list of links, clicks one, lands on your site. Impressions and ranking come from them landing on the results page. CTR captures the decision to click. Organic traffic registers on arrival. Conversions measure what they do after.

**The entire model breaks down when the click doesn't happen.**

With an AI Overview, impressions and ranking still register because your listing appeared — but CTR drops because the person got their answer, organic traffic never registers the visit, and conversions can't be tracked because they never arrived. When someone asks ChatGPT, Perplexity, Claude or Gemini for a recommendation, your brand might be mentioned, cited or linked, and **none of it shows up in your analytics at all.**

> **Your brand can be visible, influential and trusted by AI systems while your traditional metrics show no change — or a decline. If you're only looking at clicks and traffic, you could easily conclude your content isn't performing when the opposite is true.**

**Two examples of how that plays out:**

- A page with **high impressions but declining clicks** looks like a problem under a traditional lens. It may actually be earning visibility in AI Overviews, where content is surfaced and read on the results page. Under an AEO lens that can be a sign the content is doing exactly what you want.
- **Branded search volume increases but direct organic traffic to your optimised pages stays flat.** Your content could be appearing in AI answers, building awareness even when people never click through at that moment — they search for you by name later that day or week. That downstream effect is invisible if you only measure direct organic traffic.

Don't stop tracking traditional metrics; conventional search still drives the majority of web traffic. But reporting needs to expand to **capture what's happening before or instead of the click, not just after it.**

---

## Video: Which AEO metrics to trust — the three tiers

**Tier one: directly observable metrics.** Grounded in actual user actions on your website, trackable in Google Analytics and Search Console. Because they measure what people do rather than what AI systems say, they give the most reliable picture. **These are the numbers to lead with.**

- **AI referral traffic.** In GA you can identify sessions originating from ChatGPT, Perplexity, Claude and so on — they show up as referral sources in traffic acquisition reports. Volume will likely be small compared with organic search, but this traffic tends to be high-intent: **early HubSpot data suggests visitors who first encounter a brand through AI responses arrive with more context and more conviction, converting at more than three times the rate of traditional visitors.**
  - Part of why the volume looks small: most people don't click through to a site directly from an AI response. They encounter your brand in an AI answer, then validate it through review sites, social or YouTube, and eventually visit on their own — by which time GA may attribute the session to direct traffic or branded search. **AI referral traffic is just the visible portion of a larger AI-influenced audience**, but it's a reliable floor. Pairing it with a post-purchase "how did you first hear about us" survey helps capture the rest.
- **Branded search volume.** When AI systems reference your brand, people often follow up by searching for you by name. An uptick in branded queries in Search Console is a reliable signal that AI visibility is translating into real awareness. Free to track and difficult to misinterpret.
- **Conversion data from AI-referred visitors.** Knowing AI traffic is arriving isn't enough. Tracking conversion rates, engagement and lead attribution for AI-referred sessions *specifically* is what tells you whether AEO work is contributing to business outcomes.

**Tier two: metrics that require interpretation.** Real, but they don't connect cleanly to behaviour on your site, often need manual effort or specialist tools, and can shift depending on when you check. Use them to identify patterns and inform strategy rather than treating any single data point as definitive.

- **AI citation and mention tracking.** A **citation** is when an AI system includes a clickable link to your content as a source. A **mention** is when your brand appears in the text without a link. Citation tracking tells you whether AI systems are sending traffic; mention tracking tells you whether they're shaping how people perceive your brand.
- **AI Overview appearances.** Monitorable through Search Console data patterns, but Google provides no clean separate report — you read the signals indirectly, e.g. pages gaining impressions without a proportional increase in clicks.

**Tier three: directional indicators.** The broadest view, the most noise. They measure what AI systems are *saying* rather than what users are *doing*. Useful for trends over weeks and months, unreliable as point-in-time measurements.

- **AI visibility scores and share-of-voice percentages.** A visibility score measures how often your brand appears when AI systems respond to relevant queries; share of voice compares your presence against competitors.
- **The reliability problem.** A 2026 SparkToro study had 600 volunteers run the same prompts through ChatGPT, Claude and Google's AI features thousands of times. **There was less than a one-in-one-hundred chance that ChatGPT or Google AI would return the same list of brands in any two responses to the same prompt.** Nearly every response was unique in which brands appeared, their order, and even how many were included. Any single check captures one moment in a system that answers differently almost every time. **Track consistently over weeks and months and watch for directional patterns; don't treat an individual score as a precise measurement, and don't use it to compare against a competitor on any given day.**

> **The closer a metric is to actual user behaviour on your website, the more confidently you can make decisions based on it.**

---

## Video: Evaluating AI visibility tools

**Free tools — the foundation needs no investment:**

- **Google Analytics** — AI referral traffic. Isolate those sessions in traffic acquisition reports or custom explorations to track engagement and conversions for that segment.
- **Google Search Console** — branded search trends, which queries drive impressions, and patterns suggesting appearance in AI Overviews.
- **Manual prompt testing** — regularly ask the AI tools your audience uses the questions your customers would ask, and record whether your brand appears, how it's described, and whether it's linked. Results vary from prompt to prompt, but doing it consistently builds a valuable record of how AI systems perceive your brand. Qualitative insight no dashboard replaces.
- **HubSpot's AEO Grader** — free baseline analysis of how your brand appears across ChatGPT, Perplexity and Gemini.

**The HubSpot AEO tool** (in Marketing Hub Professional/Enterprise, or standalone) automates prompt testing at scale: confirm brand details and name variations, add prompts (HubSpot suggests some based on your brand identity, and you can add your own), and HubSpot runs them daily against answer engines. The dashboard gives a brand visibility score over time, a competitor landscape view with share of voice, and a **citations tab** showing which websites AI engines reference, how often they link to your domain versus competitors, your citation influence rate, which of your pages AI engines consider most authoritative, and which third-party sources most influence how AI engines describe your brand. It also surfaces prioritised recommendations with reasoning and which prompts each would impact.

Share of voice is especially valuable because **it distinguishes a drop in your own visibility from a platform-wide shift affecting everyone equally.**

**Evaluating a paid AI visibility platform — four questions:**

1. **What platforms does it actually monitor?** The most useful ones cover at least ChatGPT, Google AI and Perplexity.
2. **Does it provide context beyond simple counts?** "Mentioned 47 times" is far less useful than which queries triggered the mentions, the sentiment of each, and which pages are being cited. You want to know not just how often you appear but how you're described and whether that description is accurate.
3. **How transparent is the methodology?** Given how inconsistent AI systems are, this matters a lot. How many prompts, how often, the same prompts over time or varying? A tool running a handful of prompts monthly and outputting a score gives very different confidence from one running hundreds weekly and showing the variance. **If a vendor can't explain how they calculate their numbers, that's a red flag.**
4. **Does it integrate with your stack?** If it can't connect to GA4, Search Console or your CRM it becomes harder to tie AI visibility to business outcomes.

> **The best measurement setup isn't the one with the most tools. It's the one you can maintain consistently over time.**

---

## Video: Building your AEO reporting framework — the measurement pyramid

The data you need lives in multiple places, and looking at any one source in isolation leads to the wrong conclusion. The pyramid organises it into three layers, each building on the one below.

**Layer one — search performance (the base).** This must be in place before anything else matters, because **AI systems overwhelmingly pull from content that already performs well in traditional search: Ahrefs found 76% of AI Overview citations come from pages ranking in Google's top ten organic results.** If your content isn't being crawled, indexed and ranked, AI systems are far less likely to find and cite it.

Lives in Search Console (queries, impressions, CTR, rankings) and Google Analytics (organic traffic volume, which pages attract visitors, engagement rate, time on page, conversions).

*Question it answers:* Can search engines find my content, and is it performing in traditional search?
*Cadence:* **weekly.** The most stable and complete data you have, and your baseline.

**Layer two — AI visibility (the middle).** Once the search foundation is solid, measure whether AI systems are picking your content up.

Start with the **directly observable**: AI referral traffic in GA (sessions from domains like chat.openai.com and perplexity.ai) and branded search volume in Search Console. Both connect to real user behaviour, so they anchor this layer. Then layer in **interpretation-level** metrics: citation and mention tracking (manual or tooled) and AI Overview appearances inferred from Search Console patterns. Finally, if you have a dedicated tool, **directional indicators** like visibility scores and share of voice.

*Question it answers:* Are AI systems finding and referencing my content? **A page can rank well in traditional search and be completely absent from AI answers if it isn't structured so AI systems can extract and cite it. When that happens, layer two is where the gap shows up — and it tells you to revisit how your content is formatted and organised, not how it ranks.**
*Cadence:* **monthly.** This data is noisier than search performance; checking too frequently makes normal variation look like meaningful change. Look for directional trends, not exact numbers.

Expect incomplete data here, and that's normal. **A partial view of layer two grounded in real data is far more useful than a comprehensive dashboard built on metrics you don't trust.**

**Layer three — business impact (the top).** Built entirely on directly observable metrics: conversion rates for AI-referred visitors specifically, compared with organic search conversion rates, and AI-referred leads followed through the pipeline to see whether they become customers.

*Question it answers:* Is our search and AI visibility translating into business results? This is the layer that matters to stakeholders, and the layer that tells you where to invest more.
*Cadence:* **quarterly.** Business impact data needs time to accumulate, especially while AI referral volumes are small.

**The layers won't always connect cleanly.** You may see branded search climbing without being able to tie it to a specific citation, or strong conversion rates from a sample too small to be conclusive. **When that happens, say so.** Present what the data shows, flag the gaps, explain how you're closing them.

Build it bottom-up — each layer depends on the one below. But there's a feedback loop flowing back down: business impact data tells you which content drives the best results, which informs what you prioritise beneath it. **Over time that loop turns reporting from a static scorecard into a system that actively improves your strategy.**

**The worked scenario.** Organic traffic to a page drops 15%. Traditionally that's a problem. With the pyramid: *layer one* shows the page still ranking well with impressions actually up — so it's a click-through issue, suggesting users get their answer from an AI Overview first. *Layer two* shows AI referral traffic to the page exists, branded searches are up 20%, and prompt testing confirms ChatGPT cites the page consistently — it's gaining a different kind of visibility. *Layer three* shows those AI-referred visitors converting at twice the rate of average organic traffic. **Without the pyramid you'd have flagged this page as underperforming and shifted resources away. With it, it's one of your strongest AEO assets and the right move is to create more content like it.**
