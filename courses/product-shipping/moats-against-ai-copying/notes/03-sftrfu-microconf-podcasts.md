# Notes 03: Startups for the Rest of Us / MicroConf podcast pages on AI moats

Topic: how to defend a software/AI product against being copied with AI; which moats survive.
Method: fetched via `curl -sL https://r.jina.ai/<url>`. Quotes are from the served text; timestamps are the transcript's own.

---

## Source 1: Episode 836, "The 5 A.I. Moats Acquirers Value Most"

- URL: https://www.startupsfortherestofus.com/episodes/episode-836-the-5-a-i-moats-acquirers-value-most
- Show: Startups for the Rest of Us (Rob Walling)
- Speakers: Rob Walling (host); Einar Vollset (founder/principal, Discretion Capital; TinySeed partner; author of a sell-side M&A guide for B2B SaaS at $2M-$20M ARR)
- Date: published 2026-06-09; recorded 2026-05-15 (per transcript)
- Available: full transcript (Jina). No separate show notes read.

**Thesis:** Buyers (mostly PE, some strategics) now screen SaaS for AI-resistant moats. Five named moats are the filter. If a company has none, some PE firms will not take it to investment committee. Sentiment is "risk off" in public and private markets, but operating reality in TinySeed portfolio is strong.

### Claims table

| Claim | Example / evidence | Short verbatim quote | Verdict | Why |
|---|---|---|---|---|
| Five AI moats are what SaaS acquirers screen for in 2026 | Discretion Capital deal flow; Vollset's TinySeed Slack post | "the five AI moats that SaaS acquirers are looking for in 2026" (Rob, intro) | Keep | Core framework; anecdotal, but the only one on the topic from a deal-side source |
| Buyers now ask "will AI zero this out?" | Buyer diligence questions, 2026 | "how do we know this business isn't going to zero because of AI?" (Vollset, ~10:22) | Keep | Describes the actual question the moats answer |
| Some PE firms will not look at a company with none of the five moats | Repeat-buyer hurdles; Vollset's Slack thread | "if a company has none of these five moats, they won't even show it to their investment committee" (Rob, ~27:28) | Keep, caveat | Second-hand from buyers; Rob: "some PE firms are saying this, not all" |
| Integrations alone are no longer a moat (unless hard to get) | Ease of building integrations | "I think integrations in and of themselves are no longer a moat just because it's so much easier to build them." (~15:00) | Keep | Narrows Rob's earlier SaaS Playbook moat list |
| Unique features are a false moat | Rob's SaaS Playbook point | "And then I had a false moat, even at that point, which was unique features." Vollset: "That's not a thing anymore." (~15:39) | Keep | Agrees with source 2 |
| Brand and owned traffic channels still strong moats | Vollset's view; AEO vs SEO disruption noted | "I still think brand is a strong moat. I actually think owned traffic channels are also kind of a strong moat still." (~15:00) | Keep, caveat | Vollset concedes SEO disruption is real, "but it's correlated" |
| Two-sided marketplaces are very hard to bootstrap | Rob: he knows ~2 bootstrapped successes; Dynamite Jobs as exception (had access to one or both sides) | "It's hard to do, but hard to undo if you succeed at it." (Vollset, ~18:01) | Keep the qualitative point; discard numbers | Rob's "approximately 0% chance" is hyperbole, not data |
| Proprietary data is a moat only if it flows in and not out | Examples: BuiltWith, Fiscal.ai, DealForma, a TinySeed company | "The data has to flow in but not flow out." (Vollset, ~21:48) | Keep | Core of moat 4; Crunchbase rejected as example by Vollset |
| Snapshots of data are worthless without ongoing refresh | DealForma reasoning | "even if you took a snapshot, what good is that tomorrow?" (~23:00) | Keep | Explains why "continuously refreshed" matters |
| Switching cost = risk, not price | Rob's $10k vs $8k vs $5k example | "It's not just about price." (Rob, ~25:00) | Keep | Key reason cheap clones do not win system-of-record buyers |
| Vibe-coded or self-hosted replacements break and eat time | Vollset cites people abandoning an open-source agent setup | "It breaks all the time. I spend more time fixing it than getting productivity out of it." (~26:59) | Discard as evidence, keep as color | Anecdote from Twitter; no data |
| AI-native SaaS faces higher buyer hurdles | Zyra Talk (AI voice receptionist for HVAC): strong metrics, ~22-23 management meetings, no PE LOI, sold to Evercommerce (strategic) | "not a single one of the private equity firms even put in an LOI." (~31:00-32:08) | Keep, caveat | One deal, Discretion's own; one PE firm's AI fund "went to zero within a year" is also anecdote |
| PE is slower to adopt new risk sentiment | Vollset's 2022 experience | "private equity tends to be much more risk averse than people think, and also a little slower to react." (~32:08) | Keep | Explains why buyer hurdles lag; not a moat claim |
| Buyer hurdles rising is the signal of risk-off sentiment | Repeat-buyer pattern from 2022 and 2026 | "you can tell when you see repeat buyers putting higher and higher hurdles up before even looking." (~27:54) | Keep | Useful as a leading indicator for founders |
| Multiples are an auction; "4x or 15x" range | Vollset/Rob discussion | "it's an auction." (Rob, ~28:32) | Discard | Valuation context, off-topic for defense |
| $1M/$2M ARR and NRR/GRR thresholds | 2021 vs 2026 filters | "right now it's probably more like two million than one million" (~07:38) | Discard | Exit-threshold context, not moats |
| "Software is software" framing | Vollset | "this is still software" (~10:34) | Discard | Restates the thesis without evidence |

