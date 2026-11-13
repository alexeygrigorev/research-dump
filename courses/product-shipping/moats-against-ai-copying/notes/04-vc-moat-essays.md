# VC moat essays: notes

Fetched 2026-11-13 via `curl -sL https://r.jina.ai/<url>`. Quotes are verbatim from fetched text, each under 25 words.

---

## 1. a16z, "The Empty Promise of Data Moats"

- **URL:** https://a16z.com/the-empty-promise-of-data-moats/
- **Author:** Martin Casado and Peter Lauten per the brief; byline not visible in fetched text, verify on page.
- **Date:** 2019-05-09 (page metadata)
- **Access:** Opened, full text.

**Thesis.** "Data network effects" are mostly data scale effects, and scale effects weaken as the corpus grows: unique data gets costlier and each new datum is worth less. Data is not a moat by default. Founders who treat it as one underinvest in verticalization, GTM, account control, and brand.

| Claim | Evidence | Short verbatim quote | Keep/discard | Why |
|---|---|---|---|---|
| Data alone rarely creates a true network effect. | Definition: network effects need direct interaction between nodes. | "There generally isn't an inherent network effect that comes from merely having more data." | Keep | Core distinction. |
| Data scale effects erode with size. | Eloquent Labs chatbot study; intent coverage asymptotes near 40%. | "after 40% of the queries have been collected in this case, there is actually no advantage to collecting more data at all!" | Keep | Concrete, but single domain. |
| Data scale can weaken a moat. | Same curve. | "Instead of getting stronger, the data moat erodes as the corpus grows" | Keep | Counters the flywheel story. |
| Data commoditizes and goes stale. | Freshness argument; competitors chase same domains. | "Data, in this sense, is like a commodity." | Keep | Matters most for fast-changing domains. |
| Proprietary data can be defensible when sources are scarce or reluctant. | Pharma; Equifax, LexisNexis, Experian; government buyers. | "Accumulating proprietary data is a defensible strategy that is strongest when the sources are scanty" | Keep | The essay's conditional case for data. |
| Trusted custody of sensitive data is a moat. | Customers share more sensitive data only with proven custodians. | "Startups that prove to be responsible data custodians can earn trust from their customers" | Keep | Ties to compliance and trust. |
| Minimum viable corpus is cheap to bootstrap. | Synthetic data, transfer learning, crawling. | "Bootstrapping what we think of as the 'minimum viable corpus' is sufficient to start training against" | Keep, qualified | Early data advantage is not hard to get. The "beat incumbents" anecdote is unnamed; do not cite it as fact. |
| Better defensibility comes from elsewhere. | Concluding list. | "Greater long-term defensibility is more likely to come from packaging differentiated technology" | Keep | Feeds the "what else to build" section. |

**Moats and how to build them:** scarce or sensitive proprietary data; verticalization with scar tissue from complex markets; GTM dominance; post-sales account control; brand; talent.

**Counterpoints to "data is the moat":** scale effects are weaker than network effects; marginal data value falls and acquisition cost rises; data goes stale; competitors bootstrap cheaply; algorithm and product choices often matter more.

**Limits:** 2019, enterprise, pre-foundation-model. One domain's curve.

---

## 2. Greylock, Jerry Chen, "The New Moats" (2017) / "New New Moats" (2023)

- **URL:** https://greylock.com/blog/the-new-moats/ (fetched via https://greylock.com/greymatter/the-new-moats/, which redirects there)
- **Author:** Jerry Chen per the brief; first-person text consistent with that.
- **Date:** Metadata reads 2017-04-24, but the body is the 2023 revision ("Six years ago I published..."; mentions GPT-4, LLaMA, LlamaIndex, Langchain).
- **Access:** 2023 revision opened, full text. The original 2017 text was **not** separately fetched. The title "New New Moats" is not on the page; refer to it as the 2023 revision.

**Thesis.** Open-source models push value toward the application layer, and deep tech alone is a shallower moat. Platform shifts can preserve incumbents without making them thrive. The durable moats are the old ones: systems of record, workflow lock-in, switching costs, brand, and GTM. "The new moats are the old moats."

