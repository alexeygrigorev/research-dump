# Alexey Grigorev: monetization strategy and operating plan

**Research date: 7 September 2026.** Repository-native archive of the research conversation and accompanying report/model. Prices, volumes, cost estimates and financial results are **analyst planning assumptions**, not actual sales, validated demand or predictions of income. Public-source observations are dated; see the [source register](sources.md) for attribution and limitations.

[Archive index](README.md) · [100 ideas: 1–50](ideas-001-050.md) · [100 ideas: 51–100](ideas-051-100.md) · [Editable financial inputs](model100.csv) · [Recalculation script](model.py)

## 1. Executive decision

The strongest default expansion is a **bounded Enterprise AI Shipping Sprint** for an existing engineering team. The clearest distinct new employer-side opportunity is **AI hiring-loop design and interviewer calibration**. Test one paid engagement in each before building infrastructure or launching another broad course.

There are also attractive opportunities in developer-vendor activation services, employer memberships, curriculum licensing and hands-on developer research. These are alternatives and sequenced extensions, not a recommendation to launch several businesses simultaneously.

The central proposition is to sell a company a specific additional outcome: an evaluated workflow, a usable hiring process, maintained onboarding material or an independent answer about developer adoption. Preserve free public education. Charge for execution, organizational coordination, expert feedback and accountable delivery rather than making existing access worse.

An important qualification: Alexey already advertises consulting, DevRel, private workshops, Buildcamp, Labs and a USD 10,000 AI-Native Business Operating System program. A public price does not prove sales, but this is not a creator starting from zero. **A new offer must beat the actual contribution per founder hour of existing work it would displace.** [S05; S06; S09; S10; S28; S30](sources.md)

## 2. What the public evidence says about the starting position

### Production credibility, not only an audience

Alexey's public CV connects DataTalks.Club with prior OLX work involving ML platforms, duplicate detection and search. That supports engineering-team engagements, reliability work and marketplace-specific projects. It is relevant experience, not permission to reuse a former employer's confidential code or data. Older biographies must not be treated as proof of current employment. [S01](sources.md)

### Substantial, overlapping practitioner distribution

The July 2026 DTC sponsorship page reports over 130,000 newsletter subscribers, nearly 100,000 Slack members and 81,000 YouTube subscribers. These channels overlap and should not be added together. Public reach also does not establish active readership, buyer authority, purchasing intent or net incremental sales. [S02](sources.md)

The community survey published in May 2025 reported 40.6% senior individual contributors and 10.1% team leads. This suggests a plausible employer-funded segment reached through technical champions, but it is an older self-selected survey, not a census of the September 2026 audience or a measure of available budgets. [S03](sources.md)

### A relevant research and intellectual-property starting point

The AI Engineering Field Guide README describes analysis of 6,964 job descriptions, interview material and role-transition paths. This provides a starting point for role diagnostics, original work simulations, interviewer training and aggregate research. The potential commercial asset is original synthesis, assessment design and a repeatable methodology—not an assumed exclusive right to copied job postings or interview questions. [S08](sources.md)

### Existing commercial offers matter more than hypothetical new ones

Buildcamp was publicly listed at USD 1,799, and AI Shipping Labs had EUR 20/50/100 monthly tiers. Corporate training, consulting, DevRel and private workshops already appear in the public offer set. Therefore, many high-ranked recommendations are **expansions or optimizations**, not entirely new revenue categories. [S05; S06; S09; S10; S30](sources.md)

The AI-Native Business Operating System program was publicly listed at USD 10,000 for November 23–December 14, 2026. Its proposition is already outcome-oriented and implementation-supported. Recommending merely to launch a high-ticket AI course would ignore the existing business. Establish its real sales, delivery effort and contribution before adding another offer. [S28](sources.md)

### What remains unknown

The research did not establish actual collected revenue, sales conversion, paid member count, retention, existing margins, support costs, ownership arrangements, contributor rights, partner economics or private calendar capacity. No prospect was contacted. No proposed price was validated with a buyer.

The strongest comparative positioning is the **combination of practical engineering credibility, teaching ability, relevant practitioner distribution and reusable technical material**. It is an advantage over a generic consultant or new creator, not proof of superiority over an established specialist. Choose a problem where this combination matters to the buyer.

## 3. Economic definitions and ranking method

### Scope of the model

All amounts are EUR, over the first 12 months after launch, excluding VAT and income/corporate taxes. Published USD competitor prices remain USD reference points; they were not silently converted into EUR quotes. The scenarios are alternatives, not an additive forecast.

The cash-cost model includes setup spending, annual incremental fixed costs and paid unit-level delivery support. Founder time includes setup, sales/administration and delivery. Existing overhead, ownership splits and actual cannibalization are unknown and must be added where applicable. Cash surplus is before founder compensation and is not automatically personal take-home income.

