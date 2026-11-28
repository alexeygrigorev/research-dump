# 7. Model Context Protocol (MCP)

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 3. Agents. 5 lessons, 2–3 hours.

## Summary

Learners expose Python tools through the Model Context Protocol and call them from multiple applications. They discover advertised tool schemas, implement a local server, and connect it to the existing agent. They learn to distinguish a tool error from a connection failure.

## Learning objectives

- Explain the roles of an MCP host, client, and server
- Discover tool schemas and call tools from a client
- Expose Python functions through a local MCP server
- Connect the agent to MCP tools and diagnose failed calls

## Why here

Requires working tools and an agent from course 6. Introduces reusable tool interfaces before the multi-agent workflow course.

## Transformation

From "my tools are tied to one application" to "I can expose and reuse them through a standard interface."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

MCP hosts and clients, local stdio transport, tool descriptions and input schemas, `tools/list`, `tools/call`, tool results, connection errors and a LangChain MCP adapter.

### How it's used in the exercises

Start with a working handbook server and an organizer's script. After inspecting the exchange, implement the same tool interface over the course 5 index. Give the LangChain assistant the discovered tools and rerun its rehearsal-policy question. Compare the section IDs returned to the script and agent.

### Model / release

Python 3.13. `mcp==1.30.0`, `langchain==1.5.2`, `langchain-openai==1.8.5`, `langchain-mcp-adapters==0.3.2`. Use DataCamp-funded model API calls; no fixed model release is required. MCP processes run locally over stdio and require no external account.

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