| Claim | Evidence | Short verbatim quote | Keep/discard | Why |
|---|---|---|---|---|
| Open source moves value to the app layer. | Linux/Android analogy; LLaMA ecosystem. | "where value accrues in the stack." (the essay frames the question as "of where value accrues in the stack") | Keep | Frames where to look for moats. |
| Deep-tech IP is a shallower moat. | Oracle vs. open-source databases and cloud services. | "In an era of cloud and open source, deep technology attacking hard problems is becoming a shallower moat." | Keep | Limits the "we have better tech" defense. |
| Thin model wrappers are at risk from the model vendor. | Jasper vs. OpenAI. | "run the risk of facing direct competition from the foundation model provider" | Keep | Direct support for "cheap to copy." |
| Systems of record are the durable base layer. | CRM, HCM, ERP; Salesforce replaced Siebel. | "If the data and app power a critical business function, it becomes a 'system of record.'" | Keep | Concrete definition for the course. |
| Foundation models do not replace systems of record. | Argument on LLMs as cross-record tools. | "Foundation models do not replace existing systems of record" | Keep | Own the record, not the model. |
| Incumbents keep an edge on their own data. | Salesforce Einstein example. | "Incumbents will be advantaged on their own data." | Keep | Data is a moat only where you cross silos. |
| Customer experience and workflow defend a product. | Full-stack argument. | "companies that build great customer experiences may find defensibility through the workflow of their software." | Keep | Ties to workflow lock-in. |
| Trust is a moat in AI. | Hallucination examples. | "Trust is essential in AI – and for many populations, it hasn't been earned yet." | Keep | Supports brand/trust. |
| Surviving a platform shift is not thriving. | Mainframe persistence; x86 passed mainframe revenue in 2009. | "Strong moats help companies survive through major platform shifts, but surviving should not be confused with thriving." | Keep | Warning for data-rich incumbents. |

**Moats and how to build them:** economies of scale (flat core engineering); network effects (developer ecosystems, "where the customers and the data are"); deep IP (few substitutes, hard engineering, operational knowledge); switching costs (standardization, integrations, entrenched workflows); brand; systems of record and engagement; systems of intelligence (cross-silo data plus AI, verticalized).

**Counterpoints to "data is the moat":** incumbents hold their own data; startups must combine silos; a foundation model does not replace the record; trust and workflow may matter more than volume.

**Limits:** VC thesis, light on evidence. The 2023 text is partly predictive.

---

## 3. NFX

### 3a. "How AI Companies Will Build Real Defensibility" (most relevant)

- **URL:** https://www.nfx.com/post/ai-defensibility
- **Author:** not in fetched text; verify.
- **Date:** 2025-07-10 (metadata)
- **Access:** Opened, full text.

**Thesis.** AI makes building products cheap, so speed to scale is the primary early lever. Build a "bailey" of fast advantages (distribution, scaling, brand), then a "motte" of durable ones (true network effects, workflow embedding, lock-in) as competition rises. Data gives an early edge, with limits.

| Claim | Evidence | Short verbatim quote | Keep/discard | Why |
|---|---|---|---|---|
| Speed is the main early lever; defensibility layers over time. | Motte-and-bailey; Google's sequence (data, distribution, network effects, embedding). | "Speed to scale is your primary lever, but you have to be constantly building for the future." | Keep | Gives a sequencing model. |
| Data gives an early edge. | Listed as "to some extent, data moats." | "Access to large scale or proprietary data will give you an early edge" | Keep | Middle position. |
| Data network effects have limits; real-time data is the differentiator. | Cross-reference to NFX data essay. | "(A key differentiator is real-time data.)" | Keep | Only place this essay names what makes data hard to copy. |
| Workflow embedding is a strong AI tactic. | EvenUp in personal-injury workflows. | "Embedding into a workflow is becoming a strong tactic for many AI startups." | Keep | Supports system-of-record / workflow moat. |
| Brand matters more now. | Similar features; hallucination and privacy concerns. | "Once considered a weaker defensibility, brand has become paramount" | Keep | Brand as moat. |
| Groupon-style virality is not a network effect. | Groupon case. | "What looked like a network effect was actually just virality disguised" | Keep | Caution for growth-driven "network effects." |
| Collaborative context and memory create switching costs. | Team-memory example (Cursor, unverified detail). | "Memory within AI systems... has become a common form of defensibility." | Keep | Gives the switching-cost and collaborative-value tests. |

**Tests proposed:** Switching Cost Test ("What happens if I stop using this product?"); Collaborative Value Test; Hub-and-Spoke Test.

**Moats:** distribution and speed (bailey); brand; network effects (collaborative value, hub-and-spoke); limited data; embedding and workflow lock-in; scale.

### 3b. "What Makes Data Valuable: The Truth About Data Network Effects"

- **URL:** https://www.nfx.com/post/truth-about-data-network-effects
- **Author:** not in fetched text; verify.
- **Date:** 2020-02-25 (metadata)
- **Access:** Opened, full text.

**Thesis.** Data is not inherently valuable. Data can serve three purposes: a true data network effect (value grows with usage), data scale (linear, asymptoting), or data embedding (switching cost). Only the first is a network effect, and it is rare.

