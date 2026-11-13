# Moat catalogue — what AI cannot cheaply copy

Each entry: what it is, why an AI-assisted copycat cannot reproduce it, how a small team builds it, risks. "Evidence" points to the source log ([sources.md](sources.md)) and the subagent notes in [notes/](notes/). Strength ratings are the orchestrator's synthesis across sources, not a quote from any single speaker.

The test that runs through the whole catalogue (from the levels.io / distribution notes, rephrased): **if a clone launched tomorrow at half your price, what would still make customers stay or choose you?** Anything that answers that question is a moat. Features, code and UI are not on the list.

## Not moats any more (agreed across most sources)

| Former moat | Why it fails now | Evidence |
|---|---|---|
| Features / "unique feature" | Feature parity is a prompt away; called a "false moat" | Vollset (SFTRFU 836), Eden (MicroConf US 2026), Walling (MicroConf Europe 2026) |
| Codebase / engineering effort | "The cost of creating code is going to drop" | Eden [8:36], Danjou essay |
| Integrations alone | Agents and MCP make connectors cheap; integrations are table stakes unless they write back into a system of record | Vollset (836), Eden; Pandium (vendor) argues the opposite — low weight |
| Data you let customers export to anyone | The analysis layer above exportable data is being commoditised | tscsw "Don't Short SaaS"; How I Invest podcast |
| Plain "more data" | More data is usually a scale effect with diminishing returns, not a network effect | a16z "Empty Promise of Data Moats"; NFX "Truth About Data Network Effects" |
| Speed alone | Copyable; it buys time but doesn't defend | Hewitt calls it "maybe the universal advantage"; tactical notes rate it weak on its own |

## The moats that still work

