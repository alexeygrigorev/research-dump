# 9. Multi-Agent Patterns with LangGraph

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
| 9.1 | Workflows and agents | BC `v2/04-testing/06-multi-agent/02-workflows-and-orchestrated.md` |
| 9.2 | State, nodes, and edges in LangGraph | BC Week 4 Agentic Graphs |
| 9.3 | Routing and handoffs | BC `v2/04-testing/06-multi-agent/03-06` |
| 9.4 | Pipelines and prompt chaining | BC `v2/04-testing/06-multi-agent/07-10` |
| 9.5 | Evaluator-optimizer loops | BC `v2/04-testing/06-multi-agent/11-14` |
| 9.6 | Parallel workers and coordination | BC `v2/04-testing/06-multi-agent/15-18`; LZ `03-orchestration/07-multi-agent.md` |