```
Revenue = proposed price × actual paid units
Cash costs = launch cash + annual fixed cash + unit cash cost × paid units
Founder hours = setup hours + annual fixed hours + unit founder hours × paid units
Cash surplus = revenue − cash costs
Economic surplus = cash surplus − founder hours × hourly opportunity cost
Economic ROI = economic surplus / (cash costs + founder-time cost)
```

The default opportunity cost is **EUR 150/hour**, with EUR 75 and EUR 300 sensitivity cases. This avoids claiming spectacular ROI by counting a cheap website but ignoring hundreds of hours of work. The best practical comparison is frequently cash contribution per founder hour, combined with downside exposure and repeatability.

Subscription scenarios count paid months within the year—not a full year of revenue for the year-end customer count. Net referral commissions, book receipts and platform fees are distinguished from gross customer spending. A diagnostic credited toward a larger contract must not be counted twice.

The model expenses setup capital and does not assign terminal value. This is a launch cash-return screen, not an investment valuation, accounting-profit statement or IRR. Negative first-year results for an acquisition or equity investment do not establish that the remaining asset is worthless.

### Ranking

The prioritization weights are fit to Alexey's assets 25%, evidence of adjacent demand 20%, cash contribution per founder hour 20%, speed to revenue 10%, scalability 15% and buildable moat 10%. Each component uses a five-point scale. The cash-return grade uses thresholds of EUR 400/hour for 5, EUR 250 for 4, EUR 150 for 3, EUR 75 for 2, and below EUR 75 for 1. The weighted score is divided by five to yield a score out of 100.

Scores are judgments, not probabilities. Current moat and potential moat are separate. A positive economic return and paid validation are gates, not just another score; some reasonably ranked ideas still fail the EUR 150/hour hurdle. Licensing can score well while needing several successful direct deliveries before launch.

Use `python model.py --hourly-rate 150` to reproduce the base calculations. The script supports downside/upside volumes, changed ranking weights, cash-return thresholds, capacity checks, additional displaced contribution and CSV output. Do not double-count opportunity cost in both the hourly rate and a separate displacement allowance.

### Highest-ranked standalone scenarios

| Rank | Opportunity | Launch cash | Founder hours/year | Revenue | Economic surplus at EUR 150/h | Economic ROI |
|---:|---|---:|---:|---:|---:|---:|
| 1 | Enterprise AI Shipping Sprint | 4,000 | 236 | 144,000 | 62,600 | 77% |
| 2 | Developer activation retainers | 3,000 | 152 | 108,000 | 46,200 | 75% |
| 3 | Labs employer team plan | 4,000 | 125 | 75,000 | 26,750 | 55% |
| 4 | AI hiring-loop design and calibration | 3,000 | 180 | 80,000 | 34,000 | 74% |
| 5 | Labs activation and retention improvement | 2,000 | 108 | 54,000 incremental | 19,800 | 58% |
| 6 | Vendor academy licensing | 6,000 | 147 | 100,000 | 33,950 | 51% |
| 7 | RAG and agent reliability audit | 4,000 | 198 | 96,000 | 38,300 | 66% |
| 8 | Authorized instructor delivery licenses | 8,000 | 168 | 90,000 | 31,800 | 55% |
| 9 | AI-assisted engineering adoption sprint | 4,000 | 184 | 84,000 | 26,400 | 46% |
| 10 | Fractional AI architecture council | 2,000 | 230 | 90,000 | 34,500 | 62% |
| 11 | Paid hands-on developer research | 3,000 | 118 | 72,000 | 23,300 | 48% |
| 32 | Marketplace duplicate and search sprint | 6,000 | 170 | 80,000 | 19,500 | 32% |

These are individual operating cases. Adding their revenues ignores founder capacity, customer overlap, shared budgets and cannibalization.

## 4. Twelve operating playbooks

### 4.1 Enterprise AI Shipping Sprint — the strongest default expansion

**Buyer and trigger.** A head of data, engineering manager or technical founder at a roughly 50–500-person company. The buyer has existing engineers and an approved use case, but the prototype lacks evaluation, operational ownership or a reliable handover. Target a team of 5–12 participants rather than nontechnical operators seeking broad business automation.

**Scope.** Three weeks, one approved workflow. Deliver a reproducible baseline, reference implementation, small evaluation suite, regression check, operating runbook and team handover. Exclude a full platform rebuild, unlimited integrations, security certification and indefinite support. The reference implementation must be narrowly scoped; do not promise production readiness independent of the client's access, security and deployment requirements.

**Pricing and resources.** Two founding pilots at EUR 12,000 followed by six engagements at EUR 20,000 produce EUR 144,000. The spreadsheet represents this as eight units at EUR 18,000. Budget EUR 4,000 and 35 founder hours for setup, EUR 6,000 annual fixed cash, 105 annual founder sales/administration hours and EUR 4,500 paid support per engagement. A proposed 30–45 contractor hours per engagement fits that cash allowance only with appropriate quotes and scope.

