# Agentic Engineering Field Guide: data plan

Status: draft for Alexey's review (intake t3267u / t3269u), written 2026-11-13.
Nothing has been collected, scraped in bulk, or bought. Prices and coverage below were read from the providers' own pages on 2026-11-13; anything I could not confirm is marked "not verified".

Repo for the guide: https://github.com/alexeygrigorev/agentic-engineering-field-guide (public, skeleton only, no job data; registered in Hub).

## Decisions I need from you

1. Approve the history source. My recommendation is TheirStack, bought directly for one month: $400 for 50,000 postings. The alternative is free sources only, which gives a weaker year of history.
2. Approve the free first step before any money is spent: about 200 count queries on TheirStack's free tier, which already gives a 13-month trend line per country.
3. Confirm the geographies (section 7): keep NY, London, Amsterdam, Berlin and India; replace LA with the SF Bay Area; add a Remote bucket.
4. Confirm the sample size: about 40,000 postings (13 months, 8 geographies, about 400 per cell), against "as many as possible".
5. Say whether full job descriptions bought from a provider may go into the public repo, or only the structured fields and links (section 6, licence notes).

## What I found, in short

- Built In cannot give history. Expired postings return 404 on the live site, so a scrape today only sees what is open today. It stays useful as a current source.
- A year of history with full text exists and is cheap. TheirStack keeps expired postings back to 2021, filters by posting date, and charges one credit per posting: $400 for 50,000.
- There is a simpler way than scraping for the trend lines. TheirStack returns the total number of matching postings for one credit per query, and it can filter on words in the description. So "how many software engineer postings in Germany in March 2026 mention Claude Code or Cursor" costs one credit, with no text bought at all.
- treg has job tools, but none fits the history need. Its TheirStack route costs $0.02 per posting (2.5 times the direct price), and its cheapest provider (MobiusEngine) has open postings only and no full descriptions.
- Free history exists but is thin: Hacker News "Who is hiring" threads (complete), Indeed Hiring Lab's software-development index (aggregate only), and Wayback Machine captures of Built In pages (an uncontrolled sample).
- The market itself moved: Indeed's US software-development postings index went from 66.0 on 2025-11-07 to 81.4 on 2026-11-06 (February 2020 = 100).

## 1. What I would do, step by step

Each step that costs money or touches a site in bulk starts only after you approve it.

| Step | What happens | Cost | Output |
|---|---|---|---|
| 0 | You review this plan and answer the five decisions above | $0 | Approved scope |
| 1 | Sizing with counts: about 200 TheirStack count queries on the free tier (13 months x 5 countries x 3 queries: all software engineer postings, those mentioning AI coding tools, those with agentic titles) | $0 | First trend chart per country; real volumes per cell, so the sample plan uses measured numbers |
| 2 | Free history: Hacker News "Who is hiring" threads for Nov 2025 to Nov 2026 through the Algolia API, and the Indeed Hiring Lab CSVs | $0 | About 5,000 startup postings with full text; a market-level index for US, UK, Germany, Netherlands |
| 3 | Paid history: TheirStack backfill, a stratified sample of about 40,000 postings with full descriptions | $400 (one month, then cancel) | The 12-month corpus |
| 4 | Signal counts: about 10,000 more count queries for the fine-grained trend lines (each tool and practice, per month and geography) | Covered by the 10,000 credits left from step 3 | Monthly share series on the full population, not on the sample |
| 5 | Current data, monthly from now: Built In scraper (ported, new search terms) plus public ATS APIs (Greenhouse, Lever, Ashby) | Proxy traffic only | A fresh monthly snapshot that keeps the series going after the backfill |
| 6 | LLM extraction on the sample with a new schema (section 2) and an accuracy check on 100 hand-labelled postings, as in the AI guide | LLM cost not estimated yet | `data_structured/` |
| 7 | Analysis and writing: `role/` pages (skills, responsibilities, trends), mirroring the AI guide | $0 | The guide |

