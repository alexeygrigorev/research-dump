---
name: podcast-guest-researcher
description: Discover, parse, synthesize, and visualize guest-agnostic podcast research for The Data Hustle, including source manifests, per-source extraction, strategy, questions, and interactive HTML artifacts. Fans out across sources with subagents routed to model and effort tier by source size and complexity.
---

# podcast-guest-researcher

Use this skill to research any podcast guest from a seed URL, name, profile, or prior source. The goal is not a shallow bio. The goal is a source-grounded research system that makes the guest look excellent, helps the host avoid repeated questions, and surfaces novel angles with strong social potential.

## Inputs from the calling prompt

- `GUEST_SEED` — URL, name, LinkedIn profile, personal site, or other initial source.
- `GUEST_SLUG` — filesystem slug such as `alexey-grigorev`.
- `RESEARCH_ROOT` — target folder, usually `guest_research/<GUEST_SLUG>/`.
- `HOST_CONTEXT` — show context, book/contextual theme, audience, and any do-not-ask constraints.
- `OUTPUT_MODE` — one or more of `discovery`, `extract`, `synthesize`, `html`, `questions`.

## Output folder contract

Create or update:

```text
guest_research/<guest_slug>/
  guest.yml
  discovery/
    source_candidates.jsonl
    source_manifest.yml
  sources/
    website/
    linkedin/
    youtube/
    podcasts/
    third_party/
  extraction/
    per_source/<source_key>.json
  synthesis/
    timeline.yml
    opinion_map.yml
    offering_map.yml
    research_gaps.yml
  strategy/
    host_brief.md
    question_bank.md
    guest_intro.md
  appearances/
    appearances_manifest.json
    appearances_analysis.json
    appearances_summary.md
    transcripts/<source_id>.txt
  search_index/
    chunks.jsonl
    corpus.jsonl
    research_index.sqlite
    suggested_terms.json
    suggested_topics.json
    dashboard_search.json
    README.md
  episode_architecture/
    podcast_episode_architecture.yml
    podcast_episode_architecture.md
    data_hustle_transcript_critique.md
    <guest_slug>_episode_arc.yml
  html/
    index.html
```

## Orchestration — subagents, models, and effort

This workflow is too big for one context. A full guest pass touches 30+ sources and ~300k words of transcript. Fan out, and pick the model per task by **complexity and size**, not by habit. Running everything on the top model burns budget on link-normalizing; running everything cheap loses the cross-source judgment that makes the research worth having.

### The routing rule

**Measure before you dispatch.** Never guess a source's weight — size it first, then pick the tier:

```bash
wc -w appearances/transcripts/<source_id>.txt
```

| Task | Size / complexity | Model | Effort | Batching |
|---|---|---|---|---|
| Query generation, surface planning | judgment, small output | opus | medium | one agent, before fan-out |
| Link harvesting per surface (YouTube, podcast dirs, web, GitHub, events) | mechanical, high volume | haiku | low | one agent per surface, in parallel |
| URL normalization, dedupe, manifest assembly | deterministic | — | — | **script it, no agent** |
| Transcript/page fetch, yt-dlp enumeration, API pulls | deterministic | — | — | **script it, no agent** |
| Per-source extraction — short | < 4,000 words (show notes, author/publisher pages, lightning talks) | haiku | low | up to 5 sources per agent |
| Per-source extraction — standard | 4,000–12,000 words (typical interview) | sonnet | medium | one source per agent |
| Per-source extraction — long or dense | 12,000–25,000 words, or heavy technical claims | sonnet | high | one source per agent |
| Per-source extraction — flagship | > 25,000 words, or the 2–3 sources that carry the episode | opus | high | split by time range, merge after |
| Output metrics (GitHub API, yt-dlp, word counts) | deterministic | haiku | low | one agent to drive scripts, verify totals |
| Cross-source synthesis (timeline, opinion map, contradictions, do-not-repeat list) | the actual hard part | opus | high | **single context, never split** |
| Strategy docs (host brief, question bank, guest intro, episode arc) | voice and judgment | opus | high–xhigh | single context, after synthesis |
| HTML dashboard build, subpage generation | mechanical, templated | sonnet | medium | one agent per section family |
| Search index build | deterministic | — | — | **script it, no agent** |
| Verification (HTTP, Playwright, breakpoints) | mechanical checks | haiku | low | one agent |

Reference distribution from the Alexey pass, for calibrating a new guest: 29 transcripts, 284,732 words total, median 9,355, max 21,443, only one source under 4k. Expect most sources to land in the sonnet/medium tier.

