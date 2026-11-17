# Inbound Marketing Certification — course map and transcript sources

HubSpot Academy, portal 149750315, track `9147496`. Mapped 2026-11-17.
**24 videos across 8 content sections, 5h05m, plus a 3-hour exam.**

Transcripts are **per section, not per video** — one PDF covers all the
videos in a section. All seven content transcripts below have been extracted
and verified (70 pages, ~206,000 characters).

## Structure

| # | Section | Section ID | Videos | Time |
|---|---|---|---|---|
| 1 | Welcome to the Inbound Marketing Certification | — | 1 | 7 min |
| 2 | Inbound Marketing Fundamentals | 9253383 | 3 | 36 min |
| 3 | Getting to Know Your Customer | 9253377 | 2 | 31 min |
| 4 | Creating Content for the Buyer's Journey | 9253389 | 4 | 1 hr |
| 5 | Developing a Content Distribution Strategy | 9253395 | 4 | 44 min |
| 6 | Understanding Behavioral Marketing and Customer Segmentation | 9253407 | 3 | 32 min |
| 7 | Maximizing ROI With Marketing Attribution and Experimentation | 9253401 | 4 | 1 hr |
| 8 | Utilizing Marketing Automation and Artificial Intelligence | 9255843 | 3 | 35 min |
| 9 | Next Steps | 9255855 | — | 15 min |

Each section also carries: a knowledge check before, a short quiz after, a
study-group link, an optional "Explore HubSpot Tools" step, a slide deck, and
external resources (tools, articles, templates).

## Transcript URLs

Base: `https://f.hubspotusercontent20.net/hubfs/137828/_Academy%20Education%20-%20Learning%20Center%20Resources/`

| Key | Path after base | Size |
|---|---|---|
| `fundamentals` | `Academy_Certification%20Courses/Academy_Inbound%20Marketing%20Certification/Academy%20Lesson_Inbound%20Marketing%20Fundamentals/Transcripts/2022/Inbound%20Marketing%20Fundamentals%20Transcript.pdf` | 16p |
| `customer` | `Academy_Standalone%20Lessons/IMC%20-%20Getting%20to%20Know%20Your%20Customer/Getting%20to%20Know%20Your%20Customer%20transcript.pdf` | 7p |
| `buyers-journey` | `Academy_Certification%20Courses/Academy_Inbound%20Marketing%20Certification/Academy%20Lesson_Creating%20Content%20for%20the%20Buyers%20Journey/Transcript_Creating_Content_for_the_Buyers_Journey.pdf` | 11p |
| `distribution` | `Academy_Certification%20Courses/Academy_Inbound%20Marketing%20Certification/Academy%20Lesson_Developing%20a%20Content%20Distribution%20Strategy/Transcript_Developing%20a%20Content%20Distribution%20Strategy.pdf` | 9p |
| `attribution` | `Academy_Certification%20Courses/Academy_Inbound%20Marketing%20Certification/Academy%20Lesson_Inbound%20Marketing%20Fundamentals/Transcripts/2022/Maximizing%20ROI%20With%20Marketing%20Attribution%20and%20Experimentation%20Transcript.pdf` | 18p |
| `behavioral` | `Academy_Certification%20Courses/Academy_Inbound%20Marketing%20Certification/Academy%20Lesson_Understanding%20Behavioral%20Marketing%20and%20Customer%20Segmentation/Transcripts/Transcript_Understanding_Behavioral_Marketing_and_Customer_Segmentation.pdf` | 12p |
| `automation-ai` | `Academy_Certification%20Courses/Academy_Inbound%20Marketing%20Certification/Academy%20Lesson_Utilizing%20Marketing%20Automation%20and%20Artificial%20Intelligence/Transcripts/Transcript_Utilizing_Marketing_Automation_and_Artificial_Intelligence.pdf` | 13p |

Certification study guide (S3, **CORS-restricted to HubSpot origins** — not
fetchable from dividendit.com):
`https://hubspot-academy.s3.amazonaws.com/prod/tracks/study-guides/1028124-en-1642518845895.pdf`

## Extraction method

The container cannot reach these hosts (proxy 403). Extraction runs in the
browser:

1. `app-eu1.hubspot.com` has a CSP that blocks cdnjs, so pdf.js cannot load there.
2. `f.hubspotusercontent20.net` **does** allow CORS from `dividendit.com`.
3. So: open a tab on `dividendit.com`, load pdf.js 3.11.174 from cdnjs, `fetch()`
   each transcript, extract per-page text, and read it out via a `<pre>` dump
   plus `get_page_text` (`javascript_tool` truncates around 1,000 chars).

## Concept frequency across all seven transcripts

Counted, not estimated — this is what the certification actually emphasises.

| Concept | customer | buyers-journey | distribution | attribution | behavioral | automation-ai | fundamentals | **total** |
|---|---|---|---|---|---|---|---|---|
| **persona** | 50 | 18 | 9 | 2 | 11 | 13 | 22 | **125** |
| hero | — | — | — | 1\* | — | — | 5 | 6 |
| voice | 1\*\* | — | — | — | — | — | 3 | 4 |
| tone | — | — | 1\*\*\* | — | — | 3 | 2 | 6 |
| consistency | — | — | 1 | 1 | — | 3 | 2 | 7 |
| **third/first/second person** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| **point of view** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |

\* "hero section" of a web page, in an A/B testing example — unrelated.
\*\* "voicemail" — unrelated.
\*\*\* "sets the tone of your strategy" — unrelated to voice and tone.

**Conclusion: the certification never teaches grammatical person.** Its
consistency doctrine is about **buyer personas** (125 mentions, in every
section) and, secondarily, **brand voice and tone** — and all the genuine
brand-voice teaching sits in Fundamentals, in the ASOS and JetBlue examples.

The **hero narrative appears only in Fundamentals video 1**, as the framing
device for the whole methodology: the customer is the hero, the marketer is
the sage who guides them. It is opened and closed in that one video and is
not carried through the rest of the course.
