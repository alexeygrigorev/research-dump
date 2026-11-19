# 12. Monitoring and Observability for LLM Applications


Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 4. Application quality. 7 lessons, 2-3 hours.

## Summary

Learners instrument the internal support assistant with OpenTelemetry and use Langfuse to inspect requests, diagnose slow calls, and connect feedback to traces.

## Learning objectives

- Create nested spans for assistant requests, retrieval, tools, and model calls
- Export traces over OTLP/HTTP to Langfuse and inspect failures and latency
- Track token usage and estimated cost across a session
- Attach feedback and select representative traces for offline evaluation

## Why here

Testing establishes expected behavior. Tracing shows where real runs diverge and gives learners examples to turn into scenarios in the next course.

## Transformation

From "I don't know what my application does after I ship it" to "I can trace every request, what it cost, and whether users were happy."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

OpenTelemetry spans and attributes, OTLP/HTTP export, Langfuse trace views and scores, trace and session IDs, model usage and latency.

### How it's used in the exercises

Instrument the assistant with a parent span for the request and child spans for retrieval, tool calls, and generation. Inspect a slow trace in Langfuse, compute the cost of its session, and associate a feedback score with the trace.

### Model / release

Python 3.13, OpenTelemetry Python SDK, Langfuse tracing SDK or a compatible OTLP/HTTP exporter, and the assistant’s existing model.

### Source material

- Buildcamp Week 5, Pydantic Logfire and Jaeger, grouping traces, and feedback. Adapt the same workflow to Langfuse.
- [Langfuse OpenTelemetry ingestion documentation](https://langfuse.com/docs/api-and-data-platform/features/public-api)

### Notes

Grade instrumentation against a local in-memory span exporter and assess trace analysis against bundled traces. Use an instructor-provided or self-hosted Langfuse instance for the live walkthrough.

## Exercise adapted from the Buildcamp

Adapt the trivia agent exercise to a multi-turn internal support session. Have learners group model and tool spans by turn, join the turns using a session ID, and calculate the session cost from token counts and a supplied price table. Use bundled trace records for grading and ask learners to identify which call accounts for the most latency.

[Buildcamp Week 5 source](https://github.com/alexeygrigorev/ai-bootcamp/blob/60cc917c776e74d3aaeffb2d24f8f93c320e4b8b/v2/05-monitoring/homework/01-homework.md)

## Lesson outline and source map

see my workshop about langfuse

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 12.1 | What to trace in an assistant | BC Week 5 overview | TODO - tracing 
| 12.2 | Instrument retrieval and tool calls | BC `v2/05-monitoring/03-jaeger/01-logfire-jaeger.md` | split? 
| 12.3 | Export traces to Langfuse | [Langfuse tracing quickstart](https://langfuse.com/docs/observability/get-started) |
| 12.4 | Inspect a trace for errors and latency | BC `v2/05-monitoring/02-logfire/03-grouping-traces.md` |
| 12.5 | Track model usage and session cost | BC Week 5 homework |
| 12.6 | Attach feedback to a trace | BC `v2/05-monitoring/02-logfire/04-tracking-user-feedback.md` |
| 12.7 | Select traces for offline evaluation | BC `v2/05-monitoring/02-logfire/05-downloading-data.md` |

## Detailed lesson outline

### 12.1 What to trace in an assistant

Inspect a sample assistant run and identify request, retrieval, tool, and model operations.

**Check.** Map them into a trace with parent and child spans.

### 12.2 Instrument retrieval and tool calls

Instrument retrieval and tool calls with OpenTelemetry and capture them in a local exporter.

**Check.** Check span names, parent IDs, and error status.

### 12.3 Export traces to Langfuse

Configure OTLP export for a provided Langfuse instance or inspect a saved trace and its exporter settings.

**Check.** Match the received trace to the request ID and nested spans.

### 12.4 Inspect a trace for errors and latency

Inspect a trace with a slow model call and a failed tool.

**Check.** Identify which span accounts for the delay and which records the error.

### 12.5 Track model usage and session cost

Group traces by session and compute cost from token counts and a provided price table.

**Check.** Compare the calculated session total with the fixture total.

### 12.6 Attach feedback to a trace

Attach a feedback score to a traced answer through the supplied Langfuse workflow.

**Check.** Verify the score references the intended trace ID.

### 12.7 Select traces for offline evaluation

Pick representative success, failure, and insufficient-evidence traces and turn them into offline cases.

**Check.** Verify each case contains sanitized input, expected behavior, and a source trace ID.