Steps 1 and 2 are free and reversible. If the step 1 numbers show that TheirStack's coverage is poor for one geography (India is the one I would watch), I come back to you before step 3.

## 2. Which job titles and postings

The AI guide searched one title ("AI Engineer"). This guide has a different shape: the subject is the whole software engineer market, and the question is how postings inside it changed. So I collect a broad baseline and measure signals in it.

### Layer A: the baseline population (what gets sampled)

| Family | Titles matched |
|---|---|
| Core software engineering | Software Engineer, Software Developer, Backend Engineer, Frontend Engineer, Full Stack Engineer, Web Developer, Mobile / iOS / Android Engineer, Product Engineer, Founding Engineer, Member of Technical Staff |
| Platform and operations | Platform Engineer, DevOps Engineer, Site Reliability Engineer, Infrastructure Engineer, Developer Experience / Developer Productivity Engineer |
| Quality | QA Engineer, SDET, Test Automation Engineer |
| Leadership | Engineering Manager, Tech Lead, Staff Engineer, Principal Engineer |

All seniority levels are included, from intern and junior to principal. The junior share over the year is one of the trends to track.

Excluded by title: AI Engineer, ML Engineer, Data Scientist and Data Engineer (the AI guide covers the first; the others are a different market), Sales and Solutions Engineer, Support Engineer, and non-software engineering (hardware, mechanical, electrical, civil, field service).

### Layer B: explicitly agentic titles (collected in full, they are few)