The modeled 12 founder delivery hours per engagement requires genuine delegation. It is not credible for solo bespoke implementation, and early pilots may require more. Total founder hours are 236, all cash costs EUR 46,000, cash surplus EUR 98,000 and economic surplus EUR 62,600.

**Acquisition test.** Seek permission-based introductions through 30 relevant alumni, previous guests and professional contacts. A target funnel is ten qualified conversations, four scoped proposals and one paid pilot. These are experiment targets, not conversion evidence. Qualification requires a budget holder, an actual workflow, an internal owner, permitted data and a route to access.

Suggested positioning: “We help your existing team establish an evaluation and handover process for one AI workflow in your stack. This is not a general AI course or an open-ended consulting project.”

**Sequence.** First qualify and contract a bounded outcome. Establish baseline and acceptance criteria before implementation. Deliver with a paid partner, record all sales/delivery hours, then request permission for a case study only after acceptance. Compare the next engagement's custom work with the first.

**Competitive opening.** AI Makerspace publishes broader enterprise programs starting at USD 70,000 and USD 85,000. This supports an adjacent employer-budget category but is not a directly comparable scope or validation of the proposed price. The proposed entry point is smaller and bounded. [S13](sources.md)

**Continue/stop.** Require paid commitment, accepted deliverables, at least 70% reusable material and no more than 20 founder delivery hours per pilot before scaling. Narrow or stop after 15 qualified buyer conversations without a paid commitment, or if engagements repeatedly become custom platform projects. Scalability 4/5; moat 3/5 now, potentially 4/5 through delivery methods, original exercises, paid delivery partners and permissioned outcomes.

### 4.2 Developer activation retainers — incremental value above existing media

**Buyer and trigger.** A developer-marketing or DevRel lead whose sponsorship produces attention but leaves an onboarding/adoption question unresolved. DTC already offers newsletter placements, workshops and deeper integrations. Merely renaming existing sponsorship inventory is not incremental revenue. [S02](sources.md)

**Offer.** Maintain one practical lab, run a bounded onboarding clinic, support one defined activation task and produce a consent-based friction/activation report. Sell this separately from the existing media package. Agree which behavior counts as activation before the campaign. Do not promise downstream revenue attribution or qualified leads that cannot be established.

**Economics.** EUR 9,000 additional service revenue per vendor-quarter. Four vendors buying three delivered quarters each yield 12 units and EUR 108,000. Setup EUR 3,000/25 founder hours; annual fixed cash EUR 6,000 and 55 founder hours; unit cash EUR 2,500 and six founder hours. Total cash costs EUR 39,000, founder time 152 hours, cash surplus EUR 69,000, economic surplus EUR 46,200.

**Buyer value test.** If EUR 9,000 produces 25 incremental developers completing the agreed task, that is EUR 360 per incremental activation. Ask the buyer whether this outcome is valuable enough; do not substitute reach numbers. Definitions, observation windows and limitations belong in the proposal.

**First sale.** Two existing sponsors buy the uplift separately and agree a renewal decision process. Use paid operational support. Continue on renewal and attributable task evidence, not a pleasing report alone.

**Competition and moat.** Draft.dev's dated public guide gives its own starting retainer of USD 8,000/month; this is a category anchor, not a current quote or direct comparable. Relevant distribution plus practical adoption work is the proposed difference. Scale 4/5; moat 3 → 4 if repeatable results and useful consented insights accumulate. [S17; S18](sources.md)

**Ownership caution.** The DTC sponsorship page says money is reinvested in the community. This is an operating-organization opportunity, not automatically personal distributable income. Clarify compensation, ownership, contributor rights and the public commitment. Preserve editorial independence and avoid sponsor concentration. [S02](sources.md)

### 4.3 Labs employer team plan — recurring revenue without a new platform

**Buyer.** A manager funding practical development for five engineers and wanting coordination, not just access to content.

**Offer.** Five Premium-equivalent memberships, kickoff, a manager-facing progress brief and a capped quarterly review supported by paid mentors. Proposed price: EUR 750/month on an annual commitment, billed monthly. Five individual Premium seats at the public EUR 100 monthly tier imply EUR 500 before annual discounts; the additional EUR 250 must buy useful employer coordination. [S06](sources.md)

**Economics.** The first-year model counts 100 actual paid team-months, not 15 teams paying all year from day one. Revenue EUR 75,000; setup EUR 4,000/35 hours; fixed cash EUR 8,000 and 55 founder hours; unit support EUR 175 and 0.35 founder hours. Total cash cost EUR 29,500, founder 125 hours, cash surplus EUR 45,500 and economic surplus EUR 26,750.

