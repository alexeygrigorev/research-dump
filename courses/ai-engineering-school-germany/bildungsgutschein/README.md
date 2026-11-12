# Bildungsgutschein programme: course descriptions, syllabi and a price above €10,000

**Draft · 12 November 2026.** Nothing here has been submitted to a certifier (fachkundige Stelle, FKS), published as an offer or sent to anyone. Figures marked *(estimate)* are my own arithmetic. Figures with a link come from that source. Anything not confirmed is marked **unknown**.

| File | Content |
|---|---|
| [variante-a-agentic-engineering.md](variante-a-agentic-engineering.md) | Course description and syllabus, track **A. Agentic engineering** |
| [variante-b-ai-engineering.md](variante-b-ai-engineering.md) | Course description and syllabus, track **B. AI engineering** |
| [appendix.md](appendix.md) | Comparable approved courses above €10k (sources), AZAV checklist, open decisions |

## Where A and B come from

Variants A and B are the two tracks in question 1 of the survey, [materials/survey.en.md](../materials/survey.en.md), "What do you most want to learn?". The learning bullets and final projects in the variant files are copied from there. Programme facts used in both variants also come from the survey:

- an intensive, multi-month bootcamp with live instruction and hands-on projects
- first cohort April 2027, live online from Germany or in person in Berlin (Prenzlauer Berg, near S+U Schönhauser Allee)
- teaching in English
- both tracks assume some programming experience
- self-pay tuition €9,000–€10,000

The survey's pace question gives full-time as 12 teaching weeks, Monday to Friday 09:00–16:00, and part-time as 24 weeks, 09:00–12:30. The [teaching day](../schedule-and-capacity.md#proposed-teaching-day) turns that into 8 UE per day, 40 UE per week and 480 UE.

Content rule: every syllabus row uses survey topics plus Alexey's own material. That means LLM Zoomcamp, AI Engineering Buildcamp (Maven), Product Shipping with AI (Maven / [../../product-shipping](../../product-shipping)) and the earlier [curriculum options](../curriculum-options.md). Where a survey topic has no existing material, the row says **"material to write"**. All teaching is by Alexey, as the [README](../README.md) plans for the first iteration. No subcontractors.

## Price above €10,000: options

Rules, as already summarised in [economics.md](../economics.md#b-dks-references-not-an-automatic-maximum):

- BDKS 2026 (valid from 1 July 2026): **43414 Softwareentwicklung – Experte €15.46/UE**. Other IT lines in the [BA table](https://www.arbeitsagentur.de/datei/tabelle-der-kosten-fuer-massnahmen-der-beruflichen-weiterbildung-2024_ba049411.pdf) are similar: 43104 Informatik Experte €15.35, 43114 Wirtschaftsinformatik Experte €15.60, 43224 IT-Anwendungsberatung Experte €15.32. The highest IT line is 43154 Medieninformatik Experte at €15.98.
- Costs above BDKS need justification. More than 25% above also needs BA agreement ([§179 SGB III](https://www.gesetze-im-internet.de/sgb_3/__179.html), [§3 AZAV](https://www.gesetze-im-internet.de/azav/__3.html)).
- Calculation basis: 12 participants. The level has to follow the learning goal, not the higher rate (economics.md).

At 480 UE, €10,000 needs **€20.84/UE**, which is **34.8% above 43414**. A different occupation line cannot close that gap: the best IT line gives €7,670.40.

| # | UE | Weeks full-time / part-time | Line and rate | Price per participant | What it takes |
|---|---:|---|---|---:|---|
| 0 | 480 | 12 / 24 | 43414, €15.46 | €7,420.80 | Survey plan *(estimate)* |
| 1 | 480 | 12 / 24 | 43154, €15.98 | €7,670.40 | Wrong occupation for this content; does not reach €10k *(estimate)* |
| 2 | 480 | 12 / 24 | 43414 +25%, €19.33 | €9,276.00 | Justified special costs; still below €10k *(estimate)* |
| 3 | 480 | 12 / 24 | 43414 +34.8%, €20.84 | €10,003.20 | FKS **plus BA agreement**; high risk *(estimate)* |
| 4 | 560 | 14 / 28 | 43414 +25%, €19.33 | €10,822.00 | Justify the full 25% with costs *(estimate)* |
| **5** | **640** | **16 / 32** | **43414 +6.7%, €16.50** | **€10,560.00** | **Recommended.** Small, cost-based surcharge within the FKS's own authority *(estimate)* |
| 6 | 640 | 16 / 32 | 43414, €15.46 | €9,894.40 | Fallback if the surcharge is refused; just under €10k *(estimate)* |
| 7 | 680 | 17 / 34 | 43414, €15.46 | €10,512.80 | No surcharge, one more week *(estimate)* |
| 8 | 720 | 18 / 36 | 43414, €15.46 | €11,131.20 | No surcharge, six more weeks of solo teaching *(estimate)* |

### Recommendation: option 5

**640 UE, 16 teaching weeks full-time (40 UE/week, 09:00–16:00) or 32 weeks part-time (20 UE/week, 09:00–12:30). KldB 43414 at €16.50/UE (+6.7%). €10,560 per participant, about €126,720 per cohort at the 12-participant basis *(estimate)*.**

Why:

- **Real approved courses get above €10k through volume, not rate.** The comparables in the [appendix](appendix.md) run 720–1,050 UE at €13.86–€14.65/UE, all below €15.46.
- **The 4 extra weeks are needed for the survey's final projects, not added for price.** Track A's final project has to show people trying the app, improvements from their feedback, and how changes were tested and released. Track B's has to show where the assistant works, where it fails and how that was measured. The 12-week drafts in [curriculum-options.md](../curriculum-options.md) leave no time for a midterm feedback cycle or a measured second iteration. The 16-week syllabi add both. [economics.md](../economics.md) says: "More live hours should be justified by learning needs, never added solely to reach a desired funded price." The variant files give the reason week by week.
- **The +6.7% is a cost argument the FKS can approve alone.** Per participant, the provider has to cover LLM API, coding-agent and cloud usage. Product Shipping tells self-payers to budget US$20–500/month for this (see [maven.com/alexey-grigorev/product-shipping](https://maven.com/alexey-grigorev/product-shipping), FAQ). For Bildungsgutschein participants it belongs in the costing. For in-person cohorts, room rent adds to it. The amount per participant is **unknown** until quotes exist. If it does not hold up, option 7 (680 UE, 17 weeks, no surcharge) reaches €10,512.80.

### Costs of this choice

- Founder time: [economics.md](../economics.md#solo-cohort-illustration) estimates 38–41 h per teaching week. 16 weeks gives about 608–656 h instead of 456–492 h *(estimate)*.
- A 12 April start ends around late July instead of 6 July (holidays not counted) *(estimate)*.
- Part-time at 32 weeks is longer than six months, so holiday rules apply. Ask the FKS.
- The survey quotes self-pay €9,000–€10,000. Ask the FKS whether a higher approved voucher fee next to a lower self-pay price is a problem. **Unknown**: I found no rule on it.

### What the FKS would need

1. Curriculum with UE per module adding up to 640 (variant files), plus a written reason for the duration (above).
2. The occupation line, 43414, justified from the learning goal and the audience (programmers working at expert level).
3. A full costing at the 12-participant basis, with the per-participant LLM/agent/cloud costs and any room costs that justify €16.50/UE.
4. The rest of the evidence listed in [operations-and-azav.md](../operations-and-azav.md) and the [appendix checklist](appendix.md#azav-checklist-short).
