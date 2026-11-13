# 1. Working with LLM APIs

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 1. Foundations. 6 lessons, 2–3 hours.

## Summary

Learners call LLMs from Python code (required in 71.6% of all AI engineer jobs, 75.9% of AI-First) instead of a chat window. They send requests to OpenAI, Claude and DeepSeek APIs, apply prompt engineering (34.8% of jobs), control cost with tokens and model choice, and get typed, validated answers with structured output.

## Learning objectives

- Call an LLM from Python and control its behaviour with instructions and message history
- Compare provider APIs (OpenAI Responses, Chat Completions, Anthropic) and switch a program between them
- Estimate token usage and cost and pick the cheapest model that does the job
- Define a Pydantic schema and get validated structured output from a model

## Why here

Everything later (RAG, agents, judges) is built from these same Python API calls, prompt engineering, and structured outputs, so they come first.

## Transformation

From "I have used an LLM in a chat window" to "I can call any of the main LLM APIs from Python and get reliable, typed output back."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

Responses API and Chat Completions API calls, Anthropic Messages API, system/developer instructions, message history, token usage fields, Pydantic models, structured output parsing, streaming

### How it's used in the exercises

The learner writes short Python scripts that send a prompt, read the response object and token usage, then rewrite the same call for a second provider. They define a Pydantic class for extracting structured fields from a document and check that the parsed output passes validation.

### Model / release

Python 3.13; `openai>=2.15.0`, `anthropic>=0.76.0`, `pydantic` (version TBC), `python-dotenv>=1.2.1`. Models: smallest available OpenAI, Claude and DeepSeek chat models (DeepSeek through the Chat Completions-compatible API).

### Source material

- **FG** (AI Engineering Field Guide, 9,760 jobs): Python 71.6% (75.9% AI-First), Prompt Engineering 34.8% (rising 26.1% → 34.2%), APIs 2,515 jobs, OpenAI API 14.6%, integrator stack 91.7% of AI-First roles in Nov
- **BC**: AI Engineering Buildcamp (`ai-engineering-buildcamp/curriculum.md`) Week 1: OpenAI API (Responses API), Structured output, OpenAI Alternatives
- **LZ**: LLM Zoomcamp (`github.com/DataTalksClub/llm-zoomcamp`) `01-agentic-rag/07-llm.md`

### Notes

Bedrock, Groq and Gemini lessons are dropped because DataCamp does not provide them. DeepSeek is included via the Chat Completions-compatible API.

## Lesson outline and source map

FG = AI Engineering Field Guide, LZ = LLM Zoomcamp path, BC = AI Engineering Buildcamp path. `'new'` = no lesson in LZ or BC.

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 1.1 | Your first LLM call from Python | BC `v2/01-foundation/03-rag/03-openai-api.md`; LZ `01-agentic-rag/07-llm.md` |
| 1.2 | Prompt engineering: instructions, messages and history | BC `03-openai-api.md`; FG Prompt Engineering (34.8%) |
| 1.3 | Tokens, cost and choosing the most efficient model | BC `v2/04-testing/03-testing/06-tracking-costs.md` (cost idea introduced early) |
| 1.4 | Other providers: Chat Completions and Anthropic | BC `v2/01-foundation/06-alternatives/02-chat-completions.md`, `04-anthropic.md` |
| 1.5 | Structured output with Pydantic | BC `v2/01-foundation/04-structured-output/01-structured-output.md` |
| 1.6 | Streaming responses and streaming structured output | BC `04-structured-output/03-streaming-structured-output.md` |
