# What makes course landing pages convert: research and how it was applied

**13 November 2026.** Research for the two track landing pages on academy.datatalks.club (request t3290u). Every page in the first table was fetched on 13 November 2026 unless marked otherwise. Numbers are quoted from the linked sources; where a figure could not be checked against its primary source it is marked *unverified*. The last column of each table says what the site does with the finding. The site spec is in [DataTalksClub/academy `docs/SPEC.md`](https://github.com/DataTalksClub/academy/blob/main/docs/SPEC.md).

## 1. Pages examined

| Page | What it does | Used on our pages |
|---|---|---|
| [AI Evals for Engineers & PMs (Husain, Shankar), Maven](https://maven.com/parlance-labs/evals) | Headline is skill plus audience, subhead is an outcome. The hero carries a rating (4.7 from 1,056 reviews), "11 people enrolled last week", instructor one-liners, dates, the price and one "Enroll" button. Order: what you learn, instructors, who it is for, what is included, syllabus, free resources, reviews, FAQ. | Section order. Instructor proof in the hero. One call to action. |
| [Systematically Improving RAG (Jason Liu), Maven](https://maven.com/applied-llms/rag-playbook) | In waitlist mode, so the closest analogue. No price or dates. The call to action is an email form ("Get course updates", "Join waitlist"). Pain-led headline, a six-item benefit checklist, "Join 400+ engineers", a prerequisites section. | Email-only form as the single conversion. A short numbered outcomes list. Prerequisites stated. |
| [Spiced Academy, AI Engineering](https://www.spiced-academy.com/en/program/ai-engineering) | Facts line in the hero: "Full-time \| 32 weeks \| Berlin or Online". Funding banner "No money? No problem. Get 100% financing with the Agentur für Arbeit", while the financing section itself only says "could be eligible". | The facts strip. We do not copy the funding claim: our approval is pending. |
| [Le Wagon Berlin, Data Science & AI](https://www.lewagon.com/berlin/data-science-course) | Hero: "4.98/5 - 6,000+ student reviews", next date, "Limited seats". Many competing buttons (apply, syllabus, adviser call, info session). Funding wording is careful: "funding through SGB III with an education voucher (Bildungsgutschein) is possible". A four-step admission section and a student project portfolio. | A four-step "How you get in" section. Careful funding wording. One button instead of four. |
| [Ironhack paid-traffic page, AI Software Engineering](https://lp.ironhack.com/de-en/ai-software-engineering-program) | A page built for ads. The Bildungsgutschein gets a badge, a "who is eligible" list and an eight-step how-to. "Pays 100% of the program fee for you. No catch." Button "Save Your Spot Now". | A dedicated funding section on each landing page, with honest wording. |
| [neue fische, AI Engineering](https://www.neuefische.de/en/courses/ai-engineering) | Top banner "Education Voucher Check: Check your eligibility". The voucher is framed as something to check, not a promise. The application form sits at the very bottom of a long page. | Funding framed as a separate decision by the Agentur. Our form is in the hero and repeated at the end. |
| [Boot.dev](https://www.boot.dev/) | One low-commitment action, "WRITE SOME CODE (it takes 2 minutes)", repeated about five times. Proof is a learner count and employer logos. | One action repeated: "Join the shortlist" in the header, the hero, the sticky mobile bar and the final block. |
| [Y Combinator, Apply](https://www.ycombinator.com/apply) | Selectivity is shown through process, not adjectives: a fixed batch, a dated deadline, a promised decision date. | "Seats are offered in rounds. Everyone who applies gets an answer." No adjectives like "exclusive". |
| [Reforge courses](https://www.reforge.com/courses) | "Online courses taught by leading operators". The instructor is the main proof on every card. | The instructor block is its own section. |
| [Full Stack Deep Learning](https://fullstackdeeplearning.com/) | A positioning line and an email field. Proof: "Join thousands from UC Berkeley, University of Washington…". | An example of a page that is only a line and an email field. No conversion figure is published for it. |

Maven's own guidance for instructors was the most useful instructional source: [developing a top-converting landing page](https://help.maven.com/en/articles/6815473-guide-to-developing-a-top-converting-landing-page), [winning landing page](https://maven.com/resources/winning-landing-page), [nail your hero section](https://maven.com/resources/nail-your-hero-section), [how to increase your sales on Maven](https://help.maven.com/en/articles/14581209-how-to-increase-your-sales-on-maven).

Not examined: DCI (HTTP 403), Ironhack's main course page and Le Wagon's AI course page (404; the substitutes above were used), Masterschool (now a corporate page), altMBA (closed in 2024), Write of Passage, Building a Second Brain, On Deck, BloomTech, Scrimba, Frontend Masters, Section (now enterprise only).

## 2. Recommendations and what the site does

| # | Finding | Source | On the site |
|---|---|---|---|
| 1 | Keep the two pages structurally identical and vary only the offer. | [Kromatic, landing page smoke test](https://kromatic.com/real-startup-book/2-evaluative-market-experiments/value-proposition-test/landing-page-smoke-test/) | One template and one data file per track. A Playwright test compares the section order, heading levels and form fields of both pages. |
| 2 | Set the success threshold and sample size before launch. "If you don't set a threshold, you'll rationalize any result." 200 unique visitors per variant is the floor for a directional signal. | Kromatic (same page) | Thresholds and the decision rule are fixed in the [promo plan](promo-campaign-plan.md#decision-rule). |
| 3 | Test with cold traffic on equal terms. Warm audiences give "a generous upper bound". | Kromatic | Paid and organic results are read separately. |
| 4 | The ad's promise must match the page headline and button. | [KlientBoost, message match](https://www.klientboost.com/cro/message-match/) (vendor case studies, directional) | Ad headlines in the promo plan reuse the page headlines. |
| 5 | Headline: skill plus audience. Subhead: a concrete outcome. | [Maven, hero section](https://maven.com/resources/nail-your-hero-section) for the outcome-first headline; the advice on words to avoid is from [Maven's landing page guide](https://help.maven.com/en/articles/6815473-guide-to-developing-a-top-converting-landing-page), not from the hero page, which itself uses "learn" and "bootcamp" in examples | "Build, test and ship software with coding agents." and "Build, evaluate and run applications on language models." Using "program" and not "bootcamp" is our own choice. The headline names the skill and leaves the audience to the first line below it ("for people who already write code"). |
| 6 | A one-line facts strip under the headline. | Spiced, Le Wagon | Six facts: start, format, where, language, seats, tuition. |
| 7 | Instructor proof in the hero. | Both Maven AI pages | Photo and one line in the hero. The proof is the Zoomcamps' GitHub stars (86,755 across five repositories on 13 November 2026, written as "85,000+"), and it is labelled as that. There are no alumni of this program, so there are no testimonials. |
| 8 | One conversion and a short form. Conversion falls as fields are added; dropdowns and text areas hurt most. Pages with one link converted at 13.5% against 10.5–11.9% with more links (correlational; the primary report was not retrieved). | [HubSpot, 40,000 landing pages](https://blog.hubspot.com/blog/tabid/6307/bid/6746/which-types-of-form-fields-lower-landing-page-conversions.aspx), [Unbounce, Gardner 2015](https://unbounce.com/cta-conf/Oli_Gardner_CTAConf2015.pdf) | One field: email, required. No navigation menu on the landing pages. The pages do carry a few proof and legal links (instructor proof, Bildungsgutschein explainer, privacy, Impressum, the other track), so they are not single-link pages. |
| 9 | Name the button after the honest action. | Maven waitlist mode on the RAG page | "Join the shortlist". Not "Apply" or "Enroll", because there is nothing to apply to yet. |
| 10 | Write short and plain. Copy at 5th to 7th grade level converts at 11.1%, professional-level copy at 5.3%. The median-converting education page has 363 words. | [Unbounce Conversion Benchmark Report](https://unbounce.com/conversion-benchmark-report/) | Short sentences above the fold. Depth sits in collapsible syllabus and FAQ blocks. The pages are still much longer than the 363-word median (about 880 words with the blocks closed, about 1,460 open). That is a deliberate trade for a €9,000 to €10,000 full-time program, where a visitor needs the syllabus, funding and admission answers before leaving an email. |
| 11 | Design for mobile first. About 85% of education landing page traffic is mobile; desktop converts 17.6% better (12% against 10.2%). | [Unbounce, education](https://unbounce.com/conversion-benchmark-report/education-conversion-rate/) | Mobile layout designed first. A sticky bottom bar keeps the button reachable (an inference; no test of sticky bars was found). |
| 12 | Order: hero, outcomes, instructor, who it is for, syllabus, projects, funding, admission, FAQ, repeated call to action. | Both Maven pages, Maven guide | Hero, facts, outcomes, final project, instructor, fit, syllabus, funding, admission, FAQ, join. |
| 13 | "Who it's for" should be "specific enough to disqualify people". | Maven guide | "This is for you if" and "This is not for you if", three or four lines each. |
| 14 | Syllabus modules should say what you do and what you produce, not list topics. | Maven guide | Each of the 16 modules has one "You produce" line. |
| 15 | Show the final project. | Le Wagon, Ironhack | A "Final project" section set in large type. |
| 16 | The FAQ should answer objections. | Maven guide | Ten questions: status, what the shortlist gives, prerequisites, funding, price, place, schedule, residence, selection, data. |
| 17 | State funding status plainly. German providers that are approved write "possible" and "check your eligibility". | Le Wagon, neue fische | "A Bildungsgutschein pays for a seat. It doesn't get you one." Approval is described as pending on both pages, with identical wording so funding does not confound the test. |
| 18 | State capacity as a fact and describe the process. | Y Combinator; [Oversubscribed summary](https://www.shortform.com/summary/oversubscribed-summary-daniel-priestley) and [our own notes](../oversubscribed/principles.md) | "15 seats", the reason, four admission steps. |
| 19 | No countdown timers or invented urgency: they inflate signups without measuring demand. | Kromatic | None on the site. The seat grid says "none offered yet". |
| 20 | Say that the product is planned and what the email buys. | [Amplitude, fake door testing](https://amplitude.com/explore/experiment/fake-door-testing) | The first FAQ answer says the program is planned and that the shortlist decides which track runs. |
| 21 | Ask one more optional question after the email is captured. | [RightMessage, thank-you page surveys](https://rightmessage.com/resources/thank-you-page-surveys) (practice, no measured lift) | The success panel asks two optional one-tap questions (where you are based, how you would pay) and links to the existing survey with the email and track prefilled. |
| 22 | Keep the page fast. A 1-second page converts about three times a 5-second page (*from secondary reports*). | [Portent](https://www.portent.com/blog/analytics/research-site-speed-hurting-everyone.htm) | Static pages, self-hosted fonts, under 15 KB of JavaScript, no third-party requests. |
| 23 | Video is optional; results are mixed. | [VWO](https://vwo.com/blog/image-outperforms-video-increases-monthly-revenue/) | No video in the first version. |

## 3. Benchmarks

| Metric | Number | Source |
|---|---|---|
| Median landing page conversion, all industries | 6.6% (41,000 pages, 57 million conversions) | [Unbounce](https://unbounce.com/conversion-benchmark-report/) |
| Education, median | 8.4%; higher education 6.3%; "online course" pages 18.3% | [Unbounce, education](https://unbounce.com/conversion-benchmark-report/education-conversion-rate/) |
| Education by channel | Email 14.1%, paid search 7.3%, paid social 5.1% | same |
| Education, mobile and desktop | 10.2% and 12% | same |
| Smoke test with an email signup | Paid search 5–15% (above 10% is strong); paid social 2–5% (above 5% is strong) | [Kromatic](https://kromatic.com/real-startup-book/2-evaluative-market-experiments/value-proposition-test/landing-page-smoke-test/) |
| Maven, page view to enrolment | Target 1–2%; visitors return about five times before enrolling | [Maven](https://help.maven.com/en/articles/14581209-how-to-increase-your-sales-on-maven) |
| Waitlist pages, visitor to signup | 3–10% from paid ads (*vendor figure, unverified*) | [LaunchList](https://app.getlaunchlist.com/tools/waitlist-benchmark) |

Unbounce pages are optimised and mostly American. For an English-language, selective offer shown to cold traffic in Germany, plan below the median: 2–5% from paid social and 5–8% from search.

## 4. Legal notes for Germany

These are notes from public sources, not legal advice.

| Topic | Finding | Source | On the site |
|---|---|---|---|
| Consent for marketing email | § 7 Abs. 2 Nr. 2 UWG requires prior express consent. The existing-customer exception does not apply to a waitlist. | [§ 7 UWG](https://www.gesetze-im-internet.de/uwg_2004/__7.html) | The form has one purpose and says so next to the button. The consent text version and the time are stored with each signup. |
| Double opt-in | No statute names it, but the sender has to prove consent. The Sachsen-Anhalt data protection authority calls double opt-in required practice for electronic consent, with an advertising-free confirmation email. | [LfD Sachsen-Anhalt](https://datenschutz.sachsen-anhalt.de/fileadmin/Bibliothek/Landesaemter/LfD/Informationen/Internationales/Datenschutz-Grundverordnung/Was_darf_Werbung.pdf), [IT-Recht Kanzlei](https://www.it-recht-kanzlei.de/double-opt-in-newsletter.html) | **Open.** The first version stores single opt-in signups. Before the first mailing, the list has to go through a confirmation email (Relay supports double opt-in). See [site and pipeline](site-and-pipeline.md#open-points). |
| Privacy notice | Art. 13 GDPR: controller, purposes, legal basis, recipients, storage period, rights. | [Art. 13 GDPR](https://gdpr-info.eu/art-13-gdpr/) | `/privacy/`, linked next to every form. |
| Impressum | § 5 DDG: name, address, email, VAT ID, easy to find. | [§ 5 DDG](https://www.gesetze-im-internet.de/ddg/__5.html) | `/impressum/`, linked in every footer. |
| Pixels and analytics | § 25 TDDDG requires consent before storing or reading information on the device unless strictly necessary. Meta Pixel, LinkedIn Insight Tag and GA4 need consent. | [§ 25 TDDDG](https://www.gesetze-im-internet.de/ttdsg/__25.html), [datenschutz-generator.de](https://datenschutz-generator.de/tdddg-cookies/) | No cookies, no local storage, no pixels, no third-party requests. Page views are counted on our own server as daily totals per page and campaign. No consent banner is needed, and both pages are measured the same way. |

The ten pages in section 1 were chosen as well-known pages for comparable offers. None of them publishes its conversion rate, so they show common practice, not measured performance. The measured figures are in section 3.

## 5. What could not be verified

- Top-quartile conversion figures (published as chart images only).
- A "30% lift" from syllabus and review sections attributed to Maven (seen in a search summary, not on a Maven page).
- Tests of sticky mobile buttons, of a form in the hero against a button that opens a form, and of testimonial lift.
- A 2025 BGH decision on double opt-in mentioned by one blog.