### 1. First-party, outcome-linked proprietary data
- **What:** data generated inside your product by real usage and real outcomes (what worked, what failed, edits, approvals, results), which only you collect and which never leaves your system in usable form.
- **Why AI can't copy it:** a model, or a competitor using one, never sees it. It isn't in the training data, it isn't on the web and it can't be scraped. The Europe "Sell the outcome" talk: the learning loop "stays with you" and "it's not fast-forwardable" [10:46–11:14].
- **How to build:** instrument the core workflow; capture corrections and outcomes, not just inputs; build a private eval set from real traces (Hamel Husain's evals post); make the product better *because of* the accumulated data and show customers that it does.
- **Risks:** data that is easy to export, low-value or quick to go stale protects nothing (fpso, tscsw); most "data network effects" are really scale effects (a16z, NFX). Walling (MicroConf Europe 2026) is blunt about this: "If you have a lot of data, doesn't matter" [32:15]. His moat is the *learning loop* [31:25], not the raw data. Deep dive: [first-party-data.md](first-party-data.md).
- **Strength:** strong only when the data is scarce, compounds and is tied to outcomes. Otherwise weak.

### 2. Audience and distribution (owned attention)
- **What:** people who already know and trust you: an email list, YouTube, a community or a newsletter. Channels you own, not rent.
- **Why AI can't copy it:** "AI writes the code. It does not write your distribution" (Walling, SFTRFU 842). Building is now cheap and audiences are scarce (levels.io, Jun and Oct 2026). Brand and owned traffic channels are still rated strong by acquirers (Vollset, 836).
- **How to build:** pick one channel and go deep; build the audience *while* you build the product; recruit the first users by hand; reuse the same distribution engine for every product; publish what you learn.
- **Risks:** an audience isn't automatically buyers; incumbents with bigger distribution can win anyway (Andrew Chen, "Revenge of the GPT wrappers"); audience-driven growth plateaus without product retention.
- **Strength:** strong, and the most available moat for a solo founder or small team. This is Alexey's own unfair advantage (DataTalks.Club, newsletter, YouTube).

### 3. System of record, operational embedding and switching cost of *state*
- **What:** your product holds the customer's live state (their podcast feed, their DNS, their approvals, their history), so leaving means migrating that state.
- **Why AI can't copy it:** a clone can copy the UI but not the customer's accumulated state, or the risk of moving it. Hewitt's Castos example: "if you cancel with us, your podcast goes away" [26:26]. Greylock: "Foundation models do not replace existing systems of record."
- **How to build:** be where the work is stored, not only where it's viewed; take on write-back duties; own the operational burden (Walling: "you are a system of record" [21:16]; "hard to keep running" [34:00]).
- **Risks:** pure feature switching costs no longer hold (Eden); regulators and customers increasingly demand portability.
- **Strength:** strong for B2B workflows.

### 4. Outcome selling, learning loop and "the product can act"
- **What:** sell the result (a task done, a lead booked) rather than a tool someone clicks. This aims at labour budgets, not software budgets.
- **Why AI can't copy it:** the outcome depends on accumulated calibration from real-world results across customers, and a fresh clone starts from zero. Europe talk: "someone can't just take AI... and then catch up with you instantly" [12:35]. Foundation Capital, "service-as-software".
- **Walling's variant:** "You're allowed to act" [23:36]. The product holds the permission to do the work, not just show it.
- **How to build:** define one measurable outcome; price on it; log every attempt and its result; feed the results back into prompts, evals and routing.
- **Risks:** you carry delivery risk; this is hard to do before product-market fit.

### 5. Trust, relationships and accountability ("someone to blame")
- **What:** buyers know you, trust your results and have a person accountable when things break.
- **Why AI can't copy it:** trust is earned over time; "people always have bought from people" (Hewitt [28:21]); the paddo.dev "someone to blame" essay; Danjou: the real moat is domain knowledge and trust. Walling's moats include "buyers know and trust you" [19:09] and "They don't check your work" [25:25].
- **How to build:** found-led sales and support, public track record, case studies, SLAs, a face on the product.
- **Risks:** doesn't scale cheaply; it's a sales moat more than a product moat.

### 6. Vertical focus, domain knowledge and customer understanding
- **What:** deep specialisation in one industry's language, edge cases and regulation, and knowing *why* your customers buy. Gia Laudi (MicroConf US 2026): "knowing who your customer is is not the same as understanding why they buy" [18:12]; "the only way that actually compounds is to actually understand our customers better than anyone else" [28:52]. Her talk doesn't frame this as anti-AI, but customer interviews are first-party insight no model has.
- **Why AI can't copy it:** a generic model doesn't know the unwritten rules; a horizontal clone loses on fit. Hewitt: "vertical way over horizontal" [48:57].
- **How to build:** choose a niche you know; run 10–12 interviews with recent, successful customers in a 2-week sprint (Laudi [32:18]) and prioritise one job to be done [39:57]; collect edge cases as eval cases (which is also moat #1).
- **Risks:** small market ceiling.

### 7. Regulation, certification and compliance
- **What:** approvals, certifications and regulated-data handling (EU AI Act high-risk obligations, health, finance).
- **Why AI can't copy it:** paperwork, audits and liability take calendar time, not tokens. Eden: regulated environments stay defensible; Walling: "someone official already said yes" [27:00].
- **Risks:** raises the entry cost for you too; only relevant in regulated niches. Rated weak as an *anti-clone* measure in the tactical notes.

### 8. Network effects and coordinated groups
- **What:** the product gets better as more users join (two-sided marketplaces, communication graphs, a "Slack-style" coordinated group).
- **Why AI can't copy it:** a clone has the code but not the network. Vollset (836), Eden, the How I Invest podcast, NFX and Walling ("everyone's already in the software" [29:53]) all keep network effects.
- **Risks:** hard to bootstrap; not available to most single-player tools.

### 9. Capital-heavy infrastructure and hardware coupling
- **What:** physical or capex-heavy assets (DNS, payments, hardware plus software).
- **Why AI can't copy it:** "CapEx is still a moat" (Eden [6:17]); hardware–software coupling is acquirers' moat #1 (Vollset, 836).
- **Risks:** irrelevant for most course participants; included for completeness.

## Tactical hardening (useful, but not moats)

From [notes/06-tactical-anti-copy-methods.md](notes/06-tactical-anti-copy-methods.md). These slow a copier down; none of them stops one.

| Tactic | Honest rating |
|---|---|
| Keep prompts and business logic server-side; authorise outside the LLM (OWASP LLM07: prompts are not secrets) | Security hygiene; weak as anti-clone |
| Rate limits, anomaly detection, verified accounts, a ToS clause against distillation (Anthropic's Feb 2026 distillation post) | Moderate, only for API-exposed products |
| Private labelled eval set and trace logging | Moderate to strong; it feeds moat #1 |
| Bot blocking / pay-per-crawl for proprietary content (Cloudflare) | Weak unless content is the product |
| Ship faster than the copier | Weak alone; buys time to build moats 1–5 |
