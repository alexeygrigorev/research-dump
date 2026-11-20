# 11. Monitoring and Observability for LLM Applications

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 4. Application quality. 8 lessons, 2–3 hours.

## Summary

Learners add Langfuse tracing to the existing assistant, inspect model and tool calls, and investigate slow or incorrect answers. They track costs, review feedback, and turn checked traces into evaluation data.

## Learning objectives

- Explain traces and observations using a recorded agent run
- Trace model calls with the Langfuse OpenAI wrapper and functions with `@observe`
- Inspect latency, errors, token usage, and session costs
- Review traces and promote human-checked answers or corrections into evaluation data

## Why here

The tests from course 10 can reproduce known failures. This course helps learners investigate an individual run whose cause they do not yet know. Course 12 uses examples discovered in those runs to build an evaluation dataset.

## Transformation

Given a complaint, learners can find the affected turn, identify the step responsible, and gather evidence for a fix.

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

Langfuse SDK, wrapped OpenAI client, `@observe`, traces and observations, session IDs, token usage, feedback scores, annotation queues, and dataset items.

### How it's used in the exercises

Supply the assistant, a Langfuse project or captured exports, and a two-turn session with a slow lookup and an incorrect answer. Learners trace the agent with the SDK, inspect the recorded runs, attach feedback, review the answer, and prepare a dataset item with a human-checked expected answer.

### Model / release

Python 3.13, Langfuse Python SDK, OpenAI, and the existing assistant. Use a class Langfuse project for the walkthrough and captured traces, scores, and queue items for offline grading. Pin the SDK against the exercise runtime.

### Source material

- [AI Shipping Labs Langfuse workshop](https://github.com/AI-Shipping-Labs/workshops/tree/main/2026/2026-11-04-langfuse-tracing): `README.md`, `agent.py`, and `search.py` cover the wrapped OpenAI client, `@observe`, and trace inspection. `evals/setup_review_queue.py` and `evals/queue_to_dataset.py` cover human review and promotion of checked traces into a dataset.
- Buildcamp Week 5 supplies the session-cost and feedback exercise patterns. [Buildcamp monitoring](https://github.com/alexeygrigorev/ai-bootcamp/tree/60cc917c776e74d3aaeffb2d24f8f93c320e4b8b/v2/05-monitoring).

## Exercise adapted from the workshop

Replace the workshop FAQ corpus with the speaker handbook. Keep its progression: wrap model calls, observe the agent and retrieval functions, inspect traces, then review selected answers. Promote a trace only after a human confirms the observed answer or supplies a correction; feedback alone does not establish ground truth. Recorded exports support exercises without a live Langfuse project.

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 11.1 | Introduction to LLM Observability | Workshop `README.md` |
| 11.2 | Setting Up Langfuse | Workshop `README.md`, `app.py` |
| 11.3 | Tracing Agents and Tools | Workshop `agent.py`, `search.py` |
| 11.4 | Inspecting Traces | Workshop `README.md`, `agent.py` |
| 11.5 | Debugging Slow Requests | Buildcamp Week 5; new timeout fixture |
| 11.6 | Session Costs | Buildcamp Week 5 homework |
| 11.7 | Feedback and Human Review | Workshop `evals/setup_review_queue.py`; Buildcamp user feedback |
| 11.8 | From Traces to Datasets | Workshop `evals/queue_to_dataset.py` |

## Detailed lesson outline

### 11.1 Introduction to LLM Observability

Open a recorded Langfuse trace for one question. Find the input, answer, model call, and search result. Introduce a trace as one run and observations as the operations inside it.

**Check.** Match the question and answer to the correct trace and identify the retrieval observation.

### 11.2 Setting Up Langfuse

Configure the supplied Langfuse project and replace the OpenAI client with the Langfuse wrapper. Send one request and flush pending events before the short script exits.

**Check.** Locate the model input, output, and token usage in Langfuse. Offline exercises inspect the captured request and export.

### 11.3 Tracing Agents and Tools

Add `@observe` to the agent, tool, and retrieval functions, following the workshop code. Nest model calls and retrieval under the agent run.

**Check.** Verify that each observation belongs to the correct run and that tool arguments and retrieved source IDs are visible.

### 11.4 Inspecting Traces

Compare two questions sent close together. Follow one run through its model calls, tool calls, retrieved passages, and final answer.

**Check.** Use trace and observation IDs to match each answer to its evidence without mixing the two requests.

### 11.5 Debugging Slow Requests

Compare a normal request with a slow request containing a simulated fetch timeout and retry. Inspect errors and observation timings.

**Check.** Identify the failed attempt and successful retry, and account for the extra wall-clock time without adding overlapping durations twice.

### 11.6 Session Costs

Group two conversation turns by session ID. Inspect each model call's token usage and calculate costs with the supplied rates, including a charged retry.

**Check.** Report per-turn and session totals and exclude an unrelated nearby trace.

### 11.7 Feedback and Human Review

Attach a rating to the original answer's trace ID even after a follow-up has arrived. Add selected traces to an annotation queue and compare the answer with the handbook. Record a correctness verdict and a correction where needed.

**Check.** Verify that the rating reaches the intended answer and that the reviewer checks the cited evidence.

### 11.8 From Traces to Datasets

Follow the workshop queue-to-dataset flow. Promote completed reviews with a confirmed correct answer or human correction. Preserve the question, expected answer, source trace ID, and supporting source IDs.

**Check.** Skip unreviewed traces, keep the corrected deadline as the expected answer, and prevent a second promotion of the same trace.
