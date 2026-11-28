# Vacancy extraction v2

`vacancies.jsonl.gz` in this directory and `data/live/extracted/` contain one JSON object per **input row**, including repost observations. Report counts use `reports/dedup-audit.jsonl.gz`, one record per row, to select only the earliest original publication for each linked vacancy. Never sum the extraction rows as new jobs.

- Identity/provenance: `dataset`, `vacancy_id`, `source`, `job_id`, `url`, `title`, `company`, `locations`, `posted_date`, `month_basis`; historical capture metadata is retained. `region` is the first resolvable location region; `regions_all` retains the complete distinct set without creating extra vacancies.
- `seniority_title`: explicit title level matched by deterministic rules (intern, principal, staff, lead, manager, senior, junior, otherwise unknown). Reports prefer this when present, otherwise use explicit description seniority. Years alone do not imply a level.
- `tags`: title/metadata flags `qa_sdet`, `intern`, `staff`; `non_english` comes from extracted language (historical heuristic fallback for missing descriptions). These are descriptive tags, never filters.
- `text_hash`: SHA-256 of `jobs-v2\n` + boilerplate-stripped description. Extraction is cached **only on text**, with identical text sharing one model response. Role in `extracted` therefore describes the text; title-based tags stay row-specific.
- `status`: `ok`, `missing_description`, or `error`. Validation requires >=99% `ok` rate across non-missing rows. Missing live description rows and strict-grounding validation errors remain explicit with their error reason and are excluded from LLM-share denominators; they still count in dated vacancy `n`.
- Successful rows: `model=glm-5.3-flash`, `prompt_version=jobs-v2`, provider `request_id`, `usage_attempts` (including rejected responses/retries within a completed cache entry), and `extracted` below.

## Extracted fields

| field | type / values | missing |
|---|---|---|
| role | software_engineer, frontend, backend, fullstack, data_ml, devops_sre, qa_sdet, engineering_manager, other, unknown | unknown |
| seniority | intern, junior, mid, senior, staff, principal, lead, manager, unknown | unknown |
| skills | array of `{name, requirement: required/preferred/mentioned, evidence}` | [] |
| ai_mentions | array of `{name, context: developer_tool/product_work/general, evidence}` | [] |
| experience | `{min_years, max_years, evidence}`; explicit candidate work experience | null values |
| workplace | `{mode: remote/hybrid/office/unknown, evidence}`; description only | unknown / null |
| salary | `{min, max, currency, period: hour/day/week/month/year/unknown, evidence}`; explicit base pay, no conversion | null values / unknown period |
| language | ISO language code | unknown |

Every non-null evidence string is matched across whitespace and hyphen line wraps, mapped back to the exact source span, then validated as an exact substring of the text sent to the model. This verifies grounding, not semantic correctness: the 20-row manual pilot check separately reviews interpretation. Extracted names are model-normalized; report aggregation normalizes Unicode, case and punctuation only, so aliases can remain split. Empty AI arrays mean no explicit mention extracted, not proof that a company does not use AI.

Boilerplate removal drops whole blank-line-delimited paragraphs matching EEO, privacy, or standalone About-us/company/team headings, plus board tags. It can remove relevant requirements embedded in legal paragraphs; original inputs are unchanged. Source text is never truncated. Live hard wraps ending before lowercase text are joined; quotes refer to this normalized text.

## Reproduction

Requires Python 3.12+, requests, PyYAML, matplotlib, jsonschema. Fetch the frozen live input commit `59126d538145ec21faed82bc648cbd5536048de3` from `alexeygrigorev/agentic-engineering-field-guide` into an input directory (including listing CSV and the YAML details).

```bash
python agentic-engineering-field-guide/scripts/extract_jobs.py --live-input /path/to/frozen-live-repo --pilot
# Review reports/pilot.json, 20 rows and pilot-summary.json before full run.
python agentic-engineering-field-guide/scripts/extract_jobs.py --live-input /path/to/frozen-live-repo --workers 8
python agentic-engineering-field-guide/scripts/report_jobs.py
python agentic-engineering-field-guide/scripts/check_extraction.py
```

`ZAI_API_KEY` is preferred. Locally the existing `~/.local/share/opencode/auth.json` provider `zai-coding-plan.key` is a fallback; its value is never printed or committed. Endpoint: `https://api.z.ai/api/coding/paas/v4/chat/completions`. No credentials in CI: CI validates committed outputs and deterministic reports only. Cache defaults to `~/tmp/jobs-extractor-cache/`; rerunning resumes completed hashes. Failed hashes are retried; never published as successes. Cache keys include prompt version; bump that version whenever the extraction semantics change.

Cost uses provider-reported input, cached-input, and output token counts. [Z.ai pricing](https://docs.z.ai/guides/overview/pricing) checked November 15, 2026: $0.15/$0.03/$0.50 per million tokens. This is API-equivalent cost, not an invoice: the existing Coding Plan uses subscription quota. Pilot summaries and run summaries record tokens; final spend report separates these quantities.

## Conservative normalization and QA limits

`normalizer_version=conservative-v1` and `normalization_notes` explain deterministic adjustments after each model response (including cache hits). Unsupported seniority becomes unknown; explicit title seniority is preferred only in reports. Salary currency is null unless its code or an unambiguous currency expression is present in the source. Salary period becomes unknown unless the salary evidence states it. Office attendance inferred solely from headquarters location becomes unknown. Named LLM/developer tools require support in their evidence. The raw model cache retains the original reply. Salary `k`/`m` notation, including a shared suffix such as 150–220k, is expanded when checking numeric grounding.

Boilerplate paragraphs containing requirement/qualification/skills/responsibility markers are preserved. If stripping leaves fewer than 200 characters, the original normalized description is retained (except board tags), avoiding loss of short or single-paragraph postings. `description_chars` and `extraction_chars` record the effect. This deliberately keeps some legal/company language to protect job requirements. General company AI marketing can still enter the broad AI-mention metric; it is distinct from developer-tool mentions.

Skill mentions are descriptive and not exhaustive. The manual check found examples/alternatives sometimes over-classified as required and one coarse role error. Primary trend tables therefore use all explicit skill mentions; requirement categories remain available for cautious use. `experience.max_years` can describe the upper end of a preferred range, not an absolute hiring cutoff; alternatives to experience (degree/portfolio) remain in evidence. Conditional geography/level salary ranges can be represented by their full lower/upper envelope, with the complete evidence span. Do not treat this as a single location-specific offer.