### Each moat, with how to build it

1. **Hardware-software coupling.** Replacement is not an API swap; physical downstream effects. Build: put your software in a device or physical process the buyer depends on. Examples cited: grocery scales, EV chargers ("Software that runs in the charger"), a printer at warehouse sites. Vollset: "This is the one I know the least about." Note: the investment was seen as a minus at first (~17:25).
2. **Marketplace scale / two-sided network effects.** Build: start with one side of the market already in hand. Rob: bootstrapping one from zero is nearly impossible; Dynamite Jobs had access to one or both sides. Once it scales, sellers do not leave ("They're hard to work with. But sellers don't change because that's where all the buyers are.", ~18:55). Note: Vollset says it may be the moat for existing marketplace features.
3. **Communication graph / relationship embed.** The product is where coordination happens: messages, approvals, shared context, conversation state. Build: make the product the system of record for coordination, not a single-user tool. Vollset: "The various states of the conversation, all that kind of thing is on the platform, and that just makes it a lot harder to move off." Example: Slack (~21:17).
4. **Proprietary data with closed feedback loops.** Build: capture data that is continuously refreshed and that you can use to improve the product, and do not expose a full export (including timestamps) via API. Vollset: "the incentives are now for companies to not give you access to even your own data through an API." Examples: BuiltWith (scraping, constantly refreshed), Fiscal.ai, DealForma, a TinySeed company.
5. **Operational embed and switching costs.** Build: be the system of record for finance, warehousing, approvals, shipping, etc., plus trust and responsiveness. Vollset: "You're never getting that with something you vibe coded at home." Rob: switching cost is "the pain and the retraining and what if stuff goes wrong."
6. **Brand and owned traffic (from brand discussion; not in the five).** Vollset keeps both as strong moats. Build: brand trust and owned SEO/AEO channels; watch AEO vs SEO shifts.

### First-party data and audience mentions

- Vollset: Discretion Capital (sell-side M&A, $2M-$20M ARR); TinySeed portfolio of 200+ companies; "I've never seen the sentiment be so different" between founder Slack and public markets (~12:11).
- Zyra Talk process: ~22-23 management meetings, no PE LOI (Discretion first-hand deal data, ~31:00).
- Vollset's book: "The Definitive Guide to M&A for B2B SaaS Between Two and 20 Million of ARR" at discretioncapital.com/guide.
- Rob's MicroConf content vault: 400+ talks (intro, not moats-specific).

### MicroConf 2026 talks on moats

None named. Mentions in episode: Jason Cohen's keynote on breaking growth ceilings (MicroConf Portland; not moats); Jim Zardakis, Connect Live on onboarding (not moats).