**Validation.** Five employers pay using the existing workflow before building a dashboard. Identify an internal manager and a practical milestone for each team. Record attendance, progress, paid support cost, renewal intent and actual renewal.

**Cannibalization.** Five already-paying individuals moving to a company invoice are not five new customers. Count only incremental contribution, including the extra coordination burden. Define support entitlements so private review does not become unlimited consulting.

**Positioning.** DataCamp Business and DataExpert demonstrate alternatives in technical learning. Generic library access is weak differentiation; the intended distinction is practical progress plus a relationship with the employer. Scale 5/5; moat 2 → 3. [S19; S20](sources.md)

### 4.4 AI hiring-loop design and calibration — the best distinct employer-side idea

**Buyer.** A company hiring AI engineers whose interview loop cannot reliably distinguish framework familiarity from actual engineering competence.

**Offer.** For one role, define responsibilities, create two original work simulations, write scoring anchors, calibrate four human interviewers and review how the process works in real use. Example tasks are diagnosing retrieval regression or designing an agent workflow with explicit failure handling. Avoid a trivia question bank.

**Economics.** EUR 8,000 per employer × ten employers = EUR 80,000. Setup EUR 3,000/30 hours; annual fixed EUR 6,000/50 hours; each engagement EUR 1,000 paid support and ten founder hours. Annual cash costs EUR 19,000; founder 180 hours; cash surplus EUR 61,000; economic surplus EUR 34,000.

**Why Alexey.** The Field Guide is a useful starting point for role patterns and assessment problems, and teaching can help interviewers apply a rubric consistently. Neither the corpus nor audience proves assessment validity or willingness to pay. [S08](sources.md)

**Competition.** CodeSignal advertises entry pricing from USD 79/month; Karat operates in AI-ready engineering evaluation. An EUR 8,000 question bank is not defensible against those alternatives. Role design, original work simulations and human calibration are a different service. Do not claim superiority over specialist incumbents without evidence. [S15; S16](sources.md)

**First three customers.** Sell to managers with a live hiring need. Require three paid design partners; at least two must use the rubric in actual interviews, and at least one must pay for a refresh or additional role. Compare interviewer disagreements before and after calibration, while avoiding unsupported claims that a small pilot proves predictive validity.

**Boundaries.** Employers retain hiring decisions. Use authorized candidate data, transparent criteria, appropriate accommodations, original exercises and human review. Do not start with automated ranking, certification or hiring software. Scale 4/5; moat 2 → 4 through original assessment IP, calibrated delivery and employer reuse.

### 4.5 Labs activation and retention improvement — optimize before expanding

**Nature of the idea.** This is an improvement to an existing business, not a separate new revenue stream. Offer role-specific 30-day project milestones with paid mentor support using existing material.

**Economics.** The modeled EUR 54,000 uplift requires 900 genuinely incremental paid member-months at EUR 60 blended revenue. Setup EUR 2,000/30 hours; fixed EUR 7,000/60 hours; support EUR 10 and 0.02 founder hours per incremental member-month. Total cash costs EUR 18,000, founder time 108 hours, cash surplus EUR 36,000, economic surplus EUR 19,800.

**Critical uncertainty.** The actual paid membership base and retention are unknown. The 900-month uplift may not be attainable from the current base. Do not infer feasibility from free audience size. [S06](sources.md)

**Experiment.** Use a randomized or carefully matched holdout, define the intervention and support allowance, and measure net paid retention over three months. Include refunds, paid mentors and movement between existing products. Do not attribute natural growth or all participant signups to the intervention.

**Decision.** Expand only if incremental contribution is positive after support and the experiment beats another use of founder time. Scope the first test tightly; no new membership platform is needed. Scale 4/5; moat 2 → 3 if a repeatable completion/support method improves durable outcomes.

### 4.6 Vendor academy licensing — reusable education IP

**Buyer.** A developer-tool vendor whose customers need practical onboarding but whose team cannot continuously produce good educational material.

**Offer.** Three original modules, assessments, a sample application, facilitator guides and a bounded update commitment. Use the vendor's existing learning or lab infrastructure. Instruqt already serves the hands-on lab category; building an additional platform creates another business and support burden. [S18](sources.md)

**Economics.** EUR 25,000 per package × four = EUR 100,000. Setup EUR 6,000/40 founder hours; fixed EUR 6,000/35 hours; unit delivery EUR 8,000 and 18 founder hours. Cash costs EUR 44,000; founder 147 hours; cash surplus EUR 56,000; economic surplus EUR 33,950.

**First sale.** Secure one prepaid EUR 15,000–25,000 design partner before a catalog. Separate reusable underlying material from vendor-specific implementations. Retain reusable IP and negotiate clear nonexclusive rights where appropriate. Maintain a change budget and acceptance criteria.

