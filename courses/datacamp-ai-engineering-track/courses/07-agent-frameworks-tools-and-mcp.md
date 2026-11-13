# 7. Agent Frameworks, Tools and MCP

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 3. Agents. 7 lessons, 2–3 hours.

## Summary

After writing the loop by hand, learners move to the market-leading framework stack: **LangChain** (21.1% of all jobs; 76.8% of framework adopters) and **LangGraph** (14.4% overall; 71.0% of framework adopters; #1 co-occurring pair at 3.5x lift). They design typed tools for workflow automation, stream agent events, connect agents through the **Model Context Protocol (MCP)**—the fastest-rising skill in the field guide (9.9% → 20.4%)—and compare with PydanticAI.

## Learning objectives

- Rebuild a hand-written agent in LangChain/LangGraph and map each concept to the loop underneath
- Design tools with clear names, docstrings and typed arguments (`@tool` / Pydantic schemas)
- Extend an agent beyond search with tools that automate workflow actions
- Connect an agent to a local MCP server and expose your own tools through MCP
- Compare LangChain/LangGraph with PydanticAI on the same task

## Why here

Frameworks only make sense once the learner knows the loop from course 6; MCP belongs here because it is now the fastest-growing standard for connecting agents to tools (pulling Function Calling and LangGraph at 2.4x lift).

## Transformation

From "I can write an agent loop by hand" to "I can build agents with LangChain/LangGraph and MCP tools, and compare frameworks."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

LangChain `@tool` definitions and `langchain-openai` chat models, LangGraph agent/tool-node loop (`StateGraph` / prebuilt agent), typed tool arguments, structured agent output, streaming events, MCP server over `stdio`, MCP client inside an agent, PydanticAI comparison

### How it's used in the exercises

The learner ports the course-6 agent into LangChain/LangGraph, adds two typed action tools (e.g. creating a ticket or updating a record), watches tool calls in the event stream, starts a local MCP server over `stdio` and connects the agent to it, then implements the same agent in PydanticAI to compare ergonomics.

### Model / release

Python 3.13; `langchain`, `langgraph`, `langchain-openai`, `mcp` Python SDK (versions TBC), `pydantic-ai>=1.55.0`, `toyaikit>=0.0.11`, `openai>=2.38.0`. Small tool-calling model.

### Source material

- **FG** (AI Engineering Field Guide, 9,760 jobs): LangChain 21.1% (76.8% of framework adopters), LangGraph 14.4% (71.0% of framework adopters; #1 pair at 3.5x lift), MCP 15.6% (9.9% → 20.4%, #1 fastest-rising skill), Automating Manual Workflows 58.8%
- **BC**: AI Engineering Buildcamp (`ai-engineering-buildcamp/curriculum.md`) Week 3: Agent Frameworks, Other Agent Frameworks, Model-Context Protocol (MCP)
- **LZ**: LLM Zoomcamp (`github.com/DataTalksClub/llm-zoomcamp`) `01-agentic-rag/15-frameworks.md`, `16-other-frameworks.md`

### Notes

**Reworked from initial draft**: The field guide resolves the framework choice decisively in favor of LangChain + LangGraph as the primary production stack, while keeping Alexey's `toyaikit` (7.1) for transparency and **PydanticAI** (7.7) as a typed-Python alternative. MCP runs over `stdio` with a local server, so no external service is needed.

## Lesson outline and source map

FG = AI Engineering Field Guide, LZ = LLM Zoomcamp path, BC = AI Engineering Buildcamp path. `'new'` = no lesson in LZ or BC.

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 7.1 | Why frameworks: the loop you no longer write | LZ `01-agentic-rag/15-frameworks.md`; BC `v2/03-agents/03-agent-frameworks/02-toyaikit.md` |
| 7.2 | Tools as Python functions and typed schemas | BC `03-agent-frameworks/03-tools-class.md`; LangChain `@tool` |
| 7.3 | Beyond agentic RAG: tools that act | BC `03-agent-frameworks/04-beyond-agentic-rag.md`; FG Automation (58.8%) |
| 7.4 | The agent in LangChain and LangGraph | FG LangChain (76.8% share) + LangGraph (71.0% share); LZ `16-other-frameworks.md` |
| 7.5 | Watching the agent work: events and streaming | BC `03-agent-frameworks/06-event-stream-handlers.md` (adapted to LangGraph streaming) |
| 7.6 | Model Context Protocol (MCP): local servers | BC `v2/03-agents/07-mcp/02-stdio-transport.md`; FG MCP (9.9% → 20.4%) |
| 7.7 | Comparing frameworks: LangGraph vs PydanticAI | BC `03-agent-frameworks/05-pydantic-ai.md`, `06-agent-frameworks-alternatives/02–04` |