### Fan-out shape

1. **Discovery is loop-until-dry, not fixed-count.** Run the surface agents, dedupe against everything seen so far, and re-run only the surfaces that returned something new. Stop after two consecutive rounds with no new sources. A fixed "top 20" cap silently truncates the tail — and the tail is where the unasked questions live.
2. **Pipeline, don't barrier.** Each source should flow fetch → size → extract → per-source page without waiting for its siblings. The only true barrier is before cross-source synthesis, which genuinely needs every extraction at once.
3. **Cap concurrency at ~8–10 live agents.** Beyond that, fetches start failing on rate limits and the failures look like missing sources.
4. **One source per extraction context** (except the short-tier batch above). Mixing sources in one context blurs evidence and produces claims nobody can trace back.
5. **Scripts beat agents for anything deterministic.** Fetching, counting, indexing, and manifest-building should never consume a model call.

### Escalation and de-escalation

- Escalate a source to the next tier when the cheap pass returns thin extraction (< 5 timestamped moments for a video, no evidence quotes, or "unclear" confidence). Re-run once at the higher tier before accepting the result.
- De-escalate when a source turns out to be a duplicate upload, a re-cut of an existing talk, or a page that is mostly boilerplate — mark it in the manifest and skip the extraction entirely.
- If a hard second-pass discovery is requested ("try harder"), run the exotic surfaces (GitHub Search API, HN Algolia, Reddit JSON, Wayback CDX, package registries, speaker directories) on **haiku/low in parallel** — they are high-volume, low-judgment probes — then curate the raw hits in a single **sonnet/medium** pass before anything reaches synthesis.

### What must never be delegated cheaply

Cross-source synthesis, the do-not-repeat list, and the question bank are the deliverable. They depend on holding every source at once and noticing what nobody asked. Keep them in one opus context with full extraction output in view. If context is tight, drop raw transcripts and keep the per-source extraction JSON — never the reverse.

## Phase 1 — discovery first

Do not start with question writing. First find the source universe.

Run specialized discovery passes for:

1. Identity and owned media: canonical site, CV/about, newsletter/blog, GitHub, X, LinkedIn, email/contact, books, courses, projects.
2. LinkedIn: public profile, recent public post permalinks, company pages, articles. Mark auth-walled items as `manual_needed` rather than guessing.
3. YouTube/video: own channels, community channels, courses/playlists, talks, podcasts, conference appearances. Check whether captions/transcripts are available.
4. Podcast/audio: external podcast episodes, RSS pages, show notes, transcripts, YouTube equivalents.
5. Third-party web: publisher pages, GitHub orgs/repos, conference pages, course platforms, author pages, articles, communities, review/mention pages.

Write each candidate as JSONL:

```json
{"source_type":"youtube_video","url":"https://...","title":"...","confidence":0.95,"why_relevant":"...","access_notes":"transcript available"}
```

## Phase 2 — one parser per source

Parse one source at a time. Do not batch unrelated sources into the same analysis context. Each per-source extraction should capture:

- timeline events
- opinions and claims
- frameworks and how-to steps
- concrete results/numbers
- offerings, projects, books, courses, services
- prior questions already asked
- social hooks and quotable moments
- evidence quotes
- research gaps or uncertainty

Write each per-source result to `extraction/per_source/<source_key>.json`.

## Phase 3 — synthesis artifacts

Merge per-source extractions into:

- `timeline.yml` — chronological arc with dates, events, source keys, and evidence.
- `opinion_map.yml` — clusters of beliefs, tensions, contrarian angles, and source support.
- `offering_map.yml` — current offers and how to let the guest naturally talk about them without forced promotion.
- `research_gaps.yml` — missing private LinkedIn exports, unparsed podcasts, unverified numbers, or areas needing manual sourcing.
- `strategy/host_brief.md` — concise host-ready positioning and episode strategy.
- `strategy/question_bank.md` — novel, specific, non-generic questions with follow-ups.
- `strategy/guest_intro.md` — Data Hustle-style spoken intro, modeled on prior episode intros, with every factual claim backed by clickable numbered Markdown source links like `[(1)](https://...)`.

## Phase 4 — HTML visual artifact requirements

Always create `html/index.html` for review. It can be static, but it must feel like a usable research dashboard rather than a raw dump.

Required sections:

