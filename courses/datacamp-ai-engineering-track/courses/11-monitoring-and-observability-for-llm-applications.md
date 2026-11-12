# 11. Monitoring and Observability for LLM Applications

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 5. Production. 7 lessons, 2–3 hours.

## Summary

Once people use the application, the developer needs to see what it does. Learners log every interaction, trace agent runs, collect user feedback, track cost and latency, run a judge on live traffic, and build a dashboard.

## Learning objectives

- Define what to log for an LLM application and store it in a database
- Trace an agent run and read the span tree to find a slow or failing step
- Collect user feedback and connect it to the logged interaction
- Track cost and latency and run an online LLM judge
- Build a dashboard that shows system health

## Why here

Opens the Production stage: it needs the application, judges and cost tracking from earlier courses, and its logs feed back into evaluation.

## Transformation

From "I don't know what my application does after I ship it" to "I can see every request, what it cost, and whether users were happy."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

Log record schema, SQLite/Postgres tables, OpenTelemetry spans and traces, feedback (thumbs up/down) records, cost from token usage, online judge over stored logs, Streamlit and Grafana dashboards, synthetic traffic generator

### How it's used in the exercises

The learner adds logging to the assistant, generates synthetic traffic, queries the log table for cost and latency, adds a feedback button, runs a judge over the stored answers, and assembles the charts into a dashboard.

### Model / release

Python 3.13; streamlit>=1.58.0, pandas>=3.0.3, psycopg[binary]>=3.3.4 or sqlite3 (stdlib), opentelemetry-sdk (version TBC), pydantic-ai>=1.55.0. Small model.

### Source material

- LLM Zoomcamp (github.com/DataTalksClub/llm-zoomcamp) Module 5 Monitoring (all lessons)
- AI Engineering Buildcamp (Maven course; repo ai-engineering-buildcamp, curriculum.md) Week 5: DIY Logging and Monitoring, Pydantic Logfire and Jaeger, Logfire

### Notes

No-subscription constraint: the Buildcamp uses Logfire (hosted account); this plan uses the self-hosted route from the same material (OpenTelemetry → Jaeger, SQLite/Postgres + Streamlit/Grafana). Grafana and Jaeger need local services; if not available, keep SQLite + Streamlit.

## Lesson outline and source map

LZ = LLM Zoomcamp path, BC = AI Engineering Buildcamp path. 'new' = no lesson in either source.

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 11.1 | What to monitor in an LLM application | LZ 05-monitoring/01-intro.md, 04-metrics.md |
| 11.2 | Logging interactions to a database | LZ 05-database.md, 06-querying.md; BC v2/05-monitoring/04-diy-logging/02–04 |
| 11.3 | Tracing agent runs with OpenTelemetry | BC v2/05-monitoring/03-jaeger/01-logfire-jaeger.md; 02-logfire/03-grouping-traces.md |
| 11.4 | User feedback | LZ 08-user-feedback.md; BC 02-logfire/04-tracking-user-feedback.md |
| 11.5 | Cost, latency and an online judge | LZ 09-built-in-judge.md; BC 04-diy-logging/07-online-judge.md |
| 11.6 | Dashboards | LZ 07-streamlit-dashboard.md, 10-feedback-dashboard.md, 12-grafana.md; BC 04-diy-logging/05, 08 |
| 11.7 | Synthetic traffic and closing the loop | LZ 11-synthetic-data.md; BC 04-diy-logging/06; 02-logfire/05-downloading-data.md |
