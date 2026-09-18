# ThreadScout coding-agent contract

Read README.md, docs/SPEC.md, docs/TONIGHT.md and docs/TEST_REPORT.md first.

Local Python 3.11+, standard library, SQLite, single-owner Telegram. Existing Codex subscription is optional. No paid API fallback, paid monitoring service, cloud deployment or hardware purchase without a new explicit user request.

Run `python -m unittest discover -s tests -v` and `python -m compileall -q threadscout` after changes. Keep test fixtures invented. Tests must not read real credentials, call live models, publish social comments, or access user accounts.

Do not inspect, copy, print, commit or upload .env, data/, auth.json, Telegram tokens, OAuth tokens, local replies or raw conversation logs. Public profile.json contains only sourced professional facts. Do not read unrelated parent-repository research to enrich private profiles. Keep all changes in this project directory.

HN public-text generation, rewriting and AI translation remain off. Private notes never populate the human draft field. Code cannot prove human authorship; do not claim it does. Reddit is opt-in only after actual documented approval for the intended scope; a configuration switch is not permission. No scraping fallback or bot-detection evasion.

Current implementation does NOT publish to HN/Reddit and does NOT control a browser. Treat a future user-confirmed publisher as a separate integration with explicit recipient/parent/text/version confirmation and uncertain-delivery reconciliation. Do not silently add publishing, votes or private messaging. Only the user may approve a real external post.

Do not remove sandbox/auth restrictions to fix Codex flag errors. Check installed CLI docs first. Do not seed ChatGPT auth in public CI. User profile facts must retain sources and distinguish free, paid and sign-in-gated material. No inferred sensitive traits or invented first-person experience.

Preserve owner + private-chat authorization, HMAC Mini App validation, draft concurrency, deduplication, bounded work and source-health visibility. A 0-result scan and a failed scan must remain different. Keep known limitations honest: short-lived Reddit token, partial context, no reply tracking, no publication, no full Telegram deletion lifecycle, no live integration proof yet.