1. Hero with guest positioning and tags.
2. Best episode angles as skimmable cards.
3. **Sourced guest intro** — mandatory. Use Data Hustle intro style from prior transcript examples; include full and short versions with clickable numbered links `[(1)](...)`, `[(2)](...)` after sourced claims.
4. **External appearances tab** — mandatory when prior appearances matter for avoiding repeated questions. Search across YouTube, Google/general web, Spotify/podcast directories, conference/event sites, and other public sources; create one HTML subpage per source with the canonical URL at the top, a summary of what was said, what angle of the guest it shows, likely do-not-ask-again topics, and better uncovered follow-ups.
5. **Interactive vertical timeline** — mandatory.
6. Host brief.
7. Question bank.
8. **Episode architecture tab** — mandatory when interview-flow strategy is requested or prior show transcripts are available. Include major-podcast structure research, transcript critique, stronger question-flow rules, productive-controversy prompts, and a guest-specific episode arc.
9. **Output analytics section** — mandatory, in `html/index.html` itself, not only on a subpage. See the standard below.
10. Source candidate cards with canonical URLs.
11. Structured artifacts as YAML/JSON panels.

### Output analytics standard

Every guest gets a quantified footprint. Measure, don't guess, then derive. Write `synthesis/output_volume_metrics.{json,md}` and `synthesis/output_estimates.{json,md}`, render a full `html/metrics/index.html` subpage, and embed a condensed **Output analytics** section in the main dashboard with headline stat cards and inline-SVG charts.

Measure whatever applies to the guest:

- **GitHub** — `contributionsCollection` per year (commits, PRs, issues, repos created); `repositories(orderBy: STARGAZERS)` for stars/forks; `/repos/{o}/{r}/stats/contributors` per repo for lines added/deleted attributed to their login.
- **Video** — `yt-dlp --flat-playlist` over `/videos`, `/streams`, `/shorts` for counts and summed durations; channel follower count via `-J`.
- **Podcast/site/courses** — shallow-clone the community site repo and count content files, parse events YAML, list `cohorts/` dirs per course repo.
- **Writing** — word counts over cloned markdown/notebook corpora with code fences and frontmatter stripped; books estimated at ~300 words/page.

Rules:

1. Tag every figure **MEASURED** or **ESTIMATED**, and state the assumption inline for estimates.
2. Raw VCS churn is not "lines of code written". Publish a raw tier, a filtered tier with the filter rule stated (e.g. drop repos averaging >5,000 added lines per commit — the bulk-import signature), and a discounted hand-written range.
3. Flag mixed-authorship corpora and always offer a conservative floor the guest cannot dispute.
4. Convert big numbers into human equivalents (working days on camera, number of books, commits per day) and write ready-to-say on-air framings.
5. List what the numbers cannot show and turn it into an on-record question (real cohort enrollments, unrecorded live hours, cause of an output spike).

### Interactive vertical timeline standard

The timeline must be vertical and interactive, not just a static YAML/code block.

Minimum behavior:

- A vertical rail of dated milestone buttons.
- Clicking a milestone updates a detail panel with date, title, event, source tags, and interview angle.
- Active milestone is visibly highlighted.
- Detail panel uses `aria-live="polite"`.
- Milestones are real `<button>` elements, keyboard reachable.
- Arrow keys or Previous/Next controls should move through the timeline.
- On mobile, the vertical rail and detail panel collapse to a single column.
- Keep the raw `timeline.yml` visible later in the page for auditability, but never make it the only timeline representation.

Good timeline detail fields:

```json
{
  "date": "2018-2023",
  "title": "OLX production ML / MLOps",
  "event": "Senior to Principal Data Scientist at OLX; production image models, internal ML platform, and MLOps team.",
  "angle": "Best credibility bridge into production ML, platforms, and internal consulting.",
  "sources": ["website-cv", "yt-IxTyq96juVE"]
}
```

## Deep public-footprint/personality research

When the user asks for deeper personality research, expand beyond owned pages and obvious appearances. Search public LinkedIn posts/permalinks, GitHub repos/issues/READMEs, Kaggle, X/Twitter, Instagram, TikTok, Reddit/Hacker News, Stack Overflow, podcast directories, conference/event pages, books/articles/newsletters, course pages, and community references.

Rules:

