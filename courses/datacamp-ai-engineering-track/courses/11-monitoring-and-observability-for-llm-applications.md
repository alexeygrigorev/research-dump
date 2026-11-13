# 11. Monitoring and Observability for LLM Applications

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 5. Production. 7 lessons, 2–3 hours.

## Summary

Observability (2,018 jobs; 23.6% AI-First) and Monitoring (1,414 jobs; 15.4% AI-First) are core production requirements, with LLM-native observability/eval tooling rising to 34.5%. Learners log every interaction to SQLite/PostgreSQL, trace agent runs with OpenTelemetry, collect user feedback, track cost and latency, run an online judge, and build a dashboard.

## Learning objectives

- Define what to log for an LLM application and store it in SQLite/PostgreSQL
- Trace an agent run with OpenTelemetry and read the span tree to find a slow or failing step
- Collect user feedback and connect it to the logged interaction
- Track cost and latency and run an online LLM judge
- Build a dashboard that shows system health

## Why here

Opens the Production stage (71.0% of AI-First roles combine GenAI + Ops; deploy/production in 78.3% of responsibilities): it needs the application, judges and cost tracking from earlier courses, and its logs feed back into evaluation.

## Transformation

From "I don't know what my application does after I ship it" to "I can trace every request, what it cost, and whether users were happy."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

Log record schema, SQLite/PostgreSQL tables, OpenTelemetry spans and traces, feedback (thumbs up/down) records, cost from token usage, online judge over stored logs, Streamlit and Grafana dashboards, synthetic traffic generator

### How it's used in the exercises

The learner adds logging and OpenTelemetry tracing to the assistant, generates synthetic traffic, queries the log table for cost and latency, adds a feedback button, runs a judge over the stored answers, and assembles the charts into a dashboard.

### Model / release

Python 3.13; `streamlit>=1.58.0`, `pandas>=3.0.3`, `psycopg[binary]>=3.3.4` or `sqlite3` (stdlib), `opentelemetry-sdk` (version TBC), `langgraph` / `pydantic-ai>=1.55.0`. Small model.

### Source material

- **FG** (AI Engineering Field Guide, 9,760 jobs): Observability 2,018 jobs (23.6% AI-First), Monitoring 1,414 jobs (15.4% AI-First), LLM-native eval/observability 26.7% → 34.5%, Deploy/production 78.3%, Monitoring/maintenance 64.3%, PostgreSQL 1,020 jobs
- **LZ**: LLM Zoomcamp (`github.com/DataTalksClub/llm-zoomcamp`) Module 5 Monitoring (all lessons)
- **BC**: AI Engineering Buildcamp (`ai-engineering-buildcamp/curriculum.md`) Week 5: DIY Logging and Monitoring, Pydantic Logfire and Jaeger, Logfire

### Notes

No-subscription constraint: the Buildcamp uses Logfire (hosted account); this plan uses the self-hosted route from the same material (OpenTelemetry → Jaeger or self-hosted Langfuse-compatible trace store, SQLite/PostgreSQL + Streamlit/Grafana). Grafana and Jaeger need local services; if not available, keep SQLite + Streamlit.

## Lesson outline and source map

FG = AI Engineering Field Guide, LZ = LLM Zoomcamp path, BC = AI Engineering Buildcamp path. `'new'` = no lesson in LZ or BC.

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 11.1 | What to monitor in an LLM application | LZ `05-monitoring/01-intro.md`, `04-metrics.md`; FG Observability (23.6% AI-First) |
| 11.2 | Logging interactions to SQLite/PostgreSQL | LZ `05-database.md`, `06-querying.md`; BC `v2/05-monitoring/04-diy-logging/02–04` |
| 11.3 | Tracing agent runs with OpenTelemetry | BC `v2/05-monitoring/03-jaeger/01-logfire-jaeger.md`; `02-logfire/03-grouping-traces.md` |
| 11.4 | User feedback | LZ `08-user-feedback.md`; BC `02-logfire/04-tracking-user-feedback.md` |
| 11.5 | Cost, latency and an online judge | LZ `09-built-in-judge.md`; BC `04-diy-logging/07-online-judge.md` |
| 11.6 | Dashboards | LZ `07-streamlit-dashboard.md`, `10-feedback-dashboard.md`, `12-grafana.md`; BC `04-diy-logging/05, 08` |
| 11.7 | Synthetic traffic and closing the loop | LZ `11-synthetic-data.md`; BC `04-diy-logging/06`; `02-logfire/05-downloading-data.md` |