Agentic Engineer, Agent Engineer, AI-Native Engineer, AI Software Engineer, AI-Assisted Developer, AI Enablement Engineer, AI Developer Productivity, Forward Deployed Engineer (kept as a comparison with the AI guide's FDE page).

### Layer C: signals inside the description (what gets measured)

| Signal group | Terms |
|---|---|
| Coding agents and assistants | Claude Code, Cursor, GitHub Copilot, Codex, Windsurf, Devin, Aider, Gemini CLI, "AI coding assistant", "AI pair programming" |
| Agentic practice | "agentic", "coding agents", MCP / Model Context Protocol, "context engineering", "spec-driven", "prompt engineering", evals, "AI-assisted development" |
| Expectation wording | AI use required against nice to have; "AI-native", "AI fluency", "AI-first"; reviewing AI-generated code |
| Role shape | Years of experience, seniority, team size, breadth (full stack against a single specialty), salary range, remote or on-site |
| Classic stack | Languages, frameworks, cloud, testing and CI, so the guide can show what stayed the same |

Groups one and two are measured twice: as count queries on the full population (step 4) and as LLM-extracted fields on the sample (step 6). The other groups need the text and come from the sample only.

### Sample design

The baseline is too large to collect whole; one year of software engineer postings in these countries runs into the millions. The plan is a stratified sample: 13 months (Nov 2025 to Nov 2026) x 8 geographies x about 400 postings = about 41,600. Within a cell the postings are spread across posting days, because TheirStack returns newest first and has no random ordering. Deduplication is by company plus normalised title plus city within a month, since the same job is reposted and syndicated.

## 3. Where current data comes from

| Source | What it gives | Access | Verdict |
|---|---|---|---|
| Built In (`builtin.com`, the AI guide's source) | Full description, `datePosted`, skills, company size; search by keyword and city | Existing scraper, residential proxy | Keep as one current source. Port the scraper, change the search terms. Strong for US tech companies, thin for Germany, the Netherlands and India. No history. |
| Greenhouse, Lever, Ashby public job-board APIs | Full description, publish date, department, location, as JSON | Free, official, no login, no proxy; one request per company | Add. The simplest clean source (section 5). Needs a company list. |
| TheirStack Jobs API | Aggregated LinkedIn, Indeed, ATS and others; full description; 195 countries | Paid, 1 credit per posting | Use for history; can also do the monthly refresh if scraping becomes a burden. |
| Hacker News "Who is hiring" | About 230 to 390 top-level postings a month, full text | Free Algolia API | Add. Small, but startup-heavy and an early signal for agentic tooling. |
| LinkedIn and Indeed live scrapers (Apify actors, JobSpy) | Full description, current postings only | $1 to $3 per 1,000 on Apify; JobSpy is free and needs proxies | Skip for now. TheirStack already includes both sources. |

Built In as a starting point: yes for current data, no for history. The scraper already works and the output format is known, so the port is a small job. Two limits matter. First, a keyword search for "Software Engineer" will return far more pages than "AI Engineer" did (the AI guide's largest month was 1,709 postings across six locations), so the scraper needs a per-city page cap and the sample design above. Second, Built In is a US tech job board, so it under-represents Berlin, Amsterdam and India.

## 4. Where the last 12 months of history comes from

This is the hard part: job boards delete expired postings, so history has to come from someone who was already collecting a year ago.

| Source | History | Full text | Coverage | Cost | Verdict |
|---|---|---|---|---|---|
| TheirStack Jobs API | Expired postings back to 2021; `posted_at_gte` / `posted_at_lte` date filters | Yes | 195 countries; LinkedIn, Indeed, Greenhouse, Lever, Workable and others | $400 for 50,000 | Recommended |
| Coresignal Jobs API | Since August 2020 | Yes | Global; sources described only generically | $1,000 for 50,000 (Growth plan, one month) | Backup; has a free 2,000-credit trial for a coverage comparison |
| Bright Data datasets (LinkedIn 19.7M, Indeed 50.5M records) | Not stated; retention of expired postings not verified | Yes | Global | $250 per 100,000 records, $250 minimum | Cheapest list price, but history is unconfirmed; check the free preview first |
| Techmap / JobDataFeeds country archives | Since January 2020, daily files | Yes | Per country | US $5,999; Germany $4,999; UK $4,999; India $999; Netherlands $499 (one-time each) | Too expensive for the large countries; the Netherlands and India archives are affordable add-ons |
| Fantastic.jobs | Last 6 months only | Yes | 58 ATS platforms, LinkedIn | From $4 per 1,000 on Apify | Does not reach Nov 2025 |
| Hacker News "Who is hiring" | Complete, back to 2011 | Yes | Global, startup-heavy | Free | Use |
| Indeed Hiring Lab (GitHub, CC BY 4.0) | Daily index since Feb 2020, refreshed weekly; a separate AI-share tracker | No, aggregates only | US, UK, Germany, Netherlands and six more; no India | Free | Use as the market-level context series |
| Wayback Machine captures of `builtin.com/job/*` | About 8,000 to 12,000 captured job pages per month from Nov 2025 to Jun 2026; later months not measured (the archive was offline during the probe) | Yes, where captured | Whatever happened to be crawled, all job categories | Free | Optional. An uncontrolled sample; software engineer share unknown until fetched |
| Common Crawl | About 4,600 Built In job pages in the October 2026 crawl | Yes | Same caveat | Free | Skip; smaller than Wayback |
| ATS APIs (Greenhouse `first_published`) | Only postings still open today | Yes | Per company | Free | Not history: old postings that are still open are a biased leftover |
| Zenodo "AI-era software-engineering job postings: a 2024-2026 panel" (CC BY 4.0) | Two 2024 snapshots plus a 2026 scrape of 26 US metros | Partly; not confirmed for 2026 | US only | Free | Worth a look as a US cross-check; not a 12-month series |
| Lightcast, Revelio Labs, LinkUp | Long history | Yes | Global | Not public (contact sales; LinkUp's page was unreachable) | Enterprise contracts; not for this project |

Not usable for this purpose: Adzuna's API returns description snippets only and its history endpoint is salary averages; JSearch, SerpApi and similar are live Google Jobs results with no archive.

### What the recommended option buys

TheirStack API plans (monthly): $49 for 1,500 credits, $100 for 5,000, $169 for 10,000, $240 for 20,000, $400 for 50,000, $600 for 100,000, $900 for 200,000. One credit is one posting returned, or one count query. The free tier is 200 credits a month. Their FAQ says a one-month subscription that is then cancelled is allowed, and unused paid credits stay valid for 12 months.

| Budget | What it covers |
|---|---|
| $0 (free tier) | About 200 count queries: the headline trend per country |
| $169 (10,000 credits) | Counts only: every signal by month and geography, no texts |
| $400 (50,000 credits) | About 40,000 full postings plus about 10,000 count queries. Recommended |
| $900 (200,000 credits) | About 190,000 full postings, if you want city-level cuts with large cells |

Not verified for TheirStack: whether the listed prices are month-to-month or annual-billing rates, the maximum page size, and how complete its coverage is for India and for 2025 postings. Step 1 tests the last point for free.

## 5. Is there a simpler way than the current scrape

Yes, three of them, and they combine.

1. Count queries instead of collection. For trend lines the guide needs shares, not texts. One TheirStack request with a title filter, a date range, a country, `job_description_contains_or` and `include_total_results` returns the number of matching postings for one credit. A 13-month series for one signal in one country is 13 credits. This replaces scrape, download, parse and LLM extraction for every chart of the form "share of postings mentioning X over time".
2. An API with history instead of a scraper. The backfill is a paginated JSON API call. No proxy, no HTML parsing, no JS rendering fallback, and the response already has company, location, seniority, salary and the description in Markdown.
3. Public ATS APIs for the monthly refresh. `boards-api.greenhouse.io/v1/boards/{company}/jobs?content=true`, `api.lever.co/v0/postings/{company}?mode=json` and Ashby's posting API return every open job at a company with the full description. They are official and free. Open company lists exist (for example the MIT-licensed `Riley-Dorrington/job-board-aggregator` repo lists companies per ATS). The limit is that this covers companies using these three systems, which skews to tech startups and scale-ups.

What stays the same as the AI guide: LLM extraction over the sampled descriptions, because role shape, expectation wording and responsibilities cannot be counted with keyword filters.

## 6. treg and other paid providers

### treg

I searched the treg catalog (no paid calls made). It lists about 40 job-posting tools. The relevant ones:

| treg tool | Price in treg | History | Full description | Notes |
|---|---|---|---|---|
| `theirstack.jobs.search` | $0.02 per posting | Yes (TheirStack's archive) | Yes | 50,000 postings would cost $1,000 through treg against $400 direct |
| `mobiusengine-jobs.jobs.search` | $0.016 per 1,000 postings | Open postings only; `posted_within_days` up to 365, but only for jobs still open | No. A 300-character snippet costs $0.03 per 1,000; full text is "not sold on pay per job" | Employer career sites (Workday, Greenhouse, Lever, Ashby and about 30 more). Terms forbid publishing the data in bulk |
| `mobiusengine-jobs.jobs.count` | $0.0036 per call | Same | Not applicable | Cheap way to size today's open market by title and country |
| `blitzapi.jobs.search` | $0.001 per posting | Not stated in the catalog | Not verified | Not investigated further |
| LinkedIn search tools (`apify`, `harvestapi`, `tikhub`, `anyapi`, `crawl4ai`) | $0.00045 to $0.001 per result or call | Live only | Through a second detail call at about $0.001 | Current postings only |
| `crawl4ai.indeed.search.jobs`, `crawl4ai.glassdoor.search.jobs` | $0.00015 per call | Live only | Not verified | Current postings only |
| `crawl4ai.hackernews.jobs.hiring` | $0.00015 per call | By keyword | Yes | The free Algolia API does the same |
| `treg.companies.jobs.search` (routed) | $0.009 to $0.04 per hit | No | Varies | Looks up one company's openings; built for sales signals, not market research |
| `predictleads.*`, `crustdata.*`, `apollo.companies.jobs` | $0.009 to $0.04 | Company-keyed | Varies | Same: per-company lookups |

treg has no Built In tool, and its Coresignal tools cover people and companies, not jobs.

Verdict on treg: it does offer job data, but not what this project needs. For a year of history with full text, buying TheirStack directly is 2.5 times cheaper than the same provider through treg. treg is the right tool for small things: MobiusEngine counts to size the current market for a few cents, or a few hundred live LinkedIn postings to spot-check coverage.

### Other paid providers

Covered in the section 4 table with verified prices: TheirStack, Coresignal, Bright Data, Techmap and Fantastic.jobs. Prices I could not verify and therefore do not quote: JobsPikr (prices are images on the page), LinkUp (page unreachable), Lightcast and Revelio Labs job-postings data (contact sales).

### Licence notes

- TheirStack's terms (section 4.3) list "reposting, redistributing, and publicly displaying job postings" as permitted, and forbid handing a single customer the dataset "in whole or substantially in whole". Aggregated statistics are yours. A 40,000-posting sample out of 265 million reads as allowed to me, but this is my reading, not legal advice.
- MobiusEngine's terms forbid publishing its data in bulk, so it can feed charts but not the repo.
- The AI guide publishes full descriptions scraped from Built In. If you prefer the cautious route for bought data, the repo can hold structured fields, the source URL and a short excerpt, with full texts kept private.

## 7. Geographies

The paid sources filter by country and by location, so the unit is "metro inside a country" rather than a Built In site.

| Geography | AI guide | Proposal | Rationale |
|---|---|---|---|
| SF Bay Area | No | Add | Where coding agents are built and adopted first; the leading edge of every trend this guide tracks |
| New York | Yes | Keep | Largest non-Bay-Area US market; finance and enterprise employers balance the startup skew |
| Los Angeles | Yes (as the "global" Built In search) | Drop as its own bucket | It was in the AI guide because of how Built In's LA site searches all locations, not because LA matters for this question |
| Rest of US | No | Add as one sampled bucket | Gives a national US number that can be compared with Indeed's index |
| London | Yes | Keep | Largest European market |
| Berlin (reported with Germany) | Yes | Keep | Your home market and the course audience; German-language postings show how fast the terms spread outside English |
| Amsterdam (reported with the Netherlands) | Yes | Keep | Small but international market; cheap to cover |
| India (Bangalore, Hyderabad) | Yes | Keep | Largest software engineer workforce outside the US and a large part of the DataTalks.Club audience; coverage to be checked in step 1 |
| Remote | No | Add | A large share of startup postings have no city, and dropping them would bias the sample |

That is eight buckets. Candidates I would leave out of the first version: Canada (Toronto), Poland (Warsaw) and Singapore. Each adds about 5,000 postings, so any of them fits inside the $400 budget if you want one.

Indeed's free index covers the US, UK, Germany and the Netherlands, which gives an external check for four of the five countries.

## 8. What the collection scripts look like

Design only. The repo has empty placeholders with these names; no logic is written.

```
job-market/
├── _internal/
│   ├── config/
│   │   ├── titles.yaml          # layer A families, layer B titles, exclusions
│   │   ├── geographies.yaml     # 8 buckets: country code, provider location IDs, Built In URL
│   │   └── signals.yaml         # layer C term groups for count queries
│   ├── collectors/
│   │   ├── theirstack_counts.py    # steps 1 and 4: count queries -> data/counts.csv
│   │   ├── theirstack_backfill.py  # step 3: stratified sample of full postings
│   │   ├── hn_whoishiring.py       # step 2: monthly threads via Algolia
│   │   ├── indeed_hiring_lab.py    # step 2: download the public CSVs
│   │   ├── builtin_listings.py     # step 5: port of scrape_builtin_requests.py
│   │   ├── ats_boards.py           # step 5: Greenhouse, Lever, Ashby
│   │   └── wayback_builtin.py      # optional: archived Built In job pages
│   ├── normalize.py             # every source -> one record schema
│   ├── clean_dedup.py           # company + normalised title + city within a month
│   ├── extract_llm.py           # layer C fields; same approach as the AI guide
│   ├── eval/                    # 100 hand-labelled postings, accuracy report
│   ├── analysis/                # trends.py, skills_analysis.py, charts.py
│   └── PIPELINE.md
├── data_raw/{YYYY-MM}/          # one YAML per posting, grouped by posting month
└── data_structured/{YYYY-MM}/   # the same postings after LLM extraction
```

Differences from the AI guide's pipeline:

- Folders are keyed by posting month, not scrape date. A backfill has one scrape date and 13 posting months, so the scrape date would lose the time axis.
- One normalised record for all sources: `source`, `source_id`, `url`, `title`, `company`, `country`, `city`, `remote`, `seniority`, `date_posted`, `date_collected`, `salary`, `description`.
- Every paid collector takes `--max-credits` and defaults to `--dry-run`, which prints the queries and the credit estimate without calling the API. A run is resumable: finished cells are skipped, because TheirStack charges again for a repeated fetch.
- `theirstack_counts.py` writes one row per query: month, geography, title family, signal, count, date run. The trend charts read this file directly.
- `theirstack_backfill.py` walks the cells (month x geography x family), splits each month into days, and takes a fixed number per day until the cell quota is met.
- API keys come from environment variables and are never written to the repo.

## Risks and open points

- Source mix changes over time. An aggregator's coverage in Nov 2025 may differ from Nov 2026, which can fake a trend. The mitigation is to report shares within a fixed source (for example LinkedIn-sourced postings only) next to the overall number, and to compare against Indeed's index.
- Keyword counts over-read and under-read. "Cursor" also matches database cursors, and "agentic" appears in product descriptions for companies that sell agents. Each count signal gets a precision check on 50 sampled postings before it is used in a chart.
- Reposts inflate counts. Deduplication handles the sample; for counts, the same rule cannot be applied, so counts are reported as shares, not absolute numbers.
- TheirStack's India coverage and its exact billing basis are not verified.
- The LLM extraction cost for 40,000 postings is not estimated here; it depends on the model chosen.

## Hub registration

The Hub registry commands (`hub repos list`, `show`, `add`) return "403 forbidden" for this worker, so I could neither confirm an existing registry entry nor create one. The entry is prepared and can be added by an operator with:

```
hub repos add alexeygrigorev/agentic-engineering-field-guide --file <json>
```

with `canonical_url` `https://github.com/alexeygrigorev/agentic-engineering-field-guide`, status `active`, domains `job-market`, `agentic-engineering`, `field-guide`.

## Sources

- TheirStack: https://theirstack.com/en/pricing, https://theirstack.com/en/docs/api-reference/jobs/search_jobs_v1, https://theirstack.com/en/docs/api-reference/features/count-results, https://theirstack.com/en/docs/pricing/credits, https://theirstack.com/en/docs/legal/terms-and-conditions
- Coresignal: https://coresignal.com/pricing/, https://coresignal.com/solutions/jobs-data-api/
- Bright Data: https://brightdata.com/products/datasets/linkedin/jobs, https://brightdata.com/products/datasets/indeed, https://brightdata.com/pricing/datasets
- Techmap: https://jobdatafeeds.com/pricing
- Fantastic.jobs: https://fantastic.jobs/api
- MobiusEngine: https://jobs.mobiusengine.ai/, https://jobs.mobiusengine.ai/docs, https://jobs.mobiusengine.ai/terms
- treg catalog: `treg catalog search` and `treg catalog get`, read 2026-11-13
- Indeed Hiring Lab: https://github.com/hiring-lab/job_postings_tracker, https://github.com/hiring-lab/ai-tracker
- Hacker News: https://hn.algolia.com/api
- Zenodo panel: https://zenodo.org/records/20321172
- Adzuna: https://developer.adzuna.com/docs/search
- AI Engineering Field Guide pipeline: `job-market/_internal/PIPELINE.md` in https://github.com/alexeygrigorev/ai-engineering-field-guide
