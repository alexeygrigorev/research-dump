# 1. Working with LLM APIs

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 1. Foundations. 6 lessons, 2-3 hours.

## Summary

Learners use the OpenAI Responses API from Python. They send instructions and conversation messages, read token usage, and extract validated fields from a document. The examples adapt the Buildcamp’s documentation assistant to the track’s internal knowledge base.

## Learning objectives

- Call an LLM from Python and control its behaviour with instructions and message history
- Estimate token usage and cost and pick the cheapest model that does the job
- Define a Pydantic schema and get validated structured output from a model
- Stream a response and handle an incomplete result

## Why here

RAG, tool calling, and model-based evaluation all depend on sending requests and handling model responses. The document example prepares learners to add retrieval in the next course.

## Transformation

From using an LLM through a chat window to calling OpenAI from Python and validating the response.

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

OpenAI Responses API calls, instructions and conversation messages, token usage fields, Pydantic models, structured output, and streaming.

### How it's used in the exercises

The learner sends a request about a supplied internal policy excerpt and carries it forward into a follow-up turn. They estimate cost using token counts and a supplied price table. They then define a Pydantic model for extracting a policy title, owner, and review date, validate the extracted fields, and stream the response. Grade request construction and schema validation with fixed responses.

### Model / release

Python 3.13, `openai>=2.15.0`, Pydantic, and `python-dotenv>=1.2.1`. Use a small OpenAI model that supports structured output.

### Source material

- **FG** Python appears in 71.6% of all AI engineer roles and integrating APIs and services appears in 55.8% of responsibilities.
- **BC** Week 1 OpenAI API, Documentation Agent, and Structured Output. Token cost practice draws on Week 4.
- **LZ** `01-agentic-rag/07-llm.md`.

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 1.1 | Your first OpenAI API call from Python | BC `v2/01-foundation/03-rag/03-openai-api.md`; LZ `01-agentic-rag/07-llm.md` |
| 1.2 | Instructions and conversation history | BC `v2/01-foundation/03-rag/03-openai-api.md` |
| 1.3 | Token usage and cost | BC `v2/04-testing/03-testing/06-tracking-costs.md` |
| 1.4 | Structured output with Pydantic | BC `v2/01-foundation/04-structured-output/01-structured-output.md` |
| 1.5 | Extracting fields from a document | BC `v2/01-foundation/04-structured-output/02-documentation-rag-structured-output.md` |
| 1.6 | Streaming responses | BC `v2/01-foundation/04-structured-output/03-streaming-structured-output.md` |