**Repeatability.** The first package is not automatically recurring revenue. Sell maintenance separately and validate renewal. Avoid exclusivity and broad rights transfers that prevent reuse. Paid content/support partners provide capacity, with Alexey responsible for technical quality. Scale 4/5; moat 3 → 4 through original material, delivery know-how and repeat vendor use. [S10; S17; S18](sources.md)

### 4.7 RAG and agent reliability audit — a narrower alternative entry offer

**Buyer and offer.** The technical owner of one existing workflow with an observed quality problem. A ten-business-day review of permitted traces, failure categories, evaluation set, regression gate and handover. Require adequate data and a baseline; do not promise safety certification or a universal quality increase.

**Economics.** EUR 12,000 × eight audits = EUR 96,000. Setup EUR 4,000/30 founder hours; annual fixed EUR 4,000/40 hours; each audit EUR 2,500 cash support and 16 founder hours. Total cash cost EUR 28,000, founder time 198 hours, cash surplus EUR 68,000 and economic surplus EUR 38,300.

An EUR 3,000 diagnostic may be credited toward the EUR 12,000 engagement. It is not additional revenue when credited. An audit may be an alternative to a shipping sprint, not an automatic second purchase by every client.

**Positioning.** Parlance Labs already specializes in AI evaluation. Target a retrieval, data-pipeline or production-handover issue where Alexey's broader engineering context matters, rather than claiming generic specialist superiority. Published agent-engineering survey evidence is a dated, self-selected indication of challenges, not proof of this service's demand. [S09; S14; S23](sources.md)

**Test.** Two paid audits with adequate baseline access, followed by one paid maintenance renewal or qualified referral. Cap data access, implementation changes and post-delivery support. Scale 3/5; moat 2 → 3; cash opportunity is stronger than standalone software defensibility.

### 4.8 Authorized instructor delivery licenses — after repeatable direct delivery

**Buyer.** A training firm with corporate sales access but insufficient practical AI curriculum or delivery capability.

**Offer.** New original facilitator guides, assessments and authorized brand use, with observed teaching and annual quality review. Licensing public open-source code as though it were exclusive would be the wrong proposition. Rights to contributors' work and new materials must be established first. [S05; S27](sources.md)

**Economics.** EUR 15,000 per partner-year × six = EUR 90,000. Setup EUR 8,000/60 hours; fixed EUR 10,000/60 hours; unit cash EUR 2,500 and eight founder hours. Cash costs EUR 33,000, founder 168 hours, cash surplus EUR 57,000 and economic surplus EUR 31,800.

**Sequence.** First complete three repeatable direct engagements. Then recruit two paying partners who pass observed delivery assessment. Define what material/brand may be used, update obligations, quality standards and how poor delivery is handled. Avoid a large partner program before customers demonstrate they can sell and deliver it.

**Moat.** An effective paid delivery network can scale beyond Alexey's calendar; brand dilution is the corresponding risk. Scale 5/5; current moat 2/5, potential 4/5. This ranks well strategically but is not a first-week launch recommendation.

### 4.9 AI-assisted engineering adoption sprint

**Buyer.** An engineering manager with 8–20 developers adopting coding agents without a shared operating method.

**Offer.** Representative-task baselines, approved tool-use policies, code-review/test guardrails and maintainer training. Measure completed work, review burden and escaped defects; do not promise a universal productivity multiplier or use lines of generated code as the value metric.

**Economics.** EUR 14,000 × six teams = EUR 84,000. Setup EUR 4,000/35 hours; fixed EUR 5,000/65 hours; each engagement EUR 3,500 paid delivery and 14 founder hours. Annual cash costs EUR 30,000; founder 184 hours; cash surplus EUR 54,000; economic surplus EUR 26,400.

**Validation.** Two paying teams approve access and a representative task set. Compare work against a baseline using consistent definitions. Keep security review, proprietary source-code permissions and client rollout ownership explicit.

**Risk.** This overlaps existing workshops and internal developer-productivity functions. It becomes attractive through bounded scope and credible measurement, not rebranding generic tool training. Scale 3/5; moat 2 → 3. [S10; S13; S23; S30](sources.md)

### 4.10 Fractional AI architecture council — cash, not unlimited scale

**Buyer.** A CTO needing senior judgment but not a full-time principal engineer or an outsourced implementation team.

**Offer.** Two architecture reviews per month and bounded asynchronous decision support. Exclude on-call, emergency coverage and hands-on implementation. Maintain a small agreed issue queue and written decision records.

**Economics.** EUR 3,000 per client-month × 30 paid months = EUR 90,000. Setup EUR 2,000/15 hours; fixed EUR 4,000/35 hours; monthly paid support EUR 500 and six founder hours. Total cash costs EUR 21,000, founder 230 hours, cash surplus EUR 69,000 and economic surplus EUR 34,500.

