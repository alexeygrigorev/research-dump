# 7. Agent Frameworks, Tools and MCP

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 3. Agents. 7 lessons, 2–3 hours.

## Summary

After writing the loop by hand, learners move to a framework. They rebuild the agent with a framework, design good tools, give the agent more than search, and expose and consume tools through the Model Context Protocol.

## Learning objectives

- Rebuild a hand-written agent in a framework and map each framework concept to the loop underneath
- Design tools with clear names, docstrings and typed arguments
- Extend an agent beyond search with tools that act
- Connect an agent to a local MCP server and expose your own tools through MCP
- Compare frameworks on the same task

## Why here

Frameworks only make sense once the learner knows the loop from course 6; MCP belongs here because it is the standard way to share tools.

## Transformation

From "I can write an agent loop by hand" to "I can build agents with a framework and reusable tools, and I know what the framework does for me."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

Agent class, tool registration, typed tool arguments, structured agent output, event/stream handlers, MCP server over stdio, MCP client inside an agent; short comparison of the same agent in a second framework

### How it's used in the exercises

The learner ports the course-6 agent into the framework, adds two new tools as plain Python functions, watches the tool calls in the event stream, then starts a small local MCP server and connects the agent to it.

### Model / release

Python 3.13; pydantic-ai>=1.55.0, toyaikit>=0.0.11, openai>=2.38.0, MCP Python SDK (version TBC), langchain or openai-agents (version TBC, comparison lesson). Small tool-calling model.

### Source material

- AI Engineering Buildcamp (Maven course; repo ai-engineering-buildcamp, curriculum.md) Week 3: Agent Frameworks, Other Agent Frameworks, Model-Context Protocol (MCP)
- LLM Zoomcamp (github.com/DataTalksClub/llm-zoomcamp) 01-agentic-rag/15-frameworks.md, 16-other-frameworks.md

### Notes

Open question: the Buildcamp teaches PydanticAI as the main framework; the brief asks for the most widely used one. Draft keeps PydanticAI as main and a comparison lesson (OpenAI Agents SDK / LangChain). MCP only over stdio with a local server, so no external service.

## Lesson outline and source map

LZ = LLM Zoomcamp path, BC = AI Engineering Buildcamp path. 'new' = no lesson in either source.

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 7.1 | Why frameworks: the loop you no longer write | LZ 01-agentic-rag/15-frameworks.md; BC v2/03-agents/03-agent-frameworks/02-toyaikit.md |
| 7.2 | Tools as Python functions and classes | BC 03-agent-frameworks/03-tools-class.md |
| 7.3 | Beyond agentic RAG: tools that act | BC 03-agent-frameworks/04-beyond-agentic-rag.md |
| 7.4 | The agent in a production framework | BC 03-agent-frameworks/05-pydantic-ai.md |
| 7.5 | Watching the agent work: events and streaming | BC 03-agent-frameworks/06-event-stream-handlers.md |
| 7.6 | Model Context Protocol: local servers | BC v2/03-agents/07-mcp/02-stdio-transport.md, 03-sse-transport.md |
| 7.7 | Comparing frameworks | BC v2/03-agents/06-agent-frameworks-alternatives/02–04; LZ 16-other-frameworks.md |
