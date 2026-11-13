# Bildungsgutschein programme: research, course descriptions and syllabi

**12 November 2026.** Nothing here has been submitted to a certifier (fachkundige Stelle, FKS), published as an offer or sent to anyone. *(computed)* marks my own arithmetic. **Unknown** marks what no source settled.

| File | Content |
|---|---|
| [research.md](research.md) | Sources and findings: Alexey's own material, comparable programmes in Germany and abroad, what practitioners write, how to plan a curriculum, price and duration |
| [variante-a-agentic-engineering.md](variante-a-agentic-engineering.md) | Course description and syllabus, track **A. Agentic engineering** |
| [variante-b-ai-engineering.md](variante-b-ai-engineering.md) | Course description and syllabus, track **B. AI engineering** |
| [research-notes/](research-notes/) | Detailed source catalogues behind research.md, one entry per source with URL and fetch status |

## What replaced what

This set replaces the first draft from commit `e1cbab0`.

- `variante-a-agentic-engineering.md` and `variante-b-ai-engineering.md` were rewritten in place. The first draft of variant A left out the AI Dev Tools Zoomcamp and the Substack articles; the new one is built on them. On 13 November 2026, `variante-b-ai-engineering.md` was rebased on the refreshed **AI Engineering Field Guide** (`alexeygrigorev/ai-engineering-field-guide`, commit `ab21b128`, 9,760 job postings Feb–Nov 2026).
- `appendix.md` was deleted. Its comparables table moved into [research.md](research.md#72-courses-priced-at-12000-or-more) with more programmes, and its checklist and open decisions are below.
- This README replaces the earlier pricing README. The pricing analysis was kept and extended in [research.md](research.md#7-price-and-duration), with two corrections: the highest rate an FKS can approve alone is €19.32, not €19.33, and the note about holiday rules for courses over six months could not be verified.
- The 12-week drafts in [../curriculum-options.md](../curriculum-options.md) are older and are kept only as history.

## Where A and B come from

The two tracks are question 1 of the survey, [../materials/survey.en.md](../materials/survey.en.md). The learning goals and final projects in the variant files are the survey's wording. Programme facts also come from the survey: live teaching, first cohort April 2027, online from Germany or in Berlin, English, some programming experience assumed.

| | A. Agentic engineering | B. AI engineering |
|---|---|---|
| Alexey's definition | "agents help you build the product" | "AI is part of the product" |
| Based on | AI Dev Tools Zoomcamp and his Substack articles | LLM Zoomcamp, AI Engineering Buildcamp, and the AI Engineering Field Guide (`ab21b128`, 9,760 jobs) |
| Audience | Developers who write code and have tried AI only a little | Developers and technical professionals who program, preferably in Python |
| Starts with | Overview of the tools and setup, as in the first AI Dev Tools cohort | A Python service on an LLM API |
| Base tool | Claude Code | Python, LangChain + LangGraph (with PydanticAI compared) |
| Final project | A web application shipped to real users, improved from their feedback | A deployed enterprise/operational assistant with measured strengths and failures |

All teaching is by Alexey. No subcontractors.

## Price and duration in short

Full analysis with sources: [research.md](research.md#7-price-and-duration).

- The Agentur für Arbeit has no absolute cap. The reference rate for this course is **€15.46 per UE** (occupation line 43414, software development, expert level, table valid from 1 July 2026).
- An FKS can approve up to 25% more on its own, so up to **€19.32**, but only for named and evidenced special costs. Above that the BA has to consent.
- The premium programmes found (€12,000–14,658) reach their price through length: 22–30 weeks at €13.50–14.40 per UE. No premium surcharge and no rate above €19 was found. No course of 16 weeks or less at €12,000 or more could be verified.
- **Minimum duration without BA consent: 16 weeks (640 UE) for €12,000, 17 weeks (680 UE) for €13,000,** both at the full 25% surcharge.

Both syllabi are therefore a **16-week core of 640 UE** with four defined extension weeks:

| Version | UE | Weeks | Rate | Price per participant *(computed)* | Risk |
|---|---:|---:|---|---:|---|
| Core at the ceiling | 640 | 16 | €19.32 | €12,364.80 | Best case; no verified precedent |
| Core + 1 week | 680 | 17 | €19.32 | €13,137.60 | Same |
| Core + 2 weeks | 720 | 18 | €17.00 | €12,240.00 | Moderate |
| Core + 4 weeks | 800 | 20 | €15.46 | €12,368.00 | Lowest; how comparables price |
| Core, no surcharge | 640 | 16 | €15.46 | €9,894.40 | Fallback |

My recommendation: take the 16-week concept and a real costing to an FKS, and let the surcharge it accepts decide the version. On the evidence, 18–20 weeks is the likely outcome for €12,000. The surcharge has to rest on costs the rules recognise: a justified group below 12, per-participant agent, LLM and cloud usage, and an expert-level teacher. Those amounts are **unknown** until there are quotes.

Costs of a longer version: about 38–41 founder hours per teaching week ([../economics.md](../economics.md#solo-cohort-illustration)), so 20 weeks is roughly 760–820 hours *(computed)*. A 12 April start ends on 30 July at 16 weeks and on 27 August at 20 weeks if no week is lost to holidays or breaks *(computed)*.

## How the syllabi stay current

Both variant files separate a stable core from fast-moving tools. Outcomes are worded without tool names. Tools and versions sit in a dated annex that is reviewed before every cohort, and two late modules hold 4 UE each for what changed. Rules, triggers and change classes: [research.md](research.md#8-staying-current-what-is-stable-and-what-moves).

## AZAV checklist

Full analysis: [../operations-and-azav.md](../operations-and-azav.md).

| Requirement | Status |
|---|---|
| Provider approval including a quality-management system | Missing |
| Course approval | Missing; the variant files are the starting point for the concept |
| Course concept: goal, target group, content | Drafted for A and B in English; a formal German concept is needed |
| Entry requirements and how they are tested | Proposed: practical exercise and documented conversation; the exercise still has to be written |
| UE per module and a reason for the duration | Drafted; each extension week has its own reason |
| Measurable outcomes per module | Drafted |
| Teaching concept: live delivery, interaction in project blocks, attendance | Weekly structure drafted; full concept missing |
| Learning checks and documentation | Assessment forms drafted; rubrics missing |
| Certificate | Missing |
| Teacher qualification and absence cover | Alexey only; illness cover needed |
| Absence policy and learner support | Missing |
| Labour-market need | Bitkom data in [research.md](research.md#3-comparable-programmes-in-germany); BA data in [../research.md](../research.md) |
| Cost calculation | Options above; full costing missing |
| Rooms, equipment, platform, data protection | Berlin room terms pending |
| Distance-learning classification of the online format | Open, see operations-and-azav.md |

## Open decisions

1. Which track goes first (survey, interviews and pilot, per the [project README](../README.md)).
2. Which version to submit: 16, 17, 18 or 20 weeks. This follows from the FKS answers listed in [research.md](research.md#74-what-this-means-for-the-plan).
3. The certified group size (8 to 12) and the costing that supports a surcharge.
4. Founder capacity for 16 to 20 teaching weeks, and illness cover.
5. Whether replacing a tool under an unchanged outcome has to be reported to the FKS. No source settles it.
6. The survey quotes self-pay tuition of €9,000–10,000. Whether a higher approved fee next to a lower self-pay price is a problem is **unknown**; ask the FKS.
7. Material to write: listed at the end of each variant file.