**Validation.** Two three-month retainers with a fixed issue allowance. Observe whether clients value a repeatable review cadence and whether work stays inside six founder hours per month. If it becomes interrupt-driven consulting, adjust price/scope or stop.

**Positioning.** Production engineering experience and clear tradeoff explanations are relevant. Existing consulting means this is packaging and sales execution, not a newly discovered capability. Scale 2/5; moat 2 → 3. [S01; S09](sources.md)

### 4.11 Paid hands-on developer research — an underused audience advantage

**Buyer.** A product, research or DevRel team asking why qualified developers struggle to adopt a tool.

**Offer.** Recruit 15–20 appropriately qualified, opt-in practitioners, observe realistic tasks and deliver an independent friction report plus findings workshop. Budget approximately EUR 150 per participant, along with paid research assistance and quality review.

**Economics.** EUR 18,000 × four studies = EUR 72,000. Setup EUR 3,000/30 hours; fixed EUR 4,000/40 hours; unit cash EUR 6,000 and 12 founder hours. Cash costs EUR 31,000; founder 118 hours; cash surplus EUR 41,000; economic surplus EUR 23,300.

**Differentiation.** SlashData and Respondent establish adjacent developer-research and recruitment categories. The proposed niche is not the largest panel; it is a smaller qualified group doing genuine engineering work. The quality of the task, screening and synthesis must justify the service beyond recruitment alone. [S21; S22](sources.md)

**Validation and safeguards.** Sell one EUR 10,000+ study before panel software. Require qualified attendance of at least 80% and evidence of repeat study demand. Pay participants, obtain purpose-specific consent, minimize identifying data and prohibit client influence over findings. Never sell member lists or promise positive conclusions. Scale 4/5; moat 2 → 4 through a reliable permissioned participant network and research methods.

### 4.12 Marketplace duplicate detection and search — the differentiated technical direction

**Buyer.** A classifieds, recommerce or marketplace CTO with duplicate listings, catalog problems or poor search relevance.

**Offer.** Establish an approved historical baseline, agree the cost of relevant errors, evaluate a bounded improvement and hand over the implementation and measurement process. A paid feasibility stage needs representative client-owned or otherwise authorized data.

**Economics.** EUR 20,000 × four projects = EUR 80,000. Setup EUR 6,000/40 hours; fixed EUR 5,000/50 hours; unit cash EUR 6,000 and 20 founder hours. Cash costs EUR 35,000; founder 170 hours; cash surplus EUR 45,000; economic surplus EUR 19,500.

**Why it is distinctive.** Prior OLX/search/duplicate experience is a more specific fit than generic AI-agency positioning. It does not confer rights to confidential former-employer material. [S01; S11](sources.md)

**Why rank 32, not top five.** The technical fit is unusually good, but customer acquisition and integrations are less validated than education-adjacent offers. Expect more discovery and a narrower lead pool.

**Gate to software.** Start with paid services. Build a hosted duplicate-detection API only after several clients request essentially the same operational product and commit meaningful minimums. Scale 3/5; moat 3 → 4 if reusable technical assets and outcome evidence accumulate.

## 5. What competition does and does not prove

| Market | Existing alternatives | Proposed narrow opening | Evidence still required |
|---|---|---|---|
| Employer AI training | AI Makerspace, internal enablement, existing Buildcamp | Smaller bounded workflow with evaluation and handover | Buyer accepts scope/price; delivery stays reusable |
| Hiring assessment | CodeSignal, Karat, internal interviewers | Role design plus original work simulations and calibration | Actual rubric use, repeat purchase, assessment quality |
| Developer content/adoption | Draft.dev, in-house DevRel, Instruqt ecosystem | Relevant distribution plus a maintained activation task | Incremental task completion and vendor renewal |
| Team learning | DataCamp Business, DataExpert, internal guilds | Practical accountability and manager coordination | Net incremental seats and renewals after support costs |
| Developer research | SlashData, Respondent, internal researchers | Qualified practitioners observed doing niche tasks | Paid study and repeat demand, with independent methods |
| Reliability evaluation | Parlance Labs, platform teams, tooling vendors | Retrieval/data/production-handover-specific review | Accepted useful findings and bounded delivery cost |

Sources and limitations: [S05; S13–S23](sources.md). Competitors demonstrate that an adjacent category exists. They do **not** establish market spare capacity, the proposed number of customers, or a clear advantage in every segment. Price anchors are advertised prices, not verified transactions. Claims of opportunity must become paid experiments.

## 6. A capacity-aware first-year portfolio

Initially combine the engineering sprint and hiring-design package at lower volumes than their individual scenarios. This tests two related employer problems without multiplying course calendars.