---

## Source 2: Episode 842, "What is the Future of SaaS in an AI World?" (Rob Solo)

- URL: https://www.startupsfortherestofus.com/episodes/episode-842-what-is-the-future-of-saas-in-an-ai-world-rob-solo
- Show: Startups for the Rest of Us (Rob Walling; solo episode)
- Speakers: Rob Walling only
- Date: published 2026-07-21
- Available: full transcript (Jina). Served text has no timestamps; one stray "(10:29):" artifact. Quotes are near-verbatim.

**Thesis:** "The future of SaaS is SaaS." Four claims that SaaS is dying (self-hosting custom apps; anyone can clone an app in a day; agents replace everything; infinite competition) do not hold. Non-copyable assets are distribution, brand, market ownership, trust, data safety, and support. Code or features alone are false moats. The real squeeze is on big incumbents and single-feature utilities, which is an opening for small bootstrapped companies.

### Claims table

| Claim | Example / evidence | Short verbatim quote | Verdict | Why |
|---|---|---|---|---|
| Self-hosting custom apps replaces SaaS | Rob's 50+ subscriptions (MicroConf, TinySeed); cost math | "Who in their right mind is going to AI code and host 50 SaaS apps?" | Keep | Clear reasoning: only two legitimate reasons (save money if expensive; customization) |
| Savings from building in-house rarely justify it | $1,000 MRR growth = $12k ARR = $60k-$120k at 5x-10x | "Building to save money is a rounding error." | Keep, caveat | Multiples (5x/10x) are Rob's assumption; the logic is the point |
| Self-hosting is a small-company edge case | Dentist, YMCA, gym examples | "This is not 80% of companies." | Keep the direction; discard the percentages | The "some people" share is unquantified |
| Anyone can clone your app in a day; cloning is not the hard part | Drip had clones from month five; Rob's own companies copied | "Cloning the software was never the hard part." | Keep | Matches source 1's "unique features = false moat" |
| AI writes code, not distribution | Rob's general point | "AI writes the code. It does not write your distribution." | Keep | Core line; the strongest single sentence in the episode |
| The moat was never the code | Rob cites SaaS Playbook (four years earlier) | "The moat was never the code. It was everything you added to the code." | Keep | Core thesis |
| Agents will absorb thin workflows | Thin layer moving data from A to B | "If the product was the workflow, meaning a thin layer moving data from A to B, an agent might eat it." | Keep | Concrete risk test for products |
| Agents need SaaS as a system of record | Dentist's agent needs patient data, billing, compliance | "They actually increase the demand for good APIs" | Keep, opinion | Plausible, not evidenced in the episode |
| Agents on top of SaaS, as subscription | Agent sold as part of the subscription | "The future to me is not agents instead of SaaS, it's agents on top of SaaS." | Keep | Product direction; no data |
| Infinite competition does not mean more companies | Vibe-coded ESPs/CRMs "drop off the face of the earth" | "More apps getting built is not going to mean more companies getting built because those are two different things." | Keep | Logic is sound; "vast majority will quit" is unsupported and discard |
| Consumer/prosumer and single-feature utilities will be hit hardest | PDF-to-JPEG, ZIP-to-RAR, HitTail-style SEO tool | "If your entire product is one feature, I think you're exposed." | Keep | Concrete exposure test |
| CRMs may take a big hit | Overpriced, want your own data | "maybe it is CRMs that take a big hit" | Keep as speculation | Rob flags it as possible, not certain |
| Big incumbents are the real "SaaS apocalypse" target | Price hikes, bloat, quarterly growth pressure | "The real SaaS apocalypse is the big companies, the big incumbents." | Keep, caveat | Opinion; the opportunity argument for bootstrappers |
| Table-stakes features will commoditize faster | General | "You can't coast on a feature list anymore." | Keep | Matches source 1 |
| Non-copyable: market, brand, distribution, trust, data safety, support | General | "Owning a market, a brand, a distribution channel, and the trust that you earned by being there for years and keeping data safe, answering support, building a customer base that loves you." | Keep | The episode's moat list; overlaps source 1 |
| Critics of "SaaS is dead" are not credible sources | "80, 90 plus percent" never built a SaaS company | "I wouldn't be surprised if 95% of them have never built any company." | Discard percentages | Unsupported numbers; tone, not evidence |
| Drip's competitors came from month five | Rob's own history | "With Drip, we had competitors from, I don't know, month five after we launched." | Keep as illustration | Anecdote |
| "I've been saying this on the show for 16 years" | Authority appeal | n/a | Discard as evidence | Not evidence |

