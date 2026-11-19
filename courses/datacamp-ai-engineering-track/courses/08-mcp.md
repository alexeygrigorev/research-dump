# 8. Model Context Protocol (MCP)

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 3. Agents. 5 lessons, 2-3 hours.

## Summary

Learners expose the internal knowledge base's search and fetch functions as MCP tools and connect the LangChain agent to a local server. They inspect discovery results, call the tools through a client, and handle errors such as unknown document IDs.

## Learning objectives

- Explain the roles of an MCP host, client, and server
- Expose Python functions as tools with typed inputs and clear descriptions
- Start a local MCP server over standard input and output
- Discover and invoke server tools from a client and a LangChain agent
- Handle invalid tool arguments and unavailable tools

## Why here

The LangChain course provides an agent and typed tools that learners can reuse. Separating tool delivery into a server gives learners a concrete reason for learning the protocol.

## Transformation

From registering Python tools inside one application to exposing and consuming tools through MCP.

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

Python MCP SDK, tool schemas, standard input and output transport, client sessions, tool discovery and invocation, agent integration, and error results.

### How it's used in the exercises

Publish the search and fetch tools from the agent course in a local MCP server. Connect a client, list the available tools, and fetch a known and an unknown ID. Replace the LangChain agent's in-process knowledge tools with MCP tools and run the original search-and-fetch exercise. Grade discovery, the sequence of tool calls, and the resulting document ID with fixtures.

### Model / release

Python 3.13, the Python MCP SDK, LangChain, and its MCP integration. Tool definitions and calls can be graded with a supplied client fixture. The agent exercise can use a scripted OpenAI response.

### Source material

- **BC** Week 3 Model Context Protocol, especially `v2/03-agents/07-mcp/01-section-overview.md` and `02-stdio-transport.md`.
- **FG** MCP appears in 15.6% of roles and rose from 9.9% to 20.4% during the sampled period.

### Notes

Use a bundled server executable wherever the lesson environment supports subprocesses. Bundle recorded protocol exchanges for environments that restrict subprocesses.

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 8.1 | Hosts, clients, and servers | BC `v2/03-agents/07-mcp/01-section-overview.md` |
| 8.2 | Exposing tools over stdio | BC `v2/03-agents/07-mcp/02-stdio-transport.md` |
| 8.3 | Discovering and calling tools | BC `v2/03-agents/07-mcp/02-stdio-transport.md` |
| 8.4 | Connecting MCP tools to a LangChain agent | Adapted from BC `v2/03-agents/07-mcp/02-stdio-transport.md` |
| 8.5 | Handling tool errors | New exercise extending the local MCP server |