1. Treat social platforms as **lead sources until verified**. Do not cite Instagram/TikTok/X handles unless cross-linked from an authoritative profile or the public page itself clearly identifies the guest.
2. For LinkedIn, try public post permalinks and regional LinkedIn mirrors, but record access limits. Full feed, comments, and reactions may be gated.
3. For GitHub, inspect repos, README files, public issues/comments, stars, update recency, and repeated project patterns. Extract personality/working-style signals with evidence, not vibes.
4. Create `deep_research/` artifacts:
   - `deep_source_manifest.json`
   - `personality_profile.md`
   - `personality_profile.json`
   - `linkedin_personality_analysis.md`
   - `github_personality_analysis.md`
   - `social_platform_gap_analysis.md`
   - `social_access_limitations.json`
5. Create a dashboard section/page for the deep personality pass and rebuild the search index so these sources are agent-searchable.
6. Explicitly list blocked/unverified platforms and the next manual/account-based steps.
7. If Tony says “try harder” or doubts coverage, run a hard second-pass discovery beyond ordinary search: GitHub Search API for issues/PRs/comments, HN Algolia, Reddit JSON where available, Wayback CDX, PyPI JSON, DockerHub API, package registries, SlideShare/SpeakerDeck profile archives, Kaggle profiles, owned-site path probes, podcast-directory search pages, event/speaker directories, and direct username probes. Curate noisy raw hits into `deep_research/hard_search_round*/round*_curated_source_manifest.json`, keep raw candidates separately, and label candidate/blocked/gated sources instead of citing them as facts.
8. Document future API-key upgrades separately: Tavily/Exa/Brave/Serper/SerpAPI for web search, Firecrawl/Jina Reader for extraction, Browserbase/Bright Data/Apify for JS-heavy public pages, and Proxycurl/People Data Labs/Apify/manual export for LinkedIn.

## External appearances research

When the user asks for appearance research, do not stop at the guest's owned site or the first few YouTube hits.

1. Search across multiple surfaces, not just one engine:
   - YouTube/video search for interviews, podcasts, talks, conference sessions, webinars, workshops.
   - Google/general web for show notes, written interviews, event pages, author profiles, conference/session pages, and third-party articles.
   - Spotify and podcast-directory surfaces such as Apple Podcasts, ListenNotes, Podchaser, PodcastAddict, RSS/show pages, plus YouTube equivalents when platform APIs are limited.
   - Technical/community/event sites relevant to the guest's niche.
2. Normalize candidates into `appearances/appearances_manifest.json` with source ID, title, channel/show/site, canonical URL, source kind, date/duration when available, transcript status, transcript path, and confidence/access notes.
3. Fetch transcripts or page text where available. Store source text under `appearances/transcripts/<source_id>.txt` or a clear equivalent path.
4. Analyze each appearance source-by-source. For every source capture:
   - summary of what was said
   - what angle of the guest this shows
   - what was already covered and should probably not be asked again
   - interesting uncovered follow-ups specific to that appearance
   - best social/clip angle
   - confidence and limitations
5. Write merged outputs to `appearances/appearances_analysis.json` and `appearances/appearances_summary.md`.
6. Create `html/appearances/<source_slug>.html` for each source. Each subpage must put the external URL at the top and include the sections above.
7. For YouTube/video/audio transcripts, include clickable timestamp links for key moments and a detailed chronological transcript map. Do not settle for a 3–5 bullet summary; include enough segment-level bullets that the host can inspect the exact part of the source and understand what was said without rewatching the full episode.
8. For written/article/web sources, capture page text and include detailed source-note bullets, not just a citation card.
9. Add a top-level dashboard Appearances tab/section that links to every source subpage and summarizes the strongest clip/research angle.

## Hybrid search index for agents

When the research folder has substantial material, build a searchable agent index under `guest_research/<guest_slug>/search_index/`.

Required behavior:

1. Chunk all usable research material with provenance: appearances analysis/transcripts, source text, synthesis YAML/Markdown, strategy docs, episode architecture, and discovery manifests.
2. Preserve `chunk_id`, `source_id`, `source_type`, title, canonical URL, local dashboard/subpage path, section, optional timestamps, tags, and text.
3. Build a BM25/keyword layer using SQLite FTS5 (`research_index.sqlite`) for exact lookup of names, tools, companies, and quotes.
4. Build a lightweight semantic layer when full embeddings are unavailable. The current repo implementation uses local hashed lexical cosine as a dependency-free vector-style fallback; upgrade to real embeddings/sqlite-vec or LanceDB when provider choice is available.
5. Write reverse-mined search assets:
   - `suggested_terms.json` for raw/high-frequency useful terms.
   - `suggested_topics.json` for top-level agent query clusters such as AI engineering/RAG/agents, production ML/MLOps, DataTalks community flywheel, career/portfolio, Bookcamp/Kaggle, serverless ML, interview system design, and productive tensions.
   - `README.md` with build/search commands and recommended agent queries.
