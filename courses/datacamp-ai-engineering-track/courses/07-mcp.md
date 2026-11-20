# 7. Model Context Protocol (MCP)

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 3. Agents. 5 lessons, 2–3 hours.

## Summary

The speaker assistant and an organizer's lookup script both need the same handbook. Learners use MCP to discover which tools a separately running server offers and call one by its advertised name and schema. They then publish their own search and fetch functions and connect both applications to them.

## Learning objectives

- Trace a tool request through an MCP host, its client and the tool server.
- Discover a server's tool names and input schemas and call one from Python.
- Expose handbook search and fetch tools from a local server over standard input and output (stdio).
- Connect the course 6 LangChain agent to the server and diagnose a failed lookup.

## Why here

Learners already own working Python tools and an agent that can call them. The organizer's script introduces a second consumer. Both can use the handbook service while the assistant keeps its own rehearsal and draft tools.

## Transformation

Learners can publish a Python function once and use its advertised interface from two applications.

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

MCP hosts and clients, local stdio transport, tool descriptions and input schemas, `tools/list`, `tools/call`, tool results, connection errors and a LangChain MCP adapter.

### How it's used in the exercises

Start with a working handbook server and an organizer's script. After inspecting the exchange, implement the same tool interface over the course 5 index. Give the LangChain assistant the discovered tools and rerun its rehearsal-policy question. Compare the section IDs returned to the script and agent.

### Model / release

Python 3.13, Python MCP SDK and the course 6 LangChain stack with a compatible MCP adapter. The standalone client calls need no model. Grade the agent with a scripted model. Where subprocesses are unavailable, run the learner's handlers through an in-process client/server fixture and supply a recorded stdio exchange for the transport exercise.

### Source material

- **BC** Week 3 MCP introduces the protocol and local stdio transport. Its original worked example shows the connection and server implementation in `old/02-agents/50-mcp.md`.
- **FG** MCP appears in 15.6% of sampled roles.
- The MCP documentation illustrates discovery and execution. LangChain documents how to adapt discovered tools for its agents. [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture) · [LangChain MCP integration](https://docs.langchain.com/oss/python/langchain/mcp)

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 7.1 | Introduction to MCP | BC `v2/03-agents/07-mcp/01-section-overview.md`, MCP architecture |
| 7.2 | MCP Clients | MCP tool discovery and execution examples |
| 7.3 | Building an MCP Server | BC `v2/03-agents/07-mcp/02-stdio-transport.md` and `old/02-agents/50-mcp.md` |
| 7.4 | MCP Tools in LangChain | LangChain MCP integration, adapted to the course 6 assistant |
| 7.5 | Debugging MCP Connections | New exercise using the handbook server and client |

## Detailed lesson outline

### 7.1 Introduction to MCP

Watch the organizer's script and the speaker assistant look up the same handbook section through a supplied server. Follow one request from the host application through its client to the process that owns the handbook index.

**Check.** Label the three roles in the trace and identify which component reads the handbook and which chooses the tool for the speaker's question.

### 7.2 MCP Clients

Connect the organizer's script to the supplied server. List its tools and inspect the input schema for fetch. Use the client to search for rehearsal policy and fetch the section by the returned ID.

**Check.** Inspect the outgoing call and returned passage. The argument name must match the discovered schema and the section ID must come from the search response.

### 7.3 Building an MCP Server

Wrap course 5's search and fetch functions as server tools. Give each its typed arguments and description. Use the provided launcher to run the server over stdio, then point the organizer's script at it.

**Check.** From the client, discover both tools and retrieve a section added to the local handbook fixture. Match its ID and text to the new fixture entry.

### 7.4 MCP Tools in LangChain

Register the discovered handbook tools alongside the assistant's local schedule and draft tools. Ask how a speaker can change a rehearsal, then ask for their current slot.

**Check.** Inspect the server and local tool logs. The policy question must fetch the cited section from the server. The booking lookup must use the local schedule and return the fixture slot.

### 7.5 Debugging MCP Connections

Compare a call for a missing section with a call made while the server is unavailable. Use the client evidence to identify where each failure occurred and give the speaker an appropriate response.

**Check.** For a missing ID, show the server's completed lookup and its missing-section result. For the unavailable server, identify the transport failure. In both cases verify the assistant reports the missing evidence.
