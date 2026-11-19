# 6. Building Agents with LangChain and Pydantic AI

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 3. Agents. 6 lessons, 2-3 hours.

## Summary

Learners rebuild the internal knowledge agent in LangChain, define typed workflow tools, and stream responses. The exercises follow the Buildcamp progression from a hand-written loop to reusable tools and then a framework-based assistant. One lesson introduces PydanticAI by porting the search-and-fetch agent.

## Learning objectives

- Map LangChain's agent and tool interfaces to the loop built in the previous course
- Define typed retrieval and workflow tools with clear descriptions
- Build an agent that searches the knowledge base and writes a draft ticket to a local fixture
- Stream text and tool progress from the agent
- Build a small agent with PydanticAI and compare how it declares tools and output types

## Why here

Learners can connect framework behavior to the code they already wrote. They use the LangChain agent again in the MCP and guardrails courses. The multi-agent course introduces LangGraph explicitly.

## Transformation

From writing a tool loop by hand to building and streaming a LangChain agent with reusable tools.

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

LangChain agent creation, typed Python tool functions, tool descriptions, structured output, streaming, PydanticAI tool registration.

### How it's used in the exercises

Port the search and fetch tools to LangChain and run a supplied request to verify that the agent uses the returned document ID. Add a tool that writes a draft support ticket and a schema for the assistant's response. Stream the answer and tool progress. Rebuild the small search-and-fetch example in PydanticAI as a short comparison.

### Model / release

Python 3.13, LangChain, the LangChain OpenAI integration, and PydanticAI for the comparison lesson. Use a small OpenAI tool-calling model and scripted responses for graded exercises.

### Source material

- **BC** Week 3 Agent Frameworks, especially `v2/03-agents/03-agent-frameworks/`.
- **LZ** `01-agentic-rag/15-frameworks.md` and `01-agentic-rag/16-other-frameworks.md`.
- **FG** LangChain appears in 21.1% of all roles and 76.8% of framework adopters. Automating manual workflows appears in 58.8% of roles.

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 6.1 | Building a LangChain agent | BC `v2/03-agents/03-agent-frameworks/02-toyaikit.md`; LZ `01-agentic-rag/15-frameworks.md` |
| 6.2 | Defining tools | BC `v2/03-agents/03-agent-frameworks/03-tools-class.md` |
| 6.3 | Adding a workflow tool | BC `v2/03-agents/03-agent-frameworks/04-beyond-agentic-rag.md` |
| 6.4 | Returning structured results | BC `v2/01-foundation/04-structured-output/01-structured-output.md` |
| 6.5 | Streaming | BC `v2/03-agents/03-agent-frameworks/06-event-stream-handlers.md` |
| 6.6 | Building a small agent with PydanticAI | BC `v2/03-agents/03-agent-frameworks/05-pydantic-ai.md` |

## Detailed lesson outline

### 6.1 Building a LangChain agent

Port the support assistant’s manual tool loop to a LangChain agent with the same search tool.

**Check.** Run a fixed request and verify it still reaches the expected tool.

### 6.2 Defining tools

Define typed tools for searching and fetching support articles. Write descriptions that tell the agent when to use each tool.

**Check.** Validate a correct invocation and reject malformed arguments.

### 6.3 Adding a workflow tool

Add a tool that drafts a support ticket in a local fixture. Give the agent a request that needs follow-up.

**Check.** Check the draft contains the issue and supporting reference.

### 6.4 Returning structured results

Define a structured answer containing a response and supporting source IDs.

**Check.** Parse the agent result and verify the schema and cited IDs.

### 6.5 Streaming

Subscribe to streamed agent events and display the answer as text arrives.

**Check.** Reconstruct the final answer from the stream and identify the tool event.

### 6.6 Building a small agent with PydanticAI

Build a small PydanticAI agent around the same read-only lookup function.

**Check.** Run the same fixture and identify where tool registration and output types are defined.


can we actually give them more tools not just read
