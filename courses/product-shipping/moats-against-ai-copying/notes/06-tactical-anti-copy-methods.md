# 06 - Tactical anti-copy methods (research notes)

Scope: tactical methods (not strategic moats) that make an AI product, or a product built with AI, harder to clone.
Access date: 2026-11-13. Quotes are from fetched page text. Anything not quoted is paraphrase.

---

## 1. Someone to Blame: SaaS Moats From the Buyer's Chair

- URL: https://paddo.dev/blog/someone-to-blame/
- Author/org: not stated (personal blog, paddo.dev)
- Date: November 3, 2026 (per page)
- Access: loaded (WebFetch)

**Thesis:** AI erodes feature and build-difficulty moats. For large customers who already own their data and
integrations, the vendor's value is running the system reliably and absorbing responsibility when it fails.

| Claim | Evidence | Short quote (<=25 words) | Keep/discard | Why |
|---|---|---|---|---|
| Accountability for failure is part of what is bought | One buyer's enterprise purchase | "Your moat is whatever is left after that week: your run team, and your willingness to be the one they blame." | Keep | Essay, single experience; framing, not measured |

**Method:** Make responsibility a product feature: named run team, incident process, SLA, postmortems shared with customers.
- Small team: publish SLA response times, name a human contact per account, sell an operations-ownership tier.
- Limits: a sales and operations moat, not a technical block. A copycat can offer the same SLA.

---

## 2. Trying to Compete Against AI-Native Solutions? Why Integrations Are Your Moat in 2026

- URL: https://www.pandium.com/blogs/trying-to-compete-against-ai-native-solutions-why-integrations-are-your-moat-in-2026
- Author/org: Cristina Flaschen, CEO, Pandium (vendor blog; sells embedded integration infrastructure)
- Date: first published Feb 20, 2026; updated Aug 19, 2026
- Access: loaded (WebFetch)

**Thesis:** AI makes features easy to copy; deep integrations embedding the product in customer workflows are more durable.

| Claim | Evidence | Short quote (<=25 words) | Keep/discard | Why |
|---|---|---|---|---|
| Integrations are harder to copy than features | Assertion | "AI-native tools are eroding feature moats, but they can't replace robust integrations that deeply embed your product into customer workflows" | Keep (low weight) | Vendor opinion; plausible mechanism |
| Procedural switching costs (retraining, workflow change) | Asserted, no figures | paraphrase | Keep | Checkable in a customer's own workflow |
| 51% of buyers cite poor integration; integrated customers churn less | Chained to Mixology Digital and TechnologyRadius (via Dev.to) | paraphrase | Discard | Secondhand chain of citations |
| ShipBob: 6x faster integrations, 70% less eng time, $200k saved | Vendor's own case study | paraphrase | Discard | Marketing |

