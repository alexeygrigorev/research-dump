# Promo campaign plan: which track converts better

**13 November 2026. A plan only.** No money has been spent, no ad account was created or changed, and no campaign exists. Nothing here starts without Alexey's explicit yes on the budget and the copy. Request: t3290u.

This plan replaces the channel budgets in the [earlier paid-ads plan](../oversubscribed/paid-ads-channel-plan.md) for the period up to mid-December. That plan was written to bring applications to one school. This one answers a narrower question first.

## The question

Two tracks are candidates for the first cohort in April 2027: **agentic engineering** and **AI engineering**. Each has a landing page on academy.datatalks.club with one action: leave an email to join that track's shortlist. The campaign sends comparable traffic to both and measures which one more people sign up for. It also builds the list of emails that the survey form did not collect.

| | |
|---|---|
| Primary measure | Signup rate per landing page: shortlist signups divided by page views, per traffic source |
| Second measure | Signups per 1,000 ad impressions (ad click-through times page conversion), because the offer starts in the ad |
| Quality measure | Share of signups based in Germany and how they would pay (two optional one-tap questions after signup, plus the survey) |
| Not measured | Willingness to enrol. "An email signup is not a purchase" ([Kromatic](https://kromatic.com/real-startup-book/2-evaluative-market-experiments/value-proposition-test/landing-page-smoke-test/)). The application and the practical task measure that later. |

## Test design

1. **Two identical pages.** Same template, same funding, admission, instructor and FAQ blocks. Only the track content differs. A test in the site's CI enforces this.
2. **Paid traffic: one ad per track, same everything else.** For every channel the two ads share audience, budget, dates, format and layout. The headline of each ad is the headline of its page. Each ad links to its own landing page. This measures the offer from the first impression on.
3. **Organic traffic: one neutral link to the home page.** The home page shows both tracks side by side in random order, and the visitor picks one. The split of those choices is a second, independent reading of the same question, from people who already know Alexey.
4. **Fair delivery.** Ad platforms show each ad to a different mix of people, so a plain comparison of two ads mixes up the ad and the audience ([Braun and Schwartz, Journal of Marketing](https://www.ama.org/2025/01/07/can-you-trust-your-ad-data-a-new-study-exposes-a-hidden-flaw-in-a-b-testing-on-digital-ad-platforms/); [Burtch et al. 2025](https://arxiv.org/html/2508.21251v1)). To limit this:
   - Meta: use the A/B test tool, which splits the audience into random, non-overlapping halves with an even budget ([Jon Loomer](https://www.jonloomer.com/how-to-create-an-a-b-test-in-meta-experiments/)). Narrow, identical targeting. Exclude Audience Network: in one test 96–99% of cheap link clicks came from it ([Loomer](https://www.jonloomer.com/split-test-which-optimization-leads-to-the-most-high-quality-traffic/)).
   - Google Search: one keyword set, a custom experiment with a 50% split ([Google Ads Help](https://support.google.com/google-ads/answer/6261395?hl=en)), one arm per landing page.
   - Reddit: two ads in one ad group with even rotation. Its split-test tool reportedly needs about $1,000 a day, so it is not usable here.
   - Always read page conversion (our own numbers) next to ad click-through (the platform's numbers).
5. **Same measurement on both pages.** No pixels and no cookies (see [Tracking](#tracking)), so no consent banner removes part of the traffic on one page and not the other.

## How much traffic is enough

The sample sizes below are my own arithmetic: a two-sided test of two proportions with 80% power. "Visitors per page" means page views of one landing page.

| Signup rate, weaker track | Signup rate, stronger track | Ratio | Visitors per page, 95% confidence | Visitors per page, 90% confidence |
|---:|---:|---:|---:|---:|
| 4% | 8% | 2.0 | 552 | 435 |
| 4% | 7% | 1.75 | 905 | 713 |
| 4% | 6% | 1.5 | 1,863 | 1,467 |
| 5% | 10% | 2.0 | 434 | 342 |
| 5% | 7.5% | 1.5 | 1,470 | 1,158 |
| 8% | 12% | 1.5 | 882 | 694 |
| 10% | 15% | 1.5 | 686 | 540 |

For the home page, where visitors choose between the two tracks: 194 choices show a 60/40 split at 95% confidence, and 85 choices show a 65/35 split.

What this means:

- **A difference of 2 to 1 is cheap to see**: about 450 to 550 visitors per page.
- **A difference of 1.5 to 1 needs about 1,200 to 1,900 visitors per page** from cold paid traffic, or about 700 to 900 if the pages convert at 8% or more, as warm and search traffic usually does.
- **A difference smaller than 1.5 to 1 is not worth buying.** If the two tracks are that close, demand does not decide, and the choice should rest on signup quality, the survey answers and which track Alexey can teach best first.

Expected signup rates used for planning (sources in the [landing page research](landing-page-research.md#3-benchmarks)): paid social 2–5%, paid search 5–8%, email and own community 8–14%.

## Budget

Three sizes. The recommendation is the middle one.

| | Lean | **Recommended** | Thorough |
|---|---:|---:|---:|
| Paid budget | €1,200 | **€2,500** | €5,000 |
| Expected paid visitors, both pages together | 570–1,200 | **1,200–2,500** | 2,400–5,000 |
| Per page | 285–600 | **600–1,250** | 1,200–2,500 |
| Smallest difference it can show on paid traffic alone | 2 to 1, and only if clicks are cheap | **2 to 1 for certain; about 1.6 to 1 if clicks are cheap** | 1.5 to 1 |
| Expected paid signups | 20–42 | **42–88** | 85–175 |
| Expected cost per signup | €28–60 | **€28–60** | €28–60 |

The visitor ranges come from the cost-per-click ranges in the next table. The signup ranges assume 3% on Meta, 6.5% on Google Search and 2% on Reddit, which is below the published medians on purpose.

### Recommended split: €2,500

| Channel | Budget | Planning cost per click | Expected clicks | Role |
|---|---:|---:|---:|---|
| Meta (Instagram and Facebook feed, Reels) | €1,100 | €0.90–1.50 | 730–1,220 | Volume. Germany, people with software and data interests, English-language ads. A/B test tool, two arms. |
| Google Search | €900 | €1.50–3.50 | 260–600 | Intent. Keywords around AI and software further training, coding agents, LLM courses, and Bildungsgutschein combined with those. Experiment with a 50% split. |
| Reddit | €300 | €0.50–2.00 | 150–600 | Technical audience in Germany and Europe (for example r/de_EDV, r/berlin, r/cscareerquestionsEU, r/LocalLLaMA with a Germany geo filter). Two ads, even rotation. |
| LinkedIn | €200 | €4–5 | 40–50 | Not for the comparison: too few clicks. A quality check on the exact professional audience, by promoting Alexey's best organic post. |
| **Total** | **€2,500** | | **1,180–2,470** | |

Where the planning costs come from: Meta in Germany about €0.91 per click and €14.80 CPM ([Superads](https://www.superads.ai/facebook-ads-costs/cpc-cost-per-click/germany), modelled from one tool's data); Google Search in Germany €1.32 on average and €1.00–4.00 for further education (agency estimate, *unverified method*, [Bravery](https://braverytechnology.com/de/google-ads-statistiken/)); Reddit $0.50–2 ([Benly](https://benly.ai/learn/reddit-ads/reddit-ads-cost-benchmarks)); LinkedIn €4–5 in Europe ([Pettauer](https://pettauer.net/en/european-linkedin-ad-benchmarks-2025-2026/)). No published cost per click was found for "Bildungsgutschein" keywords. They are known to be contested by the large schools. Check Keyword Planner before fixing the search budget, and move search money to Meta if the bids are above €4.

The budget is inside the range of the earlier plan (€1,500 for stage 1) plus the conditional stage 2, and inside the caution in the [2026 expense plan](../2026-expense-plan.md): limited marketing with a specific objective. Ads that run in 2026 are services used in 2026.

### What it costs to get a meaningful result

- **€0** already gives a result if Alexey's own channels send about 400 choices through the home page: that shows a 57/43 split or stronger.
- **€1,200** shows a 2 to 1 difference on cold traffic if clicks are cheap, and nothing smaller.
- **€2,500** shows a 2 to 1 difference for certain and about 1.6 to 1 at the cheap end of the click prices. Together with organic traffic that points the same way, it is enough for the decision rule below.
- **€5,000** shows 1.5 to 1 on cold traffic alone. I do not recommend spending this before the first €2,500 has been read: if the difference is large it is already visible, and if it is small more money will not make it matter.

## Channels and the order of work

### Stage 0. Organic, 16 to 22 November. €0

All links go to the **home page** with the tags from the [link table](#links). The home page records which track each visitor opens and which shortlist they join.

| Channel | What | Who |
|---|---|---|
| LinkedIn | A follow-up to the 13 November post: "The two tracks now have their own pages. Fifteen seats. Pick one." | Alexey |
| X, Bluesky, Threads | Short version of the same | Alexey |
| DataTalks.Club newsletter | One block near the top | Alexey or the newsletter owner |
| Telegram channel, Slack #announcements | Short post | Alexey |
| YouTube | Pinned comment and description line under the most-watched agent and LLM videos; a mention in the next live stream | Alexey |
| The survey form | Add the academy link to the form's thank-you message, and make the email question required (see [site and pipeline](site-and-pipeline.md#the-existing-survey-form)) | Alexey |
| People who already answered the survey | They left no email, so they can only be reached by reposting in the same channels | |

Purpose: check that tracking works end to end, get a first conversion rate for each page, and get the first few hundred choices. Do not start paid traffic before this has run for three days without a tracking problem.

### Stage 1. Paid test, 23 November to 6 December (14 days). €2,500

- Day 0 (Friday 20 November): Alexey approves budget and copy. Ad accounts and billing checked. Keyword Planner checked.
- Days 1 to 14: all four channels run at an even daily budget. No changes to the pages, the ads or the targeting during the test, except to stop an ad that breaks a platform rule.
- Day 7: a health check only (tracking, delivery, spend split between the arms). No decision.
- Day 14: stop everything.

Fourteen days is the minimum for LinkedIn's A/B test and covers two full weeks of weekday and weekend behaviour.

### Stage 2. Reading and decision, 7 to 11 December

Export signups and page views, fill the [result table](#result-table), apply the [decision rule](#decision-rule), write the result into the [decision log](../decision-log.md). Then one more post to the shortlists: which track runs, and when applications open.

Scaling paid spend to fill the cohort is a separate decision after the track is chosen. It follows the stage 2 rules of the [earlier plan](../oversubscribed/paid-ads-channel-plan.md#stage-2-scale-what-worked-late-december-to-january-budget-15003000-conditional).

## Ad copy

Drafts. Each pair is built the same way so that only the track differs. The page headlines are reused word for word.

### Meta and Reddit (image: the seat grid from the site, 15 outlined squares on dark green, with the headline)

| | Agentic engineering | AI engineering |
|---|---|---|
| Headline | Build, test and ship software with coding agents | Build, evaluate and run applications on language models |
| Text | A full-time, live program for people who already code. 15 seats, taught by Alexey Grigorev (DataTalks.Club). Berlin or online, from April 2027. Join the shortlist to get the application first. | A full-time, live program for people who already code. 15 seats, taught by Alexey Grigorev (DataTalks.Club). Berlin or online, from April 2027. Join the shortlist to get the application first. |
| Button | Learn more | Learn more |

Second creative for both (same split): a photo of Alexey teaching, with the line "15 seats. I teach every session myself."

### Google Search

| | Agentic engineering | AI engineering |
|---|---|---|
| Headline 1 | Agentic Engineering Program | AI Engineering Program |
| Headline 2 | 15 Seats, Live, April 2027 | 15 Seats, Live, April 2027 |
| Headline 3 | Taught by Alexey Grigorev | Taught by Alexey Grigorev |
| Description | Build, test and ship software with coding agents. Full-time, Berlin or online. Bildungsgutschein funding planned, approval pending. Join the shortlist. | Build, evaluate and run LLM applications. Full-time, Berlin or online. Bildungsgutschein funding planned, approval pending. Join the shortlist. |

Keyword themes (the same list for both arms of the experiment): "KI Weiterbildung", "AI Weiterbildung Berlin", "AI engineering course", "AI bootcamp Berlin", "Weiterbildung Softwareentwicklung KI", "coding agents course", "LLM course", "Bildungsgutschein KI Weiterbildung", "Bildungsgutschein Programmieren". Phrase and exact match. Germany only.

### LinkedIn

Promote the organic post from stage 0. No separate copy.

### Rules for all copy

- No "free", "kostenlos" or "100% funded". The approval is pending.
- No "only X seats left", no countdowns. "15 seats" is the claim.
- Do not address or imply the reader's situation ("Unemployed?", "Lost your job?"). Meta's personal attributes policy forbids asserting or implying personal attributes, with financial status as its own example ([Meta](https://transparency.meta.com/policies/ad-standards/objectionable-content/privacy-violations-personal-attributes/)).
- Meta's Special Ad Category for employment applies in parts of Europe and includes professional certification programs ([Meta ad standards](https://transparency.meta.com/policies/ad-standards/), [Jon Loomer](https://www.jonloomer.com/special-ad-categories-meta-ads/)). Whether a program like this one in Germany falls under it is not settled by any text I found. Check the prompt in Ads Manager when creating the campaign. If the category applies, age and gender targeting and lookalikes are unavailable, which does not hurt this test.
- Keyword ads may target "Bildungsgutschein". The ad text must then say that approval is pending.

## Links

Use these exact links so the source is recorded with every signup and page view. `utm_campaign` is `track-test-2026-11` everywhere.

| Channel | Link |
|---|---|
| LinkedIn, organic | `https://academy.datatalks.club/?utm_source=linkedin&utm_medium=organic&utm_campaign=track-test-2026-11` |
| X | `https://academy.datatalks.club/?utm_source=x&utm_medium=organic&utm_campaign=track-test-2026-11` |
| Newsletter | `https://academy.datatalks.club/?utm_source=newsletter&utm_medium=email&utm_campaign=track-test-2026-11` |
| Telegram | `https://academy.datatalks.club/?utm_source=telegram&utm_medium=community&utm_campaign=track-test-2026-11` |
| Slack | `https://academy.datatalks.club/?utm_source=slack&utm_medium=community&utm_campaign=track-test-2026-11` |
| YouTube | `https://academy.datatalks.club/?utm_source=youtube&utm_medium=organic&utm_campaign=track-test-2026-11` |
| Meta ad, agentic | `https://academy.datatalks.club/agentic-engineering/?utm_source=meta&utm_medium=paid-social&utm_campaign=track-test-2026-11&utm_content=seats` |
| Meta ad, AI | `https://academy.datatalks.club/ai-engineering/?utm_source=meta&utm_medium=paid-social&utm_campaign=track-test-2026-11&utm_content=seats` |
| Google ad, agentic | `https://academy.datatalks.club/agentic-engineering/?utm_source=google&utm_medium=cpc&utm_campaign=track-test-2026-11&utm_term={keyword}` |
| Google ad, AI | `https://academy.datatalks.club/ai-engineering/?utm_source=google&utm_medium=cpc&utm_campaign=track-test-2026-11&utm_term={keyword}` |
| Reddit ad, agentic / AI | same pattern with `utm_source=reddit&utm_medium=paid-social` |
| LinkedIn, promoted post | `https://academy.datatalks.club/?utm_source=linkedin&utm_medium=paid-social&utm_campaign=track-test-2026-11` |

`utm_content` names the creative (`seats`, `alexey`).

## Tracking

- **Signups** are stored with the track, the time, the first link tags seen (`utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term`), the referring page and the two optional answers. Export: `python main/academy/scripts/export_signups.py` in aws-infra.
- **Page views** are counted on our own server as daily totals per page, source, campaign and creative. Export: `python main/academy/scripts/pageviews.py`. These are page loads, not unique people, because the site stores nothing on the visitor's device. Repeat visits inflate the denominator of both pages alike.
- **Ad platforms** report impressions, clicks and spend per ad. Clicks and our page views will not match exactly (bounces before the page loads, bots that the platform filters). Use platform clicks for cost and our page views for conversion.
- **No Meta Pixel, LinkedIn Insight Tag or GA4.** In Germany they need consent under § 25 TDDDG ([overview](https://datenschutz-generator.de/tdddg-cookies/)), and a consent banner would hide part of the traffic. The cost: the platforms cannot optimise for signups, only for link clicks or landing page views. That is acceptable for a two-week test of this size, which would not reach Meta's roughly 50 conversions per ad set per week anyway ([ppc.land](https://ppc.land/learning-phase/)). It matters if the campaign is later scaled; decide then whether to add consented conversion tracking.
- Test signups (addresses at `example.com` or containing `+academytest`) are flagged and left out of exports by default.

## Result table

To be filled on 7 December. One block per source group (cold paid, organic).

| Source | Page | Ad impressions | Ad clicks | Spend | Page views | Signups | Signup rate | Signups in Germany |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Meta | Agentic | | | | | | | |
| Meta | AI | | | | | | | |
| Google | Agentic | | | | | | | |
| Google | AI | | | | | | | |
| Reddit | Agentic | | | | | | | |
| Reddit | AI | | | | | | | |
| Organic, via home page | Agentic | n/a | n/a | n/a | | | | |
| Organic, via home page | AI | n/a | n/a | n/a | | | | |

## Decision rule

Fixed now, before any data exists.

1. **A track wins** if, on the cold paid traffic of all channels together, its signup rate is at least 1.5 times the other's and the difference is significant at 90% (two-proportion test), **and** the organic choices on the home page point the same way.
2. **A track wins on a weaker signal** if its signup rate is at least 1.3 times the other's in every one of Meta, Google and the organic traffic, even if no single comparison is significant.
3. **Otherwise there is no demand difference worth acting on.** Then choose by, in this order: the number of signups based in Germany who could attend full-time; the survey answers; which track Alexey has more ready material and energy for.
4. **Minimum volume.** If either page has fewer than 400 paid page views by day 14, extend by one week at the same daily budget before applying rules 1 to 3. Do not extend more than once.
5. **Overall demand check, separate from the comparison.** If both pages together bring fewer than 60 signups from all sources, the question is no longer which track, but whether the offer or its framing works. Review the page and the message before spending more.

## Before any spend

- [ ] academy.datatalks.club is live on its own domain, and a test signup with link tags arrives in the export.
- [ ] Impressum and privacy notice are live (they are part of the site).
- [ ] Alexey has approved the budget, the channels and the ad copy in writing.
- [ ] Ad accounts exist and billing works; Meta's special category prompt was checked.
- [ ] Keyword Planner checked for the search keywords.
- [ ] The confirmation email (double opt-in) is ready before the first mailing to the shortlist.
- [ ] The seat number and the start month on the page still match the plan.

## Sources for the cost and policy figures

| Topic | Figure | Source |
|---|---|---|
| Google Search, all industries, United States | Cost per click $5.42, click-through 6.64%, conversion 8.18% (April 2025 to March 2026) | [WordStream 2026](https://www.wordstream.com/blog/2026-google-ads-benchmarks) |
| Meta lead campaigns, United States | Click-through 2.59%, conversion 7.72%, cost per lead $27.66 (2025) | [LocaliQ](https://localiq.com/blog/facebook-advertising-benchmarks/) |
| LinkedIn | CPM about €74 in Western Europe; click-through 0.44–0.65%; minimum $10 a day | [Searchlab](https://searchlab.nl/statistieken/linkedin-ads-statistieken-2026), [LinkedIn](https://business.linkedin.com/advertise.html) |
| LinkedIn A/B test | Minimum two weeks; "some members might appear in both" | [LinkedIn Help](https://www.linkedin.com/help/lms/answer/a1376579) |
| Reddit | Minimum $5 a day; CPM $3–6 | [Stackmatix](https://www.stackmatix.com/blog/reddit-ads-cost) |
| Email click rate | 2.09% average, 3.02% education and training | [MailerLite](https://www.mailerlite.com/blog/email-marketing-benchmarks), [Mailchimp](https://mailchimp.com/en/resources/email-marketing-benchmarks/) |
| Smoke test precedents | Tim Ferriss tested book titles with search ads for under $200 in a week and judged by click-through; Buffer's two-page test brought about 100 signups in a month | [Boing Boing](https://boingboing.net/2010/10/25/howto-use-google-adw.html), [The Launcher](https://thelauncher.substack.com/p/from-0-to-paying-customers-the-two) |

Almost none of the published benchmarks are specific to Germany. The planning figures above are assumptions to be replaced by the first three days of real data.
