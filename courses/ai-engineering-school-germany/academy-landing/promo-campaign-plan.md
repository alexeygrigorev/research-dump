# Promo campaign plan: which track converts better

**13 November 2026, revised the same day after two independent reviews ([Carbon](reviews/carbon-review.md), [Astra](reviews/astra-review.md)). A plan only.** No money has been spent, no ad account was created or changed, and no campaign exists. Nothing here starts without Alexey's explicit yes on the budget and the copy. Request: t3290u.

This plan replaces the channel budgets in the [earlier paid-ads plan](../oversubscribed/paid-ads-channel-plan.md) for the period up to mid-December. That plan was written to bring applications to one school. This one answers a narrower question first.

## The question

Two tracks are candidates for the first cohort in April 2027: **agentic engineering** and **AI engineering**. Each has a landing page on academy.datatalks.club with one action: leave an email to join that track's shortlist. The campaign sends comparable traffic to both and measures which one more people sign up for. It also builds the list of emails that the survey form did not collect.

| | |
|---|---|
| Primary measure, paid | First-choice signups per 1,000 ad impressions and per €100 spent, per channel. The two ads differ, so the click is already part of the answer: a track whose ad draws many people must not lose because its page then converts a smaller share of a bigger crowd. |
| Diagnostic, paid | Signup rate per landing page (signups divided by page views), per channel. It explains the primary measure (impressions, clicks, page views, signups) and is what the sample sizes below are computed on. |
| Primary measure, organic | Share of first-choice signups per track among people who arrived through the home page |
| First choice | One person counts once. Someone who joins both shortlists counts for the track they joined first, and "both" is reported as its own number. |
| Quality measure | Share of signups based in Germany and how they would pay (two optional one-tap questions after signup, plus the survey) |
| Not measured | Willingness to enrol. "An email signup is not a purchase" ([Kromatic](https://kromatic.com/real-startup-book/2-evaluative-market-experiments/value-proposition-test/landing-page-smoke-test/)). The application and the practical task measure that later. |

## Test design

1. **Two identical pages.** Same template, same funding, admission, instructor and FAQ blocks. Only the track content differs. A test in the site's CI enforces this.
2. **Paid traffic: one ad per track, same everything else.** For every channel the two ads share audience, budget, dates, format and layout. The headline of each ad is the headline of its page. Each ad links to its own landing page. This measures the offer from the first impression on.
3. **Organic traffic: one neutral link to the home page.** The home page shows both tracks side by side in random order, and the visitor picks one. The split of those choices is a second, independent reading of the same question, from people who already know Alexey.
4. **Fair delivery.** Ad platforms show each ad to a different mix of people, so a plain comparison of two ads mixes up the ad and the audience ([Braun and Schwartz, Journal of Marketing](https://www.ama.org/2025/01/07/can-you-trust-your-ad-data-a-new-study-exposes-a-hidden-flaw-in-a-b-testing-on-digital-ad-platforms/); [Burtch et al. 2025](https://arxiv.org/html/2508.21251v1)). To limit this:
   - Meta: use the A/B test tool, which splits the audience into random, non-overlapping halves with an even budget ([Jon Loomer](https://www.jonloomer.com/how-to-create-an-a-b-test-in-meta-experiments/)). Narrow, identical targeting. Exclude Audience Network: in one test 96–99% of cheap link clicks came from it ([Loomer](https://www.jonloomer.com/split-test-which-optimization-leads-to-the-most-high-quality-traffic/)).
   - Google Search: one keyword set, a custom experiment with a 50% split ([Google Ads Help](https://support.google.com/google-ads/answer/6261395?hl=en)), one arm per landing page.
   - Meta, further: the study above found that ads in properly split tests still reached different people when the campaign optimised for clicks. So use fixed manual placements (feed only, the same for both arms), and compare the age, gender and placement mix of the two arms on day 7 and day 14. If they differ clearly, say so next to the result.
   - Reddit: two ads in one ad group with even rotation. Its split-test tool reportedly needs about $1,000 a day, so it is not usable here. This is not a random split of people, so Reddit numbers are reported but do not enter the decision rule.
   - The same country targeting everywhere: Germany.
   - Results are read per channel and then combined with the same weight for both tracks. Raw totals across channels are not compared, because a track that happens to get more search clicks would look better for that reason alone.
   - Always read page conversion (our own numbers) next to ad click-through (the platform's numbers).
5. **Same measurement on both pages.** No pixels and no cookies (see [Tracking](#tracking)), so no consent banner removes part of the traffic on one page and not the other.

## How much traffic is enough

The sample sizes below are my own arithmetic: a two-sided test of two proportions with 80% power. "Visitors per page" means page views of one landing page.

| Signup rate, weaker track | Signup rate, stronger track | Ratio | Visitors per page, 95% confidence | Visitors per page, 90% confidence |
|---:|---:|---:|---:|---:|
| 2% | 4% | 2.0 | 1,138 | 896 |
| 2.5% | 5% | 2.0 | 903 | 711 |
| 3% | 6% | 2.0 | 746 | 587 |
| 3% | 4.5% | 1.5 | 2,514 | 1,980 |
| 4% | 8% | 2.0 | 552 | 435 |
| 4% | 7% | 1.75 | 905 | 713 |
| 4% | 6% | 1.5 | 1,863 | 1,467 |
| 5% | 10% | 2.0 | 434 | 342 |
| 5% | 7.5% | 1.5 | 1,470 | 1,158 |
| 8% | 12% | 1.5 | 882 | 694 |
| 10% | 15% | 1.5 | 686 | 540 |

For the home page, where visitors choose between the two tracks: 194 choices show a 60/40 split at 95% confidence, and 85 choices show a 65/35 split.

What this means:

- **A difference of 2 to 1 needs about 450 to 550 visitors per page if the pages convert at 4 to 5%, and about 600 to 900 if they convert at 2 to 3%**, which is what cold social traffic is planned at.
- **A difference of 1.5 to 1 needs about 1,200 to 2,000 visitors per page** from cold paid traffic, or about 700 to 900 if the pages convert at 8% or more, as warm traffic usually does.
- These numbers give an 80% chance of seeing a difference that really exists. One time in five a real difference of that size is still missed. And they assume one visit per person, while the site counts page loads (see [Tracking](#tracking)), so treat them as a lower bound.
- **A difference smaller than 1.5 to 1 is not worth buying.** If the two tracks are that close, demand does not decide, and the choice should rest on signup quality, the survey answers and which track Alexey can teach best first.

Expected signup rates used for planning (sources in the [landing page research](landing-page-research.md#3-benchmarks)): paid social 2–5%, paid search about 5% (the one German figure found is 4.8% for education), email and own community 8–14%.

## Budget

Three sizes. The recommendation is the middle one.

| | Lean | **Recommended** | Thorough |
|---|---:|---:|---:|
| Paid budget | €1,200 | **€2,500** | €5,000 |
| Of that, in the comparison (without LinkedIn) | €1,100 | **€2,300** | €4,600 |
| Expected page views per page, after losing about 20% of clicks before the page loads | 210–410 | **440–855** | 880–1,710 |
| Chance to see a true 2 to 1 difference (90% confidence, pages converting at 2.4% and 4.9%) | about 35–60% | **about 60–85%** | about 85–98% |
| Chance to see a true 1.5 to 1 difference | under 30% | **about 25–45%** | about 45–75% |
| Expected paid signups | 14–27 | **30–57** | 60–114 |
| Expected cost per signup | €40–80 | **€40–80** | €40–80 |
| Possible one-week extension (decision rule 4), only with a new yes from Alexey | +€600 | **+€1,250** | +€2,500 |

The page view ranges come from the cost-per-click ranges in the next table. The signup ranges assume 3% on Meta, 4.8% on Google Search and 2% on Reddit. These are forecasts, not promises: no published figure is specific to this offer.

**What the recommended size is:** a pilot that will probably show a large difference (2 to 1 or more) and will probably not show a moderate one. An unclear result is a legitimate outcome, and the decision rule says what happens then.

### Recommended split: €2,500

| Channel | Budget | Planning cost per click | Expected clicks | Role |
|---|---:|---:|---:|---|
| Meta (Instagram and Facebook feed, Reels) | €1,100 | €0.90–1.50 | 730–1,220 | Volume. Germany, people with software and data interests, English-language ads. A/B test tool, two arms. |
| Google Search | €900 | €1.50–3.50 | 260–600 | Intent. Track-neutral keywords around AI and software further training, alone and combined with Bildungsgutschein. Experiment with a 50% split. |
| Reddit | €300 | €0.95–2.80 | 107–316 | Technical audience in Germany (for example r/de_EDV, r/berlin, r/cscareerquestionsEU, r/LocalLLaMA, all with a Germany geo filter). Two ads, even rotation. Reported, but outside the decision rule: the volume is small and the split is not random. |
| LinkedIn | €200 | €4–5 | 40–50 | Not for the comparison: too few clicks. A quality check on the exact professional audience, by promoting Alexey's best organic post. |
| **Total** | **€2,500** | | **1,137–2,186** (1,097–2,136 in the comparison) | |

Where the planning costs come from: Meta in Germany about €0.91 per click ([Superads](https://www.superads.ai/facebook-ads-costs/cpc-cost-per-click/germany), modelled from one tool's data; the planning range is set above it); Google Search in Germany, education: €1.28 per click, 4.0% click-through, 4.8% conversion (agency estimate, *unverified method*, [Bravery](https://braverytechnology.com/de/google-ads-statistiken/); the planning range is set above it because Bildungsgutschein keywords are contested); Reddit $1.00–3.00 for technical and developer subreddits ([Benly](https://benly.ai/learn/reddit-ads/reddit-ads-cost-benchmarks), which also suggests $500 or more for a first test, so €300 buys only a rough reading); LinkedIn €4–5 in Europe ([Pettauer](https://pettauer.net/en/european-linkedin-ad-benchmarks-2025-2026/)). No published cost per click was found for "Bildungsgutschein" keywords. They are known to be contested by the large schools. Check Keyword Planner before fixing the search budget, and move search money to Meta if the bids are above €4.

The budget is inside the range of the earlier plan (€1,500 for stage 1) plus the conditional stage 2, and inside the caution in the [2026 expense plan](../2026-expense-plan.md): limited marketing with a specific objective. Ads that run in 2026 are services used in 2026.

### What it costs to get a meaningful result

- **€0** already gives a result if Alexey's own channels send about 400 choices through the home page: that shows a 57/43 split or stronger.
- **€1,200** will more likely miss than show a 2 to 1 difference on cold traffic. It is a tracking rehearsal with a small chance of an answer.
- **€2,500** shows a true 2 to 1 difference in about 60 to 85% of cases, depending on click prices, and a 1.5 to 1 difference in fewer than half. Together with organic traffic that points the same way, it is enough for the decision rule below.
- **€5,000** shows 2 to 1 almost always and 1.5 to 1 in about 45 to 75% of cases. I do not recommend spending this before the first €2,500 has been read: if the difference is large it is probably already visible, and if it is small more money will not make it matter.
- To see 1.5 to 1 reliably on cold traffic converting at 3%, about 2,000 page views per page are needed, which is €4,000 to €8,000 at the planned click prices.

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

Fourteen days covers two full weeks of weekday and weekend behaviour.

### Stage 2. Reading and decision, 7 to 11 December

Export signups and page views, fill the [result table](#result-table), apply the [decision rule](#decision-rule), write the result into the [decision log](../decision-log.md). Then one more post to the shortlists: which track runs, and when applications open.

Scaling paid spend to fill the cohort is a separate decision after the track is chosen. It follows the stage 2 rules of the [earlier plan](../oversubscribed/paid-ads-channel-plan.md#stage-2-scale-what-worked-late-december-to-january-budget-15003000-conditional).

## Ad copy

Drafts. Each pair is built the same way so that only the track differs. The page headlines are reused word for word.

### Meta and Reddit (image: the seat grid from the site, 15 outlined squares on dark green, with the track name and headline on the image)

| | Agentic engineering | AI engineering |
|---|---|---|
| Headline (short, so phones do not cut off the track) | Agentic Engineering: Coding Agents | AI Engineering: LLM Applications |
| Text | Agentic engineering: build, test and ship software with coding agents. A full-time, live program for people who already code. 15 seats, taught by Alexey Grigorev (DataTalks.Club). Berlin or online, planned for April 2027. Join the shortlist to get the application first. | AI engineering: build, evaluate and run applications on language models. A full-time, live program for people who already code. 15 seats, taught by Alexey Grigorev (DataTalks.Club). Berlin or online, planned for April 2027. Join the shortlist to get the application first. |
| Button | Learn more | Learn more |

Second creative for both (same split): a photo of Alexey teaching, with the track name and the line "15 seats. I teach every session myself." on the image. Without the track name on the image the two arms would look the same on Instagram, where the headline is often hidden.

### Google Search

Responsive search ads allow 30 characters per headline and 90 per description, and need at least two descriptions ([Google Ads Help](https://support.google.com/google-ads/answer/7684791?hl=en)). Same number of assets and the same pinning in both arms. Description 2 is pinned so the funding status always shows.

| | Agentic engineering | AI engineering |
|---|---|---|
| Headline 1 (pinned) | Agentic Engineering Program | AI Engineering Program |
| Headline 2 | 15 Seats, Live, April 2027 | 15 Seats, Live, April 2027 |
| Headline 3 | AI Training in English | AI Training in English |
| Description 1 | Build, test and ship software with coding agents. Full-time, live, Berlin or online. | Build, evaluate and run LLM applications. Full-time, live, Berlin or online. |
| Description 2 (pinned) | Bildungsgutschein funding planned, approval pending. Join the 15-seat shortlist. | Bildungsgutschein funding planned, approval pending. Join the 15-seat shortlist. |

Keyword themes (the same list for both arms of the experiment, and only searches that do not name one of the tracks): "KI Weiterbildung", "AI Weiterbildung Berlin", "AI bootcamp Berlin", "Weiterbildung Softwareentwicklung KI", "Bildungsgutschein KI Weiterbildung", "Bildungsgutschein Programmieren". Phrase and exact match. Germany only. "AI engineering course", "LLM course" and "coding agents course" are left out of the comparison because each matches one track's ad and page better than the other's. They can run in a separate small ad group to see search volume, outside the result table. The shared headline "AI Training in English" puts "AI" into both ads and tells German-keyword searchers the language before they click.

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
| Meta ad, agentic | `https://academy.datatalks.club/agentic-engineering/?utm_source=meta&utm_medium=paid-social&utm_campaign=track-test-2026-11&utm_content=agentic-seats` |
| Meta ad, AI | `https://academy.datatalks.club/ai-engineering/?utm_source=meta&utm_medium=paid-social&utm_campaign=track-test-2026-11&utm_content=ai-seats` |
| Google ad, agentic | `https://academy.datatalks.club/agentic-engineering/?utm_source=google&utm_medium=cpc&utm_campaign=track-test-2026-11&utm_content=agentic-rsa&utm_term={keyword}` |
| Google ad, AI | `https://academy.datatalks.club/ai-engineering/?utm_source=google&utm_medium=cpc&utm_campaign=track-test-2026-11&utm_content=ai-rsa&utm_term={keyword}` |
| Reddit ad, agentic / AI | same pattern with `utm_source=reddit&utm_medium=paid-social` and `utm_content=agentic-seats` / `ai-seats` |
| LinkedIn, promoted post | `https://academy.datatalks.club/?utm_source=linkedin&utm_medium=paid-social&utm_campaign=track-test-2026-11&utm_content=promoted` |

`utm_content` names the ad arm and the creative (`agentic-seats`, `ai-seats`, `agentic-alexey`, `ai-alexey`). Every paid link must carry it, for two reasons. The page view counter does not store `utm_medium`, so without it paid and organic LinkedIn would land in one counter. And the site keeps the link tags when a visitor moves to the other track's page, so the arm name is the only way to tell a visitor of the agentic ad who ended up on the AI page from a visitor of the AI ad.

## Tracking

- **Signups** are stored with the track, the time, the first link tags seen (`utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term`), the referring page and the two optional answers. Export: `python main/academy/scripts/export_signups.py` in aws-infra.
- **Page views** are counted on our own server as daily totals per page, source, campaign and creative. Export: `python main/academy/scripts/pageviews.py`. These are page loads, not unique people, because the site stores nothing on the visitor's device. Repeat visits inflate the denominator, and not necessarily the same for both pages. This is one reason the paid decision rests on signups per impression and per euro, which the ad platforms count per person, and the page rate is a diagnostic.
- **Ad platforms** report impressions, clicks and spend per ad. Clicks and our page views will not match exactly (bounces before the page loads, bots that the platform filters). Use platform clicks for cost and our page views for conversion.
- **No Meta Pixel, LinkedIn Insight Tag or GA4.** In Germany they need consent under § 25 TDDDG ([overview](https://datenschutz-generator.de/tdddg-cookies/)), and a consent banner would hide part of the traffic. The cost: the platforms cannot optimise for signups, only for link clicks or landing page views. That is acceptable for a two-week test of this size, which would not reach Meta's roughly 50 conversions per ad set per week anyway ([ppc.land](https://ppc.land/learning-phase/)). It matters if the campaign is later scaled; decide then whether to add consented conversion tracking.
- **One person, one choice.** The export has one row per email and track. Before reading results, group by email: agentic only, AI only, both (first choice by the earlier time). The decision uses first choices.
- **Signups are not confirmed addresses yet.** Until the confirmation email exists (see [site and pipeline](site-and-pipeline.md#open-points)), look at the list by hand before the decision and drop obvious junk and bursts from one source.
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

Fixed now, before any data exists. "Signups" means first-choice signups (one per person).

1. **A track wins** if all three hold:
   - On Meta and on Google Search, each read separately, it has more signups per €100 of spend than the other track.
   - Combined over Meta and Google with the same channel weights for both tracks, its signups per 1,000 impressions are at least 1.5 times the other's, and the difference in signup counts is significant at 90% (exact binomial test on the split of paid signups, given equal spend per arm).
   - The organic first choices through the home page point the same way.
2. **A lean, not a win.** If a track is ahead by at least 1.3 times in each of Meta, Google and organic, with at least 15 signups for the leading track in each, but rule 1 is not met: record it as a lean. A lean may break a tie in rule 3. It is not a result to announce.
3. **Otherwise the result is unclear.** That is not proof that the tracks are equal, only that this test could not separate them. Then choose by, in this order: the number of signups based in Germany (people who did not answer count as unknown, not as no); the survey answers, including full-time availability; a lean from rule 2; which track Alexey has more ready material and energy for.
4. **Minimum volume.** If either page has fewer than 400 paid page views by day 14, the test may be extended by one week at the same daily budget before applying rules 1 to 3. This costs up to €1,250 more (€3,750 in total) and needs a new explicit yes from Alexey. Do not extend more than once. The reading then moves to 14 to 18 December.
5. **Overall demand check, separate from the comparison.** If paid traffic brings fewer than 1.5 signups per 100 page views on both pages, the question is no longer which track, but whether the offer or its framing works. Review the page and the message before spending more.

## Before any spend

- [ ] academy.datatalks.club is live on its own domain, and a test signup with link tags arrives in the export.
- [ ] Impressum and privacy notice are live (they are part of the site).
- [ ] `http://academy.datatalks.club` redirects to `https://` (signups from the plain-http page are refused by the API).
- [ ] Alexey has approved the budget, the channels and the ad copy in writing.
- [ ] Ad accounts exist and billing works; Meta's special category prompt was checked. Meta placements are fixed to feed, the same in both arms.
- [ ] Every paid link carries its arm in `utm_content`.
- [ ] Ad previews checked on a phone: the track name is visible in every placement.
- [ ] Keyword Planner checked for the search keywords.
- [ ] The confirmation email (double opt-in) is sent right after signup, or at the latest is ready before the first mailing to the shortlist. Sending it right away is better: people still remember signing up, and unconfirmed addresses can be left out of the count.
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
