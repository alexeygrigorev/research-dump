# Pilot and manual validity review

Final prompt: jobs-v2; model: glm-5.3-flash. Fixed pilot: 60 historical + 40 live unique texts. Schema/evidence/numeric grounding: **100/100** successful outputs, no unresolved failures. This is syntactic grounding, not 100% semantic accuracy.

API-equivalent cost for the final 100 cached results (including retries in completed entries): **$0.05340**, or **$0.534 per 1,000 unique texts**. Projected 17,010 unique texts: **$9.08**, before further retries. Existing Coding Plan quota is used; these dollar figures are token-price equivalents, not an invoice. Failed exploratory runs and superseded text versions are additional and tracked in development-spend.json and the provider usage ledger.

Manual check: 20 rows, ten historical and ten live; exact IDs, hashes, observations and limitations are in [pilot-qa.json](pilot-qa.json). All 20 were compared against the description. The review found one clear role-category error, repeated over-classification of alternative/example skills as mandatory, and ambiguous AI contexts. Broad mentions are usable for descriptive sample comparisons; strict required-skill rates and narrow categories require caution. The primary skill charts count explicit mentions of all requirement levels. No claim of semantic 100% accuracy is made.

Conservative guards suppress unsupported LLM/vendor labels, inferred salary currency/period, unsupported seniority and headquarters-only office attendance. Reports prefer explicit title levels and retain both original model interpretation and normalization notes. AI product mentions do not establish coding-tool adoption.

A boilerplate audit found 75 real descriptions were entirely removed by the first paragraph rule. The final rule protects paragraphs containing requirements/skills markers and falls back to original text when fewer than 200 characters remain. All 17,506 available descriptions now remain available; one listing (Built In 10727820, EXL Software Production Engineer) has no saved detail file and no posted_date. That row is explicit missing-description data and is excluded from dated trends. No title-only LLM extraction is substituted.

Reposts are retained in extraction output but excluded from report counts through the global earliest-publication audit. QA/SDET, interns, staff and non-English vacancies remain included.

[Pricing reference](https://docs.z.ai/guides/overview/pricing), checked 2026-11-15: $0.15/M input, $0.03/M cached input, $0.50/M output.
