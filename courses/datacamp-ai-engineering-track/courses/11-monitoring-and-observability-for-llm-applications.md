# 11. Monitoring and Observability for LLM Applications

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 4. Application quality. 8 lessons, 2–3 hours.

## Summary

A speaker receives a correct answer eight seconds after asking when slides are due. The API log says the request succeeded. Was the delay in handbook search, a failed tool call, or generation? Learners follow one request from the endpoint through the agent's calls, add OpenTelemetry timing records, and use Langfuse to investigate latency, cost, and a speaker's complaint.

## Learning objectives

- Explain a trace by following one request through its timed operations, or spans
- Instrument retrieval, tools, and model calls and export their spans to Langfuse
- Diagnose a retry and calculate model costs for a multi-turn session
- Link a speaker's rating to the answer they saw and turn a confirmed failure into an evaluation case

## Why here

The tests from course 10 can reproduce known failures. This course helps learners investigate an individual run whose cause they do not yet know. Course 12 uses examples discovered in those runs to build an evaluation dataset.

## Transformation

Given a complaint, learners can find the affected turn, identify the step responsible, and gather evidence for a fix.

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

OpenTelemetry spans, timestamps, parent and trace IDs, OTLP over HTTP, Langfuse traces and feedback scores, session IDs, model token usage.

### How it's used in the exercises

Supply a two-turn speaker session, an unrelated request at nearly the same time, and their exported traces. One turn is slow because a handbook fetch times out and retries. Another cites the draft deadline in an answer about final slides. Learners first reproduce a trace with instrumented Python code, then diagnose the recorded incidents and attach a thumbs-down to the answer that prompted it.

### Model / release

Python 3.13, OpenTelemetry Python SDK, an OTLP/HTTP exporter, Langfuse, and the existing assistant. Grade learner instrumentation with an in-memory exporter and provide a captured Langfuse session for offline analysis.

### Source material

Buildcamp Week 5 covers grouping calls, tracking user feedback and downloading traces. The DataCamp exercises use the same questions with Langfuse as the trace backend. [Buildcamp monitoring](https://github.com/alexeygrigorev/ai-bootcamp/tree/60cc917c776e74d3aaeffb2d24f8f93c320e4b8b/v2/05-monitoring) · [Langfuse tracing quickstart](https://langfuse.com/docs/observability/get-started) · [Langfuse observability data model](https://langfuse.com/docs/observability/data-model)

## Exercise adapted from the Buildcamp

In the trivia homework, students group and price calls to an agent. Here they find the cost of two turns of a speaker conversation, including a retried model call in a separate pricing example. They also explain how a response with an HTTP success code can contain a recoverable tool error. [Buildcamp Week 5 homework](https://github.com/alexeygrigorev/ai-bootcamp/blob/60cc917c776e74d3aaeffb2d24f8f93c320e4b8b/v2/05-monitoring/homework/01-homework.md)

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 11.1 | Tracing a Slow Speaker Question | BC Week 5 overview and `02-logfire/02-logfire-observability.md` |
| 11.2 | Tracing Handbook Search with OpenTelemetry | BC `03-jaeger/01-logfire-jaeger.md` |
| 11.3 | Tracing Model and Tool Calls | BC `03-jaeger/01-logfire-jaeger.md` |
| 11.4 | Viewing Assistant Traces in Langfuse | Langfuse tracing quickstart |
| 11.5 | Finding Timeouts and Retries in a Trace | BC `02-logfire/03-grouping-traces.md` |
| 11.6 | Measuring Token Usage and Cost across a Session | BC Week 5 homework |
| 11.7 | Connecting Speaker Feedback to an Answer | BC `02-logfire/04-tracking-user-feedback.md` |
| 11.8 | Creating Evaluation Cases from Traces | BC `02-logfire/05-downloading-data.md` |

## Detailed lesson outline

### 11.1 Tracing a Slow Speaker Question

See the question, the answer, an eight-second request log entry, and a timeline of that request. A trace groups the operations for the request. Each span records when one operation began and ended. Follow the request through model selection, handbook lookup, and generation.

**Check.** Use the start and end times to identify the slow lookup. Explain how an eight-second request can contain a five-second child span without taking thirteen seconds.

### 11.2 Tracing Handbook Search with OpenTelemetry

Start a request span around the answer function. Inside it, wrap the real search operation in a child span. Add the number of matches and the returned section IDs so a missed retrieval can be investigated later.

**Check.** Run one search that finds “Final Slides” and another with no matches. Inspect the exported spans for parent IDs, distinct trace IDs across requests, and the different retrieval results.

### 11.3 Tracing Model and Tool Calls

Extend the same trace to model calls and tool dispatch. When the agent invokes search as a tool, put the retrieval span inside the tool span. Record usage on each model call. Capture a simulated fetch timeout on the failed attempt and the successful retry as a separate attempt.

**Check.** Reconstruct both attempts from the local export. The failed fetch carries the error, the later fetch returns evidence, and the request completes successfully.

### 11.4 Viewing Assistant Traces in Langfuse

Configure the supplied service's OTLP/HTTP exporter for a class Langfuse instance. Send two near-simultaneous questions, capture the trace ID associated with each response, and find the final-slides lookup in the trace view.

**Check.** Match one response to its exported trace and its retrieved section by ID. For offline grading, perform the same match against the captured export.

### 11.5 Finding Timeouts and Retries in a Trace

Compare a normal request with a slow request for the same question. Both eventually cite the correct passage. Use the timestamps of the failed fetch, retry, and final model call to account for the extra wall-clock time.

**Check.** Name the operation to investigate first, quantify the additional delay against the normal run, and quote the recorded error that explains it.

### 11.6 Measuring Token Usage and Cost across a Session

Group two speaker turns by session ID. Use each model call's own input and output counts and the supplied per-model rates. The pricing fixture includes a charged retry and a nearby turn belonging to another speaker.

**Check.** Report the cost of each turn and their combined cost. Show which call was counted twice in a supplied incorrect total and which unrelated trace belongs outside the session.

### 11.7 Connecting Speaker Feedback to an Answer

A speaker rates the first answer after the second reply has arrived. The feedback event carries the original answer's trace ID. Write a Langfuse score with that ID and inspect the answer and handbook passage together.

**Check.** Demonstrate that the rating lands on the first turn. Compare the speaker's requested deliverable with the section retrieved and explain whether the complaint points to a real error.

### 11.8 Creating Evaluation Cases from Traces

Use the confirmed draft-versus-final mix-up to write a replayable case. Keep the question, handbook version, correct source ID, expected behavior and originating trace ID. Verify the expected deadline against the handbook. Add a successful lookup and a genuinely unanswerable request from the supplied traces.

**Check.** Another learner can label each expected outcome using the supplied handbook alone. The three cases retain their trace IDs and omit speaker identifiers.
