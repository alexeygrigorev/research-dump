# 8. Multi-Agent Patterns with LangGraph


Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 3. Agents. 6 lessons, 2-3 hours.

## Summary

Learners use LangGraph to coordinate specialist agents in an internal support workflow. They build a graph with shared state, add routing and feedback, and compare the resulting workflow with a fixed pipeline and a single agent.

## Learning objectives

- Choose between a fixed workflow, a single agent, and a multi-agent workflow
- Define graph state, nodes, and conditional edges in LangGraph
- Route requests to specialist agents and pass context between steps
- Implement a bounded evaluator-optimizer loop and parallel workers
- Compare workflow designs using task outcomes, model calls, and latency

## Why here

Learners already know how to implement a single agent with typed tools. This advanced course introduces graph orchestration when the task calls for explicit control of state and sequencing.

## Transformation

From building a single agent to coordinating agents in a stateful workflow.

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

LangGraph `StateGraph`, shared state, nodes, conditional edges, handoffs, prompt chaining, bounded feedback loops, and parallel workers.

### How it's used in the exercises

Start with the support assistant from the LangChain course. Route policy questions to a knowledge worker and requests for a draft ticket to a workflow worker. Add a bounded review loop for draft tickets. Use parallel workers on a request that needs evidence from two sources and combine their results. Run the same fixture requests through a fixed pipeline, a single agent, and the graph to compare outcomes and call counts.

### Model / release

Python 3.13, LangGraph, and the LangChain OpenAI integration. Use scripted results for graded routing and state transitions.

### Source material

- **BC** Week 4 Multi-Agent Systems and Agentic Graphs, `v2/04-testing/06-multi-agent/`.
- **LZ** `03-orchestration/02-context-engineering.md` and `03-orchestration/07-multi-agent.md`.
- **FG** Agentic workflows appear in 32.8% of roles and LangGraph appears in 71.0% of framework adopters.

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 8.1 | Workflows and agents | BC `v2/04-testing/06-multi-agent/02-workflows-and-orchestrated.md` |
| 8.2 | State, nodes, and edges in LangGraph | BC Week 4 Agentic Graphs |
| 8.3 | Routing and handoffs | BC `v2/04-testing/06-multi-agent/03-06` |
| 8.4 | Pipelines and prompt chaining | BC `v2/04-testing/06-multi-agent/07-10` |
| 8.5 | Evaluator-optimizer loops | BC `v2/04-testing/06-multi-agent/11-14` |
| 8.6 | Parallel workers and coordination | BC `v2/04-testing/06-multi-agent/15-18`; LZ `03-orchestration/07-multi-agent.md` |

## Detailed lesson outline

TODO let's think better about it and research what other courses teach and what other materials cover

### 8.1 Workflows and agents

Classify support requests that can follow a fixed sequence and requests that need the model to choose tools.

**Check.** Draw the steps for one request of each type.

### 8.2 State, nodes, and edges in LangGraph

Represent the request and retrieved evidence in graph state. Connect a retrieval node to an answer node.

**Check.** Run the graph and inspect the state passed between nodes.

### 8.3 Routing and handoffs

Route requests to a device-support worker or a software-access worker based on the classified intent.

**Check.** Check both routes and the fallback for an ambiguous request.

### 8.4 Pipelines and prompt chaining

Chain a lookup step and a drafting step so the second consumes a typed result from the first.

**Check.** Verify that the draft references the handoff data.

### 8.5 Evaluator-optimizer loops

Evaluate a draft for supporting citations and send it back for revision within a fixed retry limit.

**Check.** Verify that one bad draft is revised and repeated failure ends the loop.

### 8.6 Parallel workers and coordination

Run two independent lookups in parallel and merge their results in a coordinator node.

**Check.** Check that both findings appear in the merged evidence with their source IDs.
