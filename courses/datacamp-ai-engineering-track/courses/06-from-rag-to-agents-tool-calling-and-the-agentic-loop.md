# 6. From RAG to Agents: Tool Calling and the Agentic Loop

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 3. Agents. 5 lessons, 2-3 hours.

## Summary

In RAG the developer decides when to search; in an agent (56.2% of all jobs, 74.0% of AI-First roles) the model decides. Learners implement function calling (9.6% → 18.5%, #2 fastest-rising skill) and the tool-call loop by hand, turning fixed RAG into agentic RAG (RAG + Agents together rose from 33.1% to 51.0% of AI-First postings).

## Learning objectives

- Describe a tool to an LLM with a function schema and execute the call it requests
- Implement the agentic loop: call the model, run tools, return results, repeat until done
- Convert a fixed RAG pipeline into agentic RAG that can search and act across steps
- Carry conversation history across turns and limit how many times the agent can call tools

## Why here

First agents course: Agent builder is the #1 role archetype (29.9%), and RAG + Agents together now appear in 51.0% of AI-First jobs. Building the loop from scratch makes frameworks transparent in course 7.

## Transformation

From "my code tells the LLM what to do at each step" to "I can build an agent that decides which tools to call and when."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

Tool/function definitions (JSON schema), `function_call` and `function_call_output` messages, the `while`-loop over tool calls, conversation state, stop conditions and iteration limits

### How it's used in the exercises

The learner writes the search and fetch function schemas, sends a request, inspects the tool call the model returns, executes it and sends the result back. They then wrap these steps in a loop and compare the agent's answers and number of LLM calls with the fixed RAG pipeline.

### Model / release

Python 3.13; `openai>=2.38.0`, `minsearch>=0.1.0`. A small OpenAI model with tool calling through the Responses API.

### Source material

- **FG** (AI Engineering Field Guide, 9,760 jobs): Agents (any) 56.2% (74.0% AI-First), Agent builder archetype 29.9%, Function Calling 15.1% (9.6% → 18.5%, +0.88 pp/scrape), RAG + Agents together 51.0% of AI-First, agents responsibility in 53.3% of all jobs (55.8% in Nov)
- **FG learning paths / portfolio** (`learning-paths/README.md`, `portfolio/`, commit `1556dcb2`): "AI Agents" block starts with function calling and "the agentic tool-call loop" before frameworks, the same order as courses 6 → 7.
- **LZ**: LLM Zoomcamp (`github.com/DataTalksClub/llm-zoomcamp`) Module 1 Agentic RAG, lessons 11-14
- **BC**: AI Engineering Buildcamp (`ai-engineering-buildcamp/curriculum.md`) Week 3: Agent Basics

### Notes

Exercises use the OpenAI SDK directly. The multi-agent course revisits when to choose a fixed pipeline.

## Exercise adapted from the Buildcamp

Adapt the Wikipedia agent homework to the internal knowledge base with two read-only tools: search for documents and fetch one by ID. Provide scripted model responses for a direct fetch and a search followed by a fetch. Learners dispatch each tool, return its result to the model, and stop when the model produces a final answer. Grade the tool sequence, the ID passed to fetch, and the termination condition.

[Buildcamp Week 3 source](https://github.com/alexeygrigorev/ai-bootcamp/blob/60cc917c776e74d3aaeffb2d24f8f93c320e4b8b/v2/03-agents/homework/01-homework.md)

## Lesson outline and source map

FG = AI Engineering Field Guide, LZ = LLM Zoomcamp path, BC = AI Engineering Buildcamp path. `'new'` = no lesson in LZ or BC.

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 6.1 | From RAG to agents | LZ `01-agentic-rag/11-agents-intro.md`, `12-rag-revision.md`; FG Agents (56.2%) |
| 6.2 | Function calling | LZ `13-function-calling.md`; BC `v2/03-agents/02-agent-basics/02-agentic-rag-tool-calling.md`; FG Function Calling (18.5% Nov) |
| 6.3 | The agentic tool-call loop | LZ `14-agentic-loop.md`; BC `02-agent-basics/03-agentic-loop.md` |
| 6.4 | Carrying conversation history across turns | BC `v2/03-agents/02-agent-basics/04-qna-loop.md` |
| 6.5 | Handling tool errors and limiting iterations | new; extends BC `v2/03-agents/02-agent-basics/03-agentic-loop.md` |