**Method:** Write back into a system of record the customers already use (CRM, ERP, ticketing), not a read-only import.
- Small team: pick one system of record; build two-way sync with conflict handling; make the product's data live there.
- Limits: integrations are buildable with AI tools too (the article's own premise). Depth costs ongoing maintenance (API changes, auth, rate limits).

---

## 3. Detecting and preventing distillation attacks

- URL: https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks
- Author/org: Anthropic (no individual author; category "Security")
- Date: February 23, 2026
- Access: loaded (WebFetch)

**Thesis:** Named China-based labs (DeepSeek, Moonshot, MiniMax) ran large-scale distillation of Claude via fraudulent accounts; Anthropic describes API-side detection.

| Claim | Evidence | Short quote (<=25 words) | Keep/discard | Why |
|---|---|---|---|---|
| Distillation at scale happened via the API | Anthropic's own telemetry | "These labs generated over 16 million exchanges with Claude through approximately 24,000 fraudulent accounts." | Keep | Primary, first-party; not independently audited |
| Illicitly distilled models lose safeguards | Company position | "Illicitly distilled models lack necessary safeguards, creating significant national security risks." | Keep (as position) | Advocacy framing |
| Behavioral fingerprinting classifiers on API traffic, incl. chain-of-thought elicitation | Described as deployed | paraphrase | Keep | Primary description of a real method |
| Stronger identity checks for education, security research, startup accounts | Described | paraphrase | Keep | Account verification as a lever |
| Cross-lab and cloud info sharing | Described | paraphrase | Keep | Frontier-lab mechanism, not small-team |

**Method (API-exposed products):** Detect and throttle systematic extraction.
- Small team: per-account and per-IP limits; flag bulk, templated, or sequential queries covering a wide input space; verified accounts for high-volume tiers; ToS clause against training competitors on outputs; review anomalies.
- Limits: matters only if raw model output is exposed at volume. UI-only products leak capability through the product, not the API. Detection is an arms race (account rotation). Clause enforceability is contested; the OpenAI ToS check below is secondary only.

---

## 4. LLM07:2025 System Prompt Leakage (OWASP)

- URL: https://genai.owasp.org/llmrisk/llm072025-system-prompt-leakage/
- Author/org: OWASP Gen AI Security Project
- Date: 2025 edition (exact date not checked)
- Access: loaded (WebFetch)

**Thesis:** System prompts are not secrets and not a security control. The risk is what they expose; authorization must sit outside the LLM.

| Claim | Evidence | Short quote (<=25 words) | Keep/discard | Why |
|---|---|---|---|---|
| Prompt text is not a secret | OWASP guidance | "the system prompt should not be considered a secret, nor should it be used as a security control." | Keep | Primary; answers the prompt-extraction question directly |
| Authorization must be outside the LLM | OWASP guidance | "Critical controls such as privilege separation, authorization bounds checks, and similar must not be delegated to the LLM." | Keep | Primary |
| Keep credentials/roles out of prompts; guardrails outside the LLM | OWASP guidance | paraphrase | Keep | Primary |

**Method:** Keep proprietary logic (scoring rules, retrieval, tool permissions) in backend code; check authorization in code before every tool call; alert on repeated extraction attempts.
- Limits: security hygiene, not an anti-clone moat. A clone can rebuild behavior from outputs (source 3). Protects data and permissions more than prompt text.

---

## 5. Your AI Product Needs Evals

- URL: https://hamel.dev/blog/posts/evals/
- Author/org: Hamel Husain (independent engineer)
- Date: March 29, 2024 (from secondary search results; not on fetched text)
- Access: loaded (WebFetch)

**Thesis:** Failing LLM products share one root cause: no robust eval system. Eval infrastructure doubles as debugging and fine-tuning infrastructure.

| Claim | Evidence | Short quote (<=25 words) | Keep/discard | Why |
|---|---|---|---|---|
| Failing products share one root cause | Author's consulting experience | "unsuccessful products almost always share a common root cause" | Keep | Primary essay; experience-based |
| Keep reading your data | Author's guidance | "You can never stop looking at data—no free lunch exists." | Keep | Supports trace logging |
| Pass rate is a product decision | Author's guidance | paraphrase | Keep | Primary |

**Method:** Private labeled set of real failure traces used as regression suite.
- Small team: log traces (with consent and data limits); binary good/bad labels; keep labeled set and rubric private; run on every prompt or model change; feed failures into retrieval or fine-tuning.
- Limits: a clone team can build its own evals. Value depends on real usage and domain labels. Essay is from 2024. A process advantage, not a hard barrier.

---

## 6. Regulatory framework for AI (European Commission)

- URL: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- Author/org: European Commission, DG CONNECT
- Date: undated in fetched text; states the Act "became applicable on 2 August 2026, with some exceptions"
- Access: loaded (WebFetch). Paraphrase only, no quotes taken.

**Thesis (paraphrase):** High-risk providers must run risk management, keep quality data, log activity, prepare documentation, enable human oversight, and monitor post-market. Annex III high-risk rules apply from 2 Dec 2027 (AI Omnibus); Annex I from 2 Aug 2028.

| Claim | Evidence | Short quote | Keep/discard | Why |
|---|---|---|---|---|
| Logging, documentation, oversight required for high-risk providers | Official summary | none (paraphrase) | Keep | Primary |
| Maximum penalty amounts | Page gives none; only "issue fines for non-compliance" | none | Discard as a figure | Not stated |
| Compliance as a moat | Not claimed by the Commission | none | Keep (weak) | Cost for every entrant, not copy protection |

**Method:** Classify risk tier early; if high-risk, build logs and documentation from the start and sell the evidence to regulated buyers.
- Limits: raises entry cost for everyone; relevant only for high-risk use cases. SOC 2 and HIPAA not researched in this pass.

---

## 7. Introducing pay per crawl (Cloudflare)

- URL: https://blog.cloudflare.com/introducing-pay-per-crawl/
- Author/org: Will Allen, Cloudflare
- Date: July 1, 2025 (page last-modified shown as July 15, 2026)
- Access: loaded (WebFetch)

**Thesis:** Content owners charge AI crawlers per request via HTTP 402 negotiation; crawlers can also be blocked outright.

| Claim | Evidence | Short quote (<=25 words) | Keep/discard | Why |
|---|---|---|---|---|
| Owners can monetize crawler access | Vendor product announcement | "we want to empower content owners to monetize their content at Internet scale." | Keep | Primary; vendor's stated goal |
| 402 with crawler-price / crawler-max-price headers; Block setting denies access | Documented mechanism | paraphrase | Keep | Primary spec-level description |
| robots.txt is ignored by some bots | Not on this page | none | Discard as a claim from this source | Only in secondary snippets |

**Method:** Put public content behind a CDN bot-management layer rather than relying on robots.txt.
- Small team: CDN with bot management; block or charge AI crawlers.
- Limits: only relevant if the product's value is public content. Pay-per-crawl was beta; a Sept 2026 "pay per use" change is unverified (secondary blogs only).

---

## Discarded sources

| Source | Reason |
|---|---|
| OpenAI Row Terms of Use, https://openai.com/policies/row-terms-of-use/ | HTTP 403 on fetch; clause not verified from primary. Search snippets (ITPro, conductatlas) paraphrase a no-competing-models clause. Not quoted. |
| GovInfoSecurity, "OpenAI tightens rules to block rival model distillation" | HTTP 403 on fetch; only search snippets. |
| "Scapegoat in the loop", https://blog-too-far.pages.dev/blog/2026/01/10/scapegoat-in-the-loop | Search snippet only, not fetched; overlaps source 1. |
| Hacker News on a Sept 2026 Anthropic follow-up, https://thehackernews.com/2026/09/anthropic-says-seven-china-based-ai.html | One secondary outlet; original Anthropic post not found. Unverified. |
| Hamel Husain via secondary summaries | Primary essay used; summaries overstate ("if you don't have evals, you don't have a product"), a paraphrase, not his wording. |

---

## Tactic summary (honest strength)

| Tactic | Strength against cloning | Notes |
|---|---|---|
| Private labeled eval set + trace logging (flywheel) | Moderate | Strongest for a small team; needs real usage |
| Write-back integrations with systems of record | Moderate | Real switching cost; source is vendor, stats unverified |
| Rate limits, anomaly detection, verified accounts, ToS clause | Moderate, API-exposed only | Frontier-scale methods; weak for UI-only products |
| Server-side logic and authorization | Weak as anti-clone, strong as security | Prompts are not secrets (OWASP) |
| Run team / SLA / accountability | Weak as anti-clone | Single essay; sales moat |
| Bot blocking / pay-per-crawl | Weak, scope-limited | Only if content is the product |
| EU AI Act compliance | Weak as anti-clone | Raises entry cost for all; high-risk only |
| Speed of iteration | Weak as anti-clone | Process advantage; copyable |

Gaps: SOC 2, HIPAA, and watermarking not researched. OpenAI ToS and the Sept 2026 Anthropic follow-up not verified from primary text.