### Each moat, with how to build it

1. **Distribution** (the main one). Build: a channel you own and can keep (SEO, audience, sales motion). Rob: "Getting someone to know you exist, to trust you with their business, to switch off what they're already using and to stay for years is the hard part."
2. **Brand and reputation.** Build: years of trust; answer support; be a company, not a folder ("A clone with little or no distribution is a folder on someone's laptop.").
3. **Customer relationships and support.** Build: a customer base that loves you; respond to problems.
4. **Data safety and system-of-record role.** Build: be the durable, secure, accountable store agents need ("keeping data safe"). Agents "need a backend to act on."
5. **Market ownership and network** (from "owning a market" and "your network").
6. **Agent layer on top of your data.** Build: expose good APIs/CLIs/MCP and ship an agent inside your SaaS, possibly in the subscription.

Warning, not a moat: features, code, single-feature utilities, and "unique features."

### First-party data and audience mentions

- Rob: TinySeed and MicroConf run ~50 SaaS subscriptions between them (estimate, "maybe a hundred").
- Drip: competitors from month five. Rob has "been doing SaaS for almost 20 years."
- Rob's email list (robwalling.com/emails); listener question source.

### MicroConf 2026 talks on moats

None named. Announcements: MicroConf US 2027 (Austin, April 18-20, 2027; Early Bird on sale; promo code Rob50); MicroConf Connect live session with Harris Kenny (mindset/bias to action, with Tracy Osborn). Neither is about moats.

---

## Source 3: MicroConf On Air, "7 Things SaaS Founders MUST Prepare for in the Age of AI"

- URL: https://microconf.com/on-air-episodes/7-things-saas-founders-must-prepare-for-in-the-age-of-ai
- Speakers: not named on the page. Credited to "MicroConf" as author.
- Date: page shows "Oct 25"; metadata published 2023-10-25. Predates the 2026 sources by about 2.5 years.
- Available: **show-notes blurb only.** The page does not include a transcript and does not list the seven items. Jina output also carries cookie banners and nav noise.
- Not fetched: the linked YouTube video (youtu.be/n-XsTJv5kXs) and the two linked articles ("8 AI Nightmares..." and "What SaaS founders need to know about artificial intelligence"). Not in scope; a transcript would be needed to make claims.

**Thesis (from blurb only):** "How are you going to stay ahead of AI or build it into your SaaS business?" and "7 things SaaS founders should prepare for." Content of the seven items is unknown.

### Claims table

| Claim | Example / evidence | Short verbatim quote | Verdict | Why |
|---|---|---|---|---|
| (none verifiable) | n/a | "This video explores 7 things SaaS founders should prepare for..." | Discard | Blurb only; no claims to keep |

### Each moat, with how to build it

Cannot be determined from this page.

### First-party data and audience mentions

- Sponsor: Lemon.io's Lemon Hire (not relevant).
- Previous/next episodes linked; not read.

### MicroConf 2026 talks on moats

None mentioned on this page.

---

## Cross-source synthesis

- Agreement: code is not a moat; distribution, brand, trust, and switching costs (system of record) are. Source 1 (Vollset) frames this as buyer diligence; source 2 (Rob) frames it as a founder strategy.
- Agreement: "unique features" and "integrations alone" are weak moats.
- Tension: source 1 treats two-sided marketplaces and hardware as real moats but hard to build. Source 2 does not discuss them.
- Evidence quality: source 1 is deal-side and first-hand, but anecdotal (one-off deals, unnamed PE firms). Source 2 is opinion with examples and a reasoned rebuttal; no market data. Source 3 gives no usable content.
- Dates: both 2026 episodes are recent relative to the 2026-11-13 date; source 3 is from 2023.