| Claim | Evidence | Short verbatim quote | Keep/discard | Why |
|---|---|---|---|---|
| Data is not inherently valuable. | Pitch-meeting pattern. | "Data is not inherently valuable." | Keep | Core counterpoint. |
| Most data does not create a real network effect. | Own claim. | "Most data doesn't produce a real data network effect, and most data network effects aren't that powerful" | Keep | Direct. |
| Six-element test for real data network effects. | Waze as the example (automatic capture, central value, high threshold, non-asymptotic value, etc.). | "Data capture from customer usage is automatic" | Keep | Checklist for the course. |
| Scale effects are weaker. | Yelp and Amazon examples. | "Scale effects are linear and asymptote quickly" | Keep | Matches a16z. |
| Early insights flatten out. | Diagnosis example: 2,500 vs. 20,000 cases. | "most of the valuable insights you will glean from a scaled-up dataset in a particular domain will come early on." | Keep | Matches a16z asymptote. |
| Data embedding raises switching costs without being a network effect. | SaaS client-data example. | "the more data you hold for them embedded in their operations, the harder it would be to remove you" | Keep | Key for workflow-embedded data. |
| Founders overestimate their data's value. | Author's own Tickle experience: 150M users, 24B answers. | "a large company might be spending $3 billion on annual advertising, but only $30 million for research data." | Keep | First-hand evidence. Attribute to the author. |

**Moats:** data network effect (automatic capture, central value, high threshold); data scale (1-3 early insights); data embedding (client data inside operations).

**Counterpoints:** competitors can get similar data or claim similar value with less; data treadmills (CoStar, Abacus, Waze) need continuous refresh.

### 3c. "The Network Effects Manual: 16 Network Effects (And Counting)"

- **URL:** https://www.nfx.com/post/network-effects-manual
- **Date:** 2021-06-25 (metadata). **Access:** Opened; data section found by grep, not read in full.

| Claim | Evidence | Short verbatim quote | Keep/discard | Why |
|---|---|---|---|---|
| Network effects are the top digital defensibility. | NFX's claim. | "Network effects are the #1 way to create defensibility in the digital world." | Keep, attribute to NFX | Anchors the network-effects vs. data debate. |
| Network effects produce about 70% of tech value since 1994. | NFX's self-run study (linked separately, not opened). | Summarized only | Discard as a headline stat | Self-reported, not verified here. |
| Data network effects are a named category. | Section on data network effects. | Summarized only | Keep | Taxonomy source. |

---

## 4. Hamilton Helmer, "7 Powers" applied to AI

- **Primary source:** 7powers.com failed to load (`ERR_SSL_VERSION_OR_CIPHER_MISMATCH` via r.jina.ai). No primary Helmer AI essay or interview was opened.
- **Secondary search results (not opened, summaries only):** Lightcone podcast "The 7 Most Powerful Moats For AI Startups" (YC, Oct 2025); Lenny's Podcast Helmer transcript (glama.ai mirror); Nauta Capital "gen ai defensibility"; a Substack "7 Powers Framework Revisited."
- **Status:** optional source; no Helmer quotes used.
- **Framework (general knowledge, unverified against a fetched source):** Helmer's *The Seven Powers* (2016) lists scale economies, network economies, counter-positioning, switching costs, branding, cornered resource, and process power.
- **Next step:** open the Lenny's Podcast transcript or the Lightcone episode and extract quotes from there.

---

## Cross-source takeaways

| Moat | a16z 2019 | Greylock 2023 | NFX 2020-2025 | Verdict |
|---|---|---|---|---|
| Proprietary data | Only if scarce or sensitive | Incumbents' own data wins | Early edge, limited; real-time differentiates | Conditional keep |
| Data scale | Erodes | Not the moat | Linear, asymptotes | Discard as default |
| Data network effect | Rare | Not named | Six-element test | Keep as a test |
| Systems of record / workflow | Not focus | Strongest | Embedding is strong | Keep, strongest |
| Network effects | Not focus | Still a moat, weakened by open source | Strongest in digital | Keep, with tests |
| Distribution | GTM | GTM still required | Early speed lever | Keep |
| Brand | Named | Trust matters | Paramount | Keep |

## Access log

| Source | Result |
|---|---|
| a16z | Opened |
| Greylock | Opened (2023 revision); 2017 original not fetched |
| NFX manual | Opened (data section via grep) |
| NFX AI defensibility | Opened |
| NFX data effects | Opened |
| 7powers.com | Failed (TLS) |
| Helmer AI material | Search summaries only |
