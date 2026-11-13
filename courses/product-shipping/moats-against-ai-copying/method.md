# Method appendix: orchestrator plus weak subagents

Required by the t3273u brief (AC3): a smart orchestrator searches, plans and synthesises, but never reads or watches full source content. Weak subagents read and watch the sources, filter them, and return short structured notes.

## Who ran what

- **Orchestrator:** Claude **Opus 5.5** (`claude-opus-5-5`) in Claude Code, a headless Hub session on hetzner-aplexer, run date 2026-11-13. Fable was not the runtime model for this session. Opus was the model the session was started on, and it filled the orchestrator role.
- **Subagents:** Claude **Haiku** (Agent tool, `model: haiku`, general-purpose type), the weakest Claude model the runtime could spawn. That matches the brief's Anthropic split, with a "Haiku" reader under a stronger orchestrator.

## What the orchestrator did and did not consume

**Did:**
- Ran three web searches, which returned titles, URLs and search-engine summaries.
- Tried `yt-dlp` metadata for the starting video; the YouTube bot check blocked it.
- Wrote the briefs and read the subagents' short replies.
- Read the claim tables and discard lists in `notes/` with grep and short excerpts, then wrote the synthesis files.
- Ran one keyword spot-check on the cached Hewitt transcript to verify the subagent's claim that "audience" is never said: `grep -c audience` returned 0, and two `copy` lines were printed. That was the only direct contact with any transcript.

**Did not:** open any full article, page dump or transcript.

## Subagent ledger

| # | Model / type | Assignment | Sources reviewed | Output | Kept / discarded |
|---|---|---|---|---|---|
| S1 | Haiku / general-purpose | Watch Alexey's starting talk | https://www.youtube.com/watch?v=8cSCJtPOkmM (full auto-transcript via fetch-youtube; title via Jina reader) | [notes/01](notes/01-microconf-primary-8cSCJtPOkmM.md) | Kept as primary source; several statistics in the talk discarded as unsourced |
| S2 | Haiku / general-purpose | Find the other MicroConf moat talk(s) | 81j1sV32Wng and msH7lUkWZAY (full transcripts); MicroConf channel listing; Gk05cd9XHAU, FlbAfgJ2umk, KxgomEbhWu0 (titles only) | [notes/02](notes/02-microconf-other-moat-talks.md) | Kept 81j1sV32Wng and msH7lUkWZAY; discarded Gk05cd9XHAU; did not review the other two |
| S3 | Haiku / general-purpose | MicroConf podcast episodes | SFTRFU ep 836, ep 842 (full transcripts on page); MicroConf On Air "7 Things" (show notes only) | [notes/03](notes/03-sftrfu-microconf-podcasts.md) | Kept 836 and 842; discarded "7 Things" |
| S4 | Haiku / general-purpose | Classic VC moat essays | a16z data moats; Greylock The New Moats; NFX AI defensibility; NFX data network effects; NFX manual (grep only); 7 Powers (failed) | [notes/04](notes/04-vc-moat-essays.md) | Kept a16z, Greylock, two NFX essays; discarded 7 Powers (not verified) and the NFX 70% stat |
| S5 | Haiku / general-purpose | Distribution, audience and brand | levels.io ×3; Andrew Chen ×2; Paul Graham; SaaS Club/Tibo; Lenny; Stratechery; Marc Lou; SEO listicles | [notes/05](notes/05-distribution-audience-brand.md) | Kept levels.io, Chen and PG; discarded Tibo (secondary), Lenny (empty), Stratechery (404), Marc Lou and listicles |
| S6 | Haiku / general-purpose | Tactical anti-copy methods | paddo.dev; Pandium; Anthropic distillation post; OWASP LLM07; Hamel evals; EU AI Act page; Cloudflare pay-per-crawl; OpenAI ToS (403); GovInfoSecurity (403) | [notes/06](notes/06-tactical-anti-copy-methods.md) | Kept seven; discarded the 403s, snippet-only and single-secondary sources |
| S7 | Haiku / general-purpose | Debate and counterviews | UjV0w0k_m90 (How I Invest, transcript); Foundation Capital; fpso; Danjou; tscsw; pulse.bot ×2; dealroom; paywalled pieces | [notes/07](notes/07-debate-and-counterviews.md) | Kept five; discarded aggregators, 403s and paywalled pages |
| S8 | Haiku / general-purpose | Rob Walling "10 attacks / 8 moats" talk and conference order | KpILHX2D-AA (transcript); SFTRFU ep 830; youtubesummary.com; paddo.dev; Cyberbase blog | [notes/08](notes/08-rob-walling-attacks-and-moats.md) | Kept KpILHX2D-AA and ep 830 (facts); secondary summaries used only as leads |
| S9 | Haiku / general-purpose | Gia Laudi's MicroConf US 2026 talk | FlbAfgJ2umk (full transcript) | [notes/09](notes/09-gia-laudi-gtm-moat.md) | Kept as a secondary moat talk; self-reported growth figures discarded |
| S10 | Haiku / general-purpose | Verify Walling's moat names against his transcript (S8 had relied on a secondary summary) | KpILHX2D-AA transcript | Appended to [notes/08](notes/08-rob-walling-attacks-and-moats.md) | Corrected six of eight moat names to Walling's own wording |

## Quality controls

- Each brief told the subagent never to invent quotes, to say when a page couldn't be opened, and to mark keep/discard with a reason.
- Where the orchestrator doubted a subagent's claim, it checked it: a keyword grep for S1, and the separate verification pass S10 for S8.
- Known limits:
  - Timestamps come from auto-captions (±a few seconds) and some names are garbled ("Interval Set").
  - YouTube upload dates are unverified because the bot check blocked yt-dlp.
  - The speaker of 81j1sV32Wng is not confirmed.
  - Haiku notes may still contain paraphrase errors. Check a quote against the video before putting it on a slide.
