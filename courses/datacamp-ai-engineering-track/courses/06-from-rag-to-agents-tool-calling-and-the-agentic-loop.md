# 6. From RAG to Agents: Tool Calling and the Agentic Loop

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 3. Agents. 6 lessons, 2–3 hours.

## Summary

In RAG the developer decides when to search. In an agent the model decides. Learners give the model a search tool, implement the tool-call loop by hand, and turn the fixed RAG pipeline into agentic RAG.

## Learning objectives

- Describe a tool to an LLM with a function schema and execute the call it requests
- Implement the agentic loop: call the model, run tools, return results, repeat until done
- Convert a fixed RAG pipeline into agentic RAG that can search several times
- Decide when a fixed pipeline is enough and when an agent is worth the extra cost

## Why here

First agents course: it reuses the RAG assistant the learner already knows and builds the loop from scratch before any framework hides it.

## Transformation

From "my code tells the LLM what to do at each step" to "I can build an agent that decides which tools to call and when."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

Tool/function definitions (JSON schema), function_call and function_call_output messages, the while-loop over tool calls, conversation state, stop conditions and iteration limits

### How it's used in the exercises

The learner writes the search function schema, sends a question, inspects the tool call the model returns, executes it and sends the result back. They then wrap these steps in a loop and compare the agent's answers and number of LLM calls with the fixed RAG pipeline.

### Model / release

Python 3.13; openai>=2.38.0, minsearch>=0.1.0. A small model with tool calling (OpenAI, Claude or DeepSeek).

### Source material

- LLM Zoomcamp (github.com/DataTalksClub/llm-zoomcamp) Module 1 Agentic RAG, lessons 11–14
- AI Engineering Buildcamp (Maven course; repo ai-engineering-buildcamp, curriculum.md) Week 3: Agent Basics; Alternatives to OpenAI: Tool Calling

### Notes

No framework in this course on purpose. One lesson repeats tool calling with a second provider to keep the concept portable.

## Lesson outline and source map

LZ = LLM Zoomcamp path, BC = AI Engineering Buildcamp path. 'new' = no lesson in either source.

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 6.1 | From RAG to agents | LZ 01-agentic-rag/11-agents-intro.md, 12-rag-revision.md |
| 6.2 | Function calling | LZ 13-function-calling.md; BC v2/03-agents/02-agent-basics/02-agentic-rag-tool-calling.md |
| 6.3 | The agentic tool-call loop | LZ 14-agentic-loop.md; BC 02-agent-basics/03-agentic-loop.md |
| 6.4 | A conversational Q&A loop | BC 02-agent-basics/04-qna-loop.md |
| 6.5 | Tool calling with other providers | BC v2/03-agents/05-openai-alternatives/04-chat-completions.md, 05-anthropic.md |
| 6.6 | Agent or pipeline? Cost and control | BC 02-agent-basics/06-visual-summary.md; LZ 10-rag-next-steps.md |