| Scenario | Paid volume | Revenue | Cash costs | Founder hours | Cash surplus before founder pay | Economic surplus at EUR 150/h |
|---|---|---:|---:|---:|---:|---:|
| Downside | 2 shipping + 1 hiring | 44,000 | 29,000 | 254 | 15,000 | -23,100 |
| Base, normalized pricing | 6 shipping + 6 hiring | 156,000 | 52,000 | 352 | 104,000 | 51,200 |
| Upside | 10 shipping + 12 hiring | 276,000 | 76,000 | 460 | 200,000 | 131,000 |

These use the model's EUR 18,000 average sprint price and EUR 8,000 hiring price. They are volume scenarios, not probability-weighted forecasts. Fixed annual costs and sales time remain in the downside. A failed presale test should stop earlier instead of incurring the full annual spend.

### Preserve the pilot-pricing correction

The standalone eight-sprint mix of two EUR 12,000 pilots and six EUR 20,000 regular engagements averages EUR 18,000. That average does **not** apply unchanged to a smaller six-sprint mix.

With exactly two EUR 12,000 pilots plus four EUR 20,000 regular sprints and six EUR 8,000 hiring packages, base revenue is **EUR 152,000**, cash costs EUR 52,000, founder hours 352, cash surplus EUR 100,000 and economic surplus **EUR 47,200**. The archive retains this correction alongside the normalized original model. Replace averages with actual contracts.

### Opportunity cost can reverse the decision

| Value of founder time | Normalized base economic surplus | Economic ROI |
|---:|---:|---:|
| EUR 75/hour | 77,600 | 99% |
| EUR 150/hour | 51,200 | 49% |
| EUR 300/hour | -1,600 | -1% |

The normalized base breaks even against approximately EUR 295 of alternative contribution per founder hour. At a genuinely available EUR 300/hour alternative, these modeled new offers are not an improvement. A high-ticket existing offer may be the better place to invest, but only actual receipts and delivery effort can establish that.

The model's 600-hour incremental annual capacity is a planning cap, not evidence that Alexey has 600 free hours. Existing teaching, operations, recovery time and other commitments must be protected. Do not hire or spend against the upside scenario before sales.

## 7. First 90 days: sell, deliver, measure

Public pages showed Buildcamp scheduled September 21–November 22 and the AI-ops program November 23–December 14, 2026. These are not Alexey's private calendar, but they caution against adding a substantial teaching commitment during the same period. [S05; S28](sources.md)

| Period | Work | Founder budget | Decision gate |
|---|---|---:|---|
| September 7–20 | Review existing economics; define two bounded offers; clarify rights and paid delivery partner | 16 hours | New offers plausibly beat a real alternative |
| September 21–October 4 | Permission-based introductions, qualified conversations and scoped proposals | 16 hours | One paid commitment before substantial building |
| October 5–November 1 | Deliver first engineering pilot with a paid partner | 32 hours | Accepted artifacts and recorded delivery economics |
| November 2–22 | Deliver hiring-design pilot and observe real use | 24 hours | Employer applies rubric, not merely approves document |
| November 23–December 6 | Review economics, referrals, repeatability and capacity | 16 hours | Continue only offers clearing the actual hurdle |

Total: **104 founder hours**, approximately eight per week. Stage the combined EUR 7,000 launch envelope. Keep uncommitted cash at risk below EUR 5,000 before paid validation; do not spend an annual plan upfront. Contractor delivery budgets are separate modeled unit costs and should be funded through appropriate customer receipts/milestones rather than hidden inside setup spending.

### A minimum commercial test record

For each prospect, record the buyer role, live problem, current alternative, budget authority, scope, price proposed, objections and whether money was committed. For each delivered engagement, record all founder sales/delivery hours, paid support, custom work, accepted artifacts, refunds and follow-on purchases. Separate a referral from a renewal and a new customer from a migration between existing products.

An enthusiastic response, a waitlist signup or an audience poll is not the same as a funded project. The relevant evidence is a paid commitment, accepted deliverable and contribution after the actual work.

### Stop rules

Narrow or stop an offer after 15 qualified conversations without a paid commitment. Reprice or reduce scope when a pilot requires more than 20 founder delivery hours or mostly custom implementation. Do not convert unpaid interest into a software build. Do not continue a retention experiment with negative contribution after support. Do not pursue a licensing program until delivery is reusable and rights are clear.

## 8. Scalability and a moat that can actually be earned

Audience access reduces some acquisition friction. It is not by itself durable product differentiation, a permanent right to contact people or a guarantee of low customer acquisition cost.

The strongest prospective assets are original assessments and delivery material, calibrated paid instructors/interviewers, permissioned outcome evidence, employer relationships and repeatable renewal workflows. Data is defensible only when provenance, consent, relevance and ongoing collection are legitimate; a folder of scraped job postings is not automatically proprietary.

