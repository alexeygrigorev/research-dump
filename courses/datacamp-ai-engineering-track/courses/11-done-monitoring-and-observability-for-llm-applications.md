# 11. Monitoring and Observability for LLM Applications - DONE

Part of the [DataCamp AI Engineering track plan](../README.md). Stage: 4. Application quality. 7 lessons, 2-3 hours. Each lesson is designed for approximately 20-25 minutes.

## Summary

Learners add tracing to an AI application and inspect what happened inside a run. They follow model and tool calls, track token costs, and connect user feedback to the relevant answer. They review recorded interactions and turn checked examples into evaluation data.

## Learning objectives

- Instrument model and tool calls and inspect their traces
- Attribute token usage and cost to runs and sessions
- Connect user feedback to the correct answer
- Review traces and build a dataset with checked answers

## Why here

Tests cover known failures; monitoring supplies evidence about individual application runs and new problems.

## Transformation

From "I can see the final answer" to "I can trace the run and turn reviewed failures into evaluation cases."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

Langfuse SDK, wrapped OpenAI client, `@observe`, traces and observations, session IDs, token usage, feedback scores, annotation queues, and dataset items.

### How it's used in the exercises

Learners instrument the existing agent, send requests to the supplied local Langfuse service, inspect traces and costs, attach feedback, review a run, and create a dataset item. A captured trace export supports analysis tasks; it does not replace live model calls.

### Model / release

Python 3.13. `langfuse==5.2.0`, `openai==3.57.0`, `pydantic==2.14.4`. Use DataCamp-funded model API calls. Select the lowest-cost available model that meets the exercise criteria; no fixed model release is required.

### Source material

- [AI Shipping Labs Langfuse workshop](https://github.com/AI-Shipping-Labs/workshops/tree/main/2026/2026-11-04-langfuse-tracing): `README.md`, `agent.py`, and `search.py` cover the wrapped OpenAI client, `@observe`, and trace inspection. `evals/setup_review_queue.py` and `evals/queue_to_dataset.py` cover human review and promotion of checked traces into a dataset.
- Buildcamp Week 5 supplies the session-cost and feedback exercise patterns. [Buildcamp monitoring](https://github.com/alexeygrigorev/ai-bootcamp/tree/60cc917c776e74d3aaeffb2d24f8f93c320e4b8b/v2/05-monitoring).

### Notes

Provide a preconfigured, locally hosted Langfuse service in the exercise workspace and project credentials for that service. Learners do not create an external account. Configure and trace calls before combining feedback with human review.

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 11.1 | Introduction to LLM Observability | Workshop `README.md` |
| 11.2 | Tracing Agents and Tools | Workshop `README.md`, `app.py`; Workshop `agent.py`, `search.py` |
| 11.3 | Inspecting Agent Traces | Workshop `README.md`, `agent.py` |
| 11.4 | Tracking Tokens and Costs | Buildcamp Week 5 homework |
| 11.5 | User Feedback | Buildcamp user feedback |
| 11.6 | Human Review | Workshop `evals/setup_review_queue.py` |
| 11.7 | Building Datasets from Traces | Workshop `evals/queue_to_dataset.py` |

## Detailed lesson outline

### 11.1 Introduction to LLM Observability

Open a recorded Langfuse trace for one question. Find the input, answer, model call, and search result. Introduce a trace as one run and observations as the operations inside it.

**Check.** Match the question and answer to the correct trace and identify the retrieval observation.

### 11.2 Tracing Agents and Tools

Configure the supplied Langfuse project and replace the OpenAI client with the Langfuse wrapper. Send one request and flush pending events before the short script exits.

**Check.** Locate the model input, output, and token usage in Langfuse. Offline exercises inspect the captured request and export.

Add `@observe` to the agent, tool, and retrieval functions, following the workshop code. Nest model calls and retrieval under the agent run.

**Check.** Verify that each observation belongs to the correct run and that tool arguments and retrieved source IDs are visible.

### 11.3 Inspecting Agent Traces

Compare two questions sent close together. Follow one run through its model calls, tool calls, retrieved passages, and final answer.

**Check.** Use trace and observation IDs to match each answer to its evidence without mixing the two requests.

### 11.4 Tracking Tokens and Costs

Group two conversation turns by session ID. Inspect each model call's token usage and calculate costs with the supplied rates, including a charged retry.

**Check.** Report per-turn and session totals and exclude an unrelated nearby trace.

### 11.5 User Feedback

Attach a user rating to the original answer's trace ID even after a follow-up has arrived. Inspect the rated answer and use the feedback to select traces for review.

**Check.** Verify that the rating reaches the intended answer rather than the most recent turn.

### 11.6 Human Review

Add selected traces to a Langfuse annotation queue. Compare each answer with the handbook and its cited evidence. Record a correctness verdict and a correction where needed.

**Check.** Complete a review of an incorrect answer with a corrected expected answer. Confirm that a user rating alone does not count as a completed review.

### 11.7 Building Datasets from Traces

Follow the workshop queue-to-dataset flow. Promote completed reviews with a confirmed correct answer or human correction. Preserve the question, expected answer, source trace ID, and supporting source IDs.

**Check.** Skip unreviewed traces, keep the corrected deadline as the expected answer, and prevent a second promotion of the same trace.
