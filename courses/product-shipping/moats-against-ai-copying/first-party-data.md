# First-party data deep-dive

The claim Alexey took from the MicroConf talk was that **the main moat is first-party data: your audience, and proprietary data that AI cannot see or copy**. This file tests that claim against the sources.

## What the talk actually says (Craig Hewitt, Castos, MicroConf US 2026 Portland)

From [notes/01-microconf-primary-8cSCJtPOkmM.md](notes/01-microconf-primary-8cSCJtPOkmM.md), a Haiku subagent's reading of the full auto-transcript:

- He ranks four moats and calls first-party data the best: "the best is first-party proprietary data" [24:48]. He means product data that improves over time.
- His Castos example is mostly about *state and switching cost*: "if you cancel with us, your podcast goes away" [26:26–26:34].
- The other three are **speed**, "maybe the universal advantage" [27:43]; **enterprise relationships**, "people always have bought from people" [28:21]; and **vertical focus**, "vertical way over horizontal" [48:57].
- The first-party data section is short, about 2.5 minutes, and the evidence is anecdotal.

**Corrections to the recollection:**
1. "Audience" is **not** named as a moat in this talk. The orchestrator grepped the transcript and found zero occurrences of the word. The audience argument comes from other sources: Walling's SFTRFU 842, levels.io, Andrew Chen, and Vollset's "brand and owned traffic" in SFTRFU 836.
2. He does not argue that AI "cannot see" proprietary data. He actually recommends feeding your data into AI tools. The "AI can't see it" framing is a fair synthesis (the Europe "sell the outcome" talk and SFTRFU 836 make it explicit), but don't attribute it to Hewitt.

The talk is fine to cite for "first-party data ranked #1 by a bootstrapped SaaS founder at MicroConf". It is not enough on its own to carry a course module.

## A stronger version of the claim

Combining the sources, first-party data is a moat only when **all four** of these hold. That four-point test is the orchestrator's synthesis.

| Test | Question | Source |
|---|---|---|
| **Unseen** | Is it absent from the public web, training data and competitors' reach? | SFTRFU 836: proprietary data "flows in but not out" |
| **Outcome-linked** | Does it record what *worked*, not just what was entered? | MicroConf Europe "Sell the outcome": a learning loop on real-world outcomes |
| **Compounding** | Does each new customer's data improve the product for all customers? | NFX "Truth About Data Network Effects" has a six-element test; a16z warns most of these are scale effects |
| **Sticky** | Is it expensive or risky to move, or does it lose its value outside your product? | fpso "Software Moats in the AI Age": data gravity; tscsw: exportable data doesn't protect the layer above it |

If any one fails, treat the data as an *asset*, not a moat.

## Two kinds of first-party data

1. **Audience data, relationships and customer understanding.** You know who your people are, what they ask and what they buy, and you can reach them without paying a platform: email list, community, YouTube subscribers, course alumni. AI cannot copy the relationship. It can copy content, but not the trust or the reachable list. This is the "distribution" moat ([moat-catalogue.md](moat-catalogue.md) #2). Qualitative insight belongs here as well: interviews that explain *why* customers buy (Gia Laudi, MicroConf US 2026: understanding customers "better than anyone else" is what compounds [28:52]).
2. **Product and outcome data.** Traces, corrections, accepted versus rejected outputs, results, and domain edge cases. These become your private eval set, your prompt and routing improvements, and your benchmarks. This is the "learning loop" moat (#1 and #4).

The strongest position for a small founder combines the two. The audience gives you early users, those users generate outcome data, the data makes the product better than a clone, and the better product gives you more to talk about with the audience.

## Counterarguments to teach honestly

- **"Data is not inherently valuable"** (NFX). **"There generally isn't an inherent network effect that comes from merely having more data"** (a16z, 2019).
- **Incumbents are advantaged on their own data** (Greylock "The New Moats", 2023 text). A small founder rarely out-datas an incumbent; the realistic path is out-niching them.
- **Exportable data doesn't protect you** (tscsw): "As long as you can export the data, the analytical layer above the system of record is increasingly commoditised."
- **Eden (MicroConf US 2026, the same Portland conference as Hewitt)** lists "proprietary data and knowledge" among the *previous* SaaS moats [1:59–2:04] and adds that "not all those are defensible" [2:28]. He keeps network effects, regulation, operational excellence and capex instead. That makes for a useful on-stage disagreement with Hewitt's ranking.
- **Raw data volume doesn't matter** (Walling, MicroConf Europe 2026): "If you have a lot of data, doesn't matter" [32:15]. He moves the moat to the cross-customer *learning loop* [31:25].
- **SaaS-era data moats no longer work** (How I Invest podcast, UjV0w0k_m90). The speaker there keeps network effects and counter-positioning instead.

## Practical checklist for course participants

1. List every piece of data your product will generate. Mark each one as public, user-exportable or unseen.
2. For each core action, capture the *outcome* (accepted, edited, rejected, result), not just the input.
3. Start a private eval set from real traces in week 1 of usage.
4. Write down how next month's product will be better because of this month's data. If you can't, it isn't a moat yet.
5. Separately, list your owned audience channels and their size. Pick the one you will grow during the course.
