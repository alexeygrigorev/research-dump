# academy.datatalks.club: landing pages and the track test

**13 November 2026.** Alexey's request (t3290u): put landing pages for the two candidate tracks on academy.datatalks.club, collect emails (the survey form collected none), research what makes course pages convert and build on that, and prepare a campaign that shows which track people want more, with channels and a budget. No money has been spent.

| File | Content |
|---|---|
| [landing-page-research.md](landing-page-research.md) | Ten course and program pages examined, 23 findings with sources and what the site does with each, conversion benchmarks, legal notes for Germany |
| [site-and-pipeline.md](site-and-pipeline.md) | How the site and the signup storage are built, how they connect to the existing survey form, how to export the data, open points |
| [promo-campaign-plan.md](promo-campaign-plan.md) | Test design, how much traffic is enough, three budget sizes (recommended: €2,500), channels, dates, ad copy, links, tracking, the decision rule |
| [reviews/carbon-review.md](reviews/carbon-review.md), [reviews/astra-review.md](reviews/astra-review.md) | The two independent reviews, unedited |

## In short

- **Site**: [academy.datatalks.club](https://academy.datatalks.club/) with one page per track, [agentic engineering](https://academy.datatalks.club/agentic-engineering/) and [AI engineering](https://academy.datatalks.club/ai-engineering/). The pages are identical in structure. The only action is "Join the shortlist", and the email is required.
- **Storage**: every signup is stored with the track and the link tags of the post or ad it came from. Page views are counted per page and source without cookies.
- **Survey**: after signing up, a visitor can open the existing survey with the email and track prefilled.
- **Campaign**: one week of organic posts to the home page, then a 14-day paid test on Meta, Google Search, Reddit and LinkedIn with one ad per track on equal terms. A fixed rule decides: a track wins if it brings at least 1.5 times the signups per 1,000 ad impressions, more signups per euro on both Meta and Google, and the organic choices point the same way.
- **Budget**: €2,500 recommended. It is a pilot: it shows a true 2 to 1 difference in about 60 to 85% of cases and a 1.5 to 1 difference in fewer than half. An unclear result is possible, and the rule says how to choose then. A one-week extension would cost up to €1,250 more and needs a separate yes.

## Waiting for Alexey

1. A yes or no on the campaign budget and the ad copy. Nothing is spent before that.
2. In the Google Form: make the email question required, reword the note above it, align "12 teaching weeks" with the site's 12 to 16, and add the academy link to the confirmation message ([details](site-and-pipeline.md#open-points), point 13).
3. A confirmation email (double opt-in) through Relay, ideally sent right after signup and in place before paid traffic starts.
4. The legal name for the Impressum and the privacy notice: "Alexey Grigorev, DataTalks.Club" as a sole proprietor, or a company with its register number. And a phone number or contact form as a second contact channel.
5. A decision on protecting the signup API against fake signups before paid traffic (rate limit, confirmed addresses only).

## Independent reviews

Two models reviewed the live site, the site and API code, and these documents on 13 November 2026, each on its own and without seeing the other's report: Carbon (Gemini 4 Carbon) and Astra (GPT-6 Astra). Both confirmed that the pages are structurally identical, the email is required, the survey prefill works, the sample-size arithmetic is right and the main benchmark citations say what the research file claims. Their findings and what happened to each:

| Finding | Found by | Status |
|---|---|---|
| Plain http served the site without a redirect, and signups from it were refused | Carbon | **Fixed.** HTTPS is enforced in the GitHub Pages settings |
| "€2,500 shows a 2 to 1 difference for certain" overstated the power; baseline rates in the sample table did not match the budget table; LinkedIn clicks and click loss were not taken out; the extension was not budgeted | both | **Fixed** in the plan: honest chances per budget, low-baseline rows, extension shown and tied to a new yes |
| The decision rule judged page signup rate after the click and pooled channels, so it could crown the track with fewer signups per euro; rule 2 could make a winner from tiny counts; "no difference" was claimed from an unclear result | both | **Fixed** in the plan: signups per impression and per euro are primary, channels are read separately, the 1.3 rule is a lean with a minimum count, the third outcome is "unclear" |
| People who join both shortlists count twice | both | **Fixed in the plan** (first choice counts). The export script still needs a first-choice view: open |
| Paid and organic LinkedIn share one page view counter; both ad arms had the same link tags | both | **Fixed in the plan**: every paid link carries its arm in `utm_content`. Storing `utm_medium` in the counter: open |
| Google ad descriptions were longer than the 90-character limit; the keyword list and ad text favoured the AI track | both (limit), Carbon (bias) | **Fixed** in the plan: assets within limits, neutral keywords, a shared "AI" headline |
| Meta: second creative did not name the track; long headlines cut off the track on phones; placements were not fixed | Carbon | **Fixed** in the plan |
| Cost sources misquoted (Bravery, Benly, Superads), a stale LinkedIn A/B line, a Maven attribution | both | **Fixed** in the plan and the research file. Search conversion for planning lowered to 4.8%, Reddit click price raised |
| On phones the seat grid pushed the form's button below the fold | Carbon | **Fixed** on the site |
| The agentic page said it is for people who "have used AI tools only a little" | Carbon | **Fixed** on the site |
| The home page showed "Track B" before "Track A" half the time, and numbered outcomes 01, 03, 05 | Carbon, own check | **Fixed** on the site |
| A visitor could sign up before reading that the program is planned and only one track runs | Astra | **Fixed** on the site: one line next to the hero form |
| "The Berlin room doesn't fit more" is not confirmed (earlier notes say the room holds 20) | Astra | **Fixed** on the site: sentence removed, the teaching reason stays |
| Optional answers looked saved when the request failed | both | **Fixed** on the site |
| The form posted to GitHub Pages without JavaScript; small tap targets | Carbon | **Fixed** on the site |
| Privacy notice: logs, survey prefill and US providers not described | both | **Fixed** on the site. Automatic deletion after 24 months: open |
| Impressum names "DataTalks.Club, represented by"; only one contact channel | both | Open, needs Alexey (point 4 above) |
| Confirmation email is planned as a later batch, not at signup | both | Open (point 3 above) |
| The public API has no rate limit and accepts forged requests | both | Open (point 5 above) |
| First-touch link tags are stored per field; long emails are cut before validation; exports can carry spreadsheet formulas | both | Open, small API changes listed in [site and pipeline](site-and-pipeline.md#open-points) |
| The survey form contradicts the site in four places | Carbon | Open, only Alexey can edit the form |
| Docker is a prerequisite on the AI track only; the pages say 12 to 16 weeks next to a 16-week draft syllabus | Carbon, Astra | Open, curriculum decisions for Alexey |
| The site counts page loads, not people, so visitor-based statistics are approximate | Astra | Accepted and stated in the plan. A per-visitor identifier would need storage on the device and a consent banner |

The messaging follows the [Oversubscribed notes](../oversubscribed/README.md): 15 seats, the honest reason, and "a Bildungsgutschein pays for a seat, it doesn't get you one".