| Stage | Asset to establish | Evidence before expansion |
|---|---|---|
| First 90 days | A paid bounded deliverable | Acceptance and measured contribution per founder hour |
| Months 4–6 | Repeatable original process/material | Three similar engagements with substantial reuse |
| Months 7–12 | Paid delivery bench and renewal behavior | Quality survives delegation; customers buy again |
| Later | Licensing or narrow software | Several buyers pay for the same reusable capability |

A repeatable service can be economically attractive before it becomes a software company. Conversely, a scalable product with no distribution or retention advantage can consume more capital than a small high-margin service. Scale is not a reason to ignore the path to paying customers.

## 9. Why lower-ranked ideas remain in the archive

The full 100-idea inventory deliberately includes different directions: services, employer learning, vendor media/adoption, recruiting, research/data products, publishing, licensing, events, operational software, developer infrastructure, consumer tools and investing. Keeping lower-return ideas makes the selection explicit rather than pretending only obvious winners were considered.

**Generic AI software.** Hosted RAG chatbots, resume generators and code explainers face weak proposed differentiation relative to build, support and acquisition effort. Existing code lowers prototype cost, not necessarily cost to operate a paying business. Alexey's abandoned-project writing is relevant evidence against repeating tools displaced by broader capabilities, not proof that all similar products must fail. [S11; S12](sources.md)

**PocketShell and lightweight search tools.** A paid extension needs a specific unmet operational need. Termius already has free and paid remote-access alternatives; basic SSH access is not sufficient differentiation. For hosted search or duplicate APIs, seek repeated paid service demand before uptime obligations and security support. [S24; S25](sources.md)

**Books and low-priced courses.** They may strengthen reputation and acquisition, while showing weak first-year direct economic returns after writing and maintenance time. Strategic marketing value should be evaluated explicitly, not smuggled into a cash forecast. Existing free Zoomcamps and paid courses also make cannibalization relevant. [S01; S05; S06](sources.md)

**Certificates and assessment software.** Issuing a certificate is easier than obtaining employer recognition. Validity, identity assurance, updating, accommodations and appeals require resources. Develop employer-used original assessments and human calibration before a standalone exam or automated candidate-ranking product. [S08; S15; S16](sources.md)

**Events and retreats.** These can deepen relationships but add venue commitments, cancellations, logistics and cash exposure. Anchor buyers/presales should cover noncancelable commitments before expanding the event operation. Direct financial returns must include founder coordination time.

**Advertising, affiliates and merchandise.** These can be sensible tightly bounded additions to existing activity. They are weaker candidates for a dedicated new operation because of low ticket size, platform dependence, low defensibility or trust conflicts. Do not count existing revenue as incremental.

**Investing and consulting for equity.** These are capital allocation and risk decisions, not reliable near-term earned-income strategies. The model assumes no speculative first-year cash distributions or markups. Its low rankings are cash-generation screens, not assertions that an equity stake has zero fair value.

The correct reason to promote a lower-ranked idea is changed evidence: a real buyer, repeated standardized demand, better unit costs, verified retention, lawful owned IP or an identifiable distribution advantage. Technical excitement alone is insufficient.

## 10. Commercial, legal and trust boundaries

Community economics and personal income are distinct. Clarify the operating entity, compensation, ownership, contributor rights and obligations before treating a DTC contract as personal cash. Pay mentors, reviewers, researchers and delivery partners; do not turn learners into unpaid client labor. [S02](sources.md)

Use consent-based introductions and research participation. Do not sell member lists or expose private participant/candidate data. Use only authorized client data and respect former-employer confidentiality. Keep sponsor-funded research independent and disclose referral incentives. Do not manufacture exclusivity around existing open-source materials.

Obtain Germany-specific legal review before expanding remote paid instruction. ZFU's provider FAQ addresses the applicability of distance-learning rules to business customers; the actual service and contract matter, not merely calling something a workshop or consulting. This report does not decide any particular offering's legal classification or compliance. [S27](sources.md)

Use actual platform/payment terms. Maven's payment documentation describes a platform fee plus processing, while affiliate channels can add costs. Owned-audience and affiliate economics should not be mixed, and advertised prices are not net collected income. [S26; S29](sources.md)

No employment outcome, security certification, percentage productivity gain or financial return is promised. A small test can justify another bounded test, not broad claims of effectiveness.

## 11. Final recommendation

Start with **one funded engineering-team sprint and one paid hiring-design pilot**, while protecting the actual economics of existing offers. The sprint is the strongest near-term expansion; hiring design and hands-on developer research are more distinct new directions. Employer Labs plans and developer activation are promising recurring extensions, and academy/instructor licensing becomes attractive after repeatable delivery.

Let accepted work, real contribution per founder hour and repeat purchases decide what scales. Preserve the original research as a dated hypothesis set, then record experimental evidence separately. The next moat is not a larger idea list: it is useful original work that customers repeatedly pay for and that a paid team can deliver without requiring Alexey in every hour.
