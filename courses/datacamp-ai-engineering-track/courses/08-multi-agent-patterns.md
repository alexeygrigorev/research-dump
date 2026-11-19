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
| 8.1 | Choose a workflow or a team of agents | BC `v2/04-testing/06-multi-agent/02-workflows-and-orchestrated.md` |
| 8.2 | Pass typed state between LangGraph nodes | BC Week 4 Agentic Graphs |
| 8.3 | Route requests to specialist agents | BC `v2/04-testing/06-multi-agent/03-06` |
| 8.4 | Delegate tasks to specialists from a supervisor | BC Week 4 Multi-Agent Systems; [DeepLearning.AI course](https://www.deeplearning.ai/courses/multi-ai-agent-systems-with-crewai) |
| 8.5 | Revise unsupported drafts with a retry limit | BC `v2/04-testing/06-multi-agent/11-14` |
| 8.6 | Run independent specialists in parallel | BC Week 4 coordination; [Anthropic workflow patterns](https://www.anthropic.com/research/building-effective-agents) |

## Detailed lesson outline

### 8.1 Choose a workflow or a team of agents

Use a single-agent support baseline for three requests: one known lookup, one request for a specialist, and one that needs two specialists. Decide which requests justify delegation.

**Check.** Explain the choice for each request using tool scope and coordination cost.

### 8.2 Pass typed state between LangGraph nodes

Represent the request and retrieved evidence in graph state. Connect a retrieval node to an answer node.

**Check.** Run the graph and inspect the state passed between nodes.

### 8.3 Route requests to specialist agents

Route requests to a device-support worker or a software-access worker based on the classified intent.

**Check.** Check both routes and the fallback for an ambiguous request.

### 8.4 Delegate tasks to specialists from a supervisor

Give a supervisor access to two specialist agents with distinct tools. Have it handle an access request that also depends on device eligibility by passing each worker only the relevant context.

**Check.** Verify which specialist received each task and trace the claims in the combined reply to worker results.

### 8.5 Revise unsupported drafts with a retry limit

Evaluate a draft for supporting citations and send it back for revision within a fixed retry limit.

**Check.** Verify that one bad draft is revised and repeated failure ends the loop.

### 8.6 Run independent specialists in parallel

Have two specialists retrieve device and software requirements concurrently. Merge their evidence, then compare the answer and dispatch count with the single-agent baseline.

**Check.** Verify that both source IDs survive the merge and describe when parallel work is worth the extra calls.
