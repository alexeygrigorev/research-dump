# 6. Building Agents with LangChain and Pydantic AI - DONE

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 3. Agents. 6 lessons, 2–3 hours.

## Summary

Learners build an agent using typed Python tools and an agent framework. They add read and write operations, validate structured replies, and stream progress. They reuse the tools in a small alternative-framework implementation to identify which parts depend on the framework.

## Learning objectives

- Register typed read and write tools with an agent framework
- Return validated structured agent output
- Stream tool progress and answer text
- Reuse tool functions in another framework and compare the implementations

## Why here

Builds on the manual loop so learners can recognize what a framework manages. Supplies the agent and tool functions used by the MCP and workflow courses.

## Transformation

From "I can write an agent loop" to "I can build a tool-using agent with reusable functions and validated output."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

LangChain `create_agent`, Python tool functions with type hints and docstrings, Pydantic result models, message and tool events, and Pydantic AI tool registration.

### How it's used in the exercises

Supply a small rehearsal schedule and an in-memory draft store alongside the handbook index. A draft records the issue, speaker's requested change and supporting references. Creating one returns a draft ID. Updating one requires that ID. Learners inspect the store after each run. Submitting a draft to the ticket queue is introduced in course 13.

### Model / release

Python 3.13. `openai==3.57.0`, `pydantic==2.14.4`, `langchain==1.5.2`, `langchain-openai==1.8.5`, `pydantic-ai-slim==2.71.0`. Use DataCamp-funded model API calls; no fixed model release is required. MCP processes run locally over stdio and require no external account.

### Source material

- **BC** Week 3 Agent Frameworks covers reusable tools, Pydantic AI and event streaming. The framework alternatives section includes a LangChain implementation. The draft tools are a new exercise.
- **LZ** Module 1, lessons 15–16, compares the manual loop with framework implementations.
- **FG** LangChain appears in 21.1% of sampled roles. Automating manual workflows appears in 58.8%.

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 6.1 | Agents with LangChain | BC `v2/03-agents/06-agent-frameworks-alternatives/03-langchain.md`, LZ `01-agentic-rag/15-frameworks.md` |
| 6.2 | Defining Typed Tools | BC `v2/03-agents/03-agent-frameworks/03-tools-class.md`, adapted to schedule data |
| 6.3 | Reading and Writing Data with Tools | New workflow exercise extending the BC tool collection |
| 6.4 | Structured Agent Output | BC `v2/03-agents/02-agent-basics/05-structured-output.md` |
| 6.5 | Streaming Agent Events | BC `v2/03-agents/03-agent-frameworks/06-event-stream-handlers.md` |
| 6.6 | Agents with Pydantic AI | BC `v2/03-agents/03-agent-frameworks/05-pydantic-ai.md` |

## Detailed lesson outline

### 6.1 Agents with LangChain

Register course 5's search and fetch functions with a LangChain agent. Run the same rehearsal-policy question. Match the tool request, result and final message to the steps in the manual loop.

**Check.** Compare the two traces. In each, the fetched section ID must come from the search results and appear in the answer.

### 6.2 Defining Typed Tools

Add a typed tool that takes a speaker ID and returns that speaker's rehearsal slot, time and room. Write a description that distinguishes an individual booking from general handbook policy.

**Check.** Inspect the advertised schema. Call the tool for two speakers and an unknown ID. Verify that each known booking comes from the matching row and that the missing booking is reported.

### 6.3 Reading and Writing Data with Tools

Implement create and update tools around the supplied draft store. Ask for a draft about a rehearsal conflict, then say “Add that I can do Friday afternoon.” Pass the first tool's draft ID into the update.

**Check.** Inspect the store. It must contain one draft with the correction and original references. An update for an unknown ID must return an error and leave existing drafts intact.

### 6.4 Structured Agent Output

Define a reply with answer text, source IDs and an optional draft ID. Return it from a handbook-only request and from a request to draft a ticket.

**Check.** Parse both replies. Match cited sections to the fetched evidence and the returned draft ID to the stored draft. The handbook-only request should leave the store empty.

### 6.5 Streaming Agent Events

Add a stream consumer to the rehearsal lookup. Show that the booking arrived, then display answer text as it becomes available. Use a supplied sequence of events that includes tool-call arguments and a tool result.

**Check.** Verify that the progress message follows the tool result, assembled answer text matches the completed response, and tool-call arguments stay out of the speaker-facing text.

### 6.6 Agents with Pydantic AI

Use a starter Pydantic AI agent. Register the existing rehearsal lookup and draft-creation functions and declare the same reply type. Replay the request against a fresh draft store.

**Check.** Compare the LangChain and Pydantic AI runs on booking references, stored draft contents and result fields. Identify the tool registration and result declarations that changed in the port.