6. Export `dashboard_search.json` and copy it into `html/search_index/dashboard_search.json` so the static dashboard can load it from the local HTTP server root.
7. Add a dashboard Search tab with topic chips, query box, filters, and source-aware result cards linking back to local subpages and external URLs.

CLI pattern:

```bash
cd scripts
node research-index/build-index.mjs --guest <guest_slug> --root ../guest_research/<guest_slug> --sqlite /path/to/sqlite3
node research-index/search.mjs --guest <guest_slug> --root ../guest_research/<guest_slug> --query "AI agents production guardrails" --mode hybrid --topK 8
node research-index/reverse-terms.mjs --guest <guest_slug> --root ../guest_research/<guest_slug>
```


Questions should:

- Make the guest look sharp, specific, and useful.
- Prefer trade-offs, updated beliefs, decision rules, and concrete examples.
- Avoid generic biography unless it is needed as a fast bridge.
- Avoid questions already asked repeatedly in prior podcasts/interviews; when external appearances are available, build a source-level do-not-repeat list and prefer follow-ups that were not covered in that specific appearance.
- Create social clips: contrarian claims, clear frameworks, vivid examples, or a strong before/after.
- Weave current offerings naturally by asking about problems and lessons the offering solves, not by naming the offer.

## Episode architecture and transcript critique

When Tony asks for interview flow, episode structure, big-podcast comparison, controversy, or previous-episode critique:

1. Run specialist research passes for:
   - major interview podcast structure
   - question-flow mechanics
   - narrative/story arcs
   - ethical/productive controversy prompts
   - technical/data/AI podcast pacing and depth
2. If prior show transcripts are available, analyze them deeply for:
   - opening strength
   - question length and specificity
   - follow-up ladders
   - story/tension extraction
   - missed uncomfortable prompts
   - closing strength
3. Write `episode_architecture/` artifacts and add a separate HTML dashboard tab.
4. The tab should include:
   - a recommended 45–60 minute episode arc
   - critique of prior Data Hustle question patterns
   - productive-controversy prompt bank
   - guest-specific episode flow
   - reference shows/sources
5. Default target arc: `Hook → stakes → story → conflict → framework → application → callback → takeaway`.

Controversy rules:

- Use controversy as earned belief, not gotcha.
- Ask permission to push.
- Challenge ideas, incentives, and trade-offs, not the person.
- Ask where mainstream advice breaks, where the guest's own framework fails, and who should not buy their offer.
- Do not pressure guests to reveal confidential information, violate NDAs, or name-and-shame.

## Verification

Before handoff:

1. Validate files exist under `guest_research/<guest_slug>/`.
2. Serve `html/index.html` locally.
3. Expose through Tailscale when Tony needs review.
4. Verify HTTP 200 locally and on the Tailscale URL.
5. Run Playwright at MacBook Air, iPad, and iPhone breakpoints.
6. Verify:
   - title and H1 render
   - timeline section exists
   - timeline has milestone buttons
   - clicking a later milestone changes the detail panel
   - episode architecture tab exists when requested and tab buttons switch panels
   - appearances tab exists when requested, links to one subpage per appearance source, and representative subpages render URL, summary, guest angle, do-not-ask-again, and uncovered-follow-up sections
   - no relevant console/page errors
   - no horizontal overflow
7. Attach screenshots for the three standard breakpoints.

## Common pitfalls

1. **Skipping discovery.** Do not rely only on the seed URL.
2. **Batching too many sources.** One source per parser preserves detail and avoids mixing evidence.
3. **Treating LinkedIn as complete.** Public LinkedIn is partial; mark full activity export as manual when auth-walled.
4. **Writing static visual artifacts.** Raw YAML is useful for audit, but the HTML dashboard must include interactive visual representations, especially the vertical timeline.
5. **Overpromoting offerings.** Let the guest explain problems, trade-offs, and stories that naturally reveal the offer.
6. **Asking stale questions.** Use prior interviews to build a do-not-repeat list.
7. **One model for everything.** Sizing sources before dispatch is the difference between a cheap pass and a wasteful one — and between a thin extraction and a usable one. See the routing table.
8. **Barriering the pipeline.** Waiting for every extraction before starting any per-source page wastes wall-clock for no gain. Only synthesis needs the barrier.

Write only the requested outputs. Do not print credentials, tokens, cookies, API keys, or private data. Replace any credential-like values with `[REDACTED]`.
