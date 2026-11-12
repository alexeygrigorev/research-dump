# 8. Multi-Agent Patterns and Guardrails

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 3. Agents. 7 lessons, 2–3 hours.

## Summary

One agent with many tools gets unreliable. Learners split work across agents using a small set of named patterns (routing, pipelines, feedback loops, coordination), add a human-in-the-loop step, and protect the system with input and output guardrails.

## Learning objectives

- Distinguish workflows from agents and choose between them for a task
- Implement routing, pipeline, feedback and coordination patterns
- Add human approval to an agent action
- Add input and output guardrails that stop unsafe or off-topic requests
- Decide when a multi-agent design is justified

## Why here

Needs a framework (course 7). It closes the Agents stage so that the Quality stage can test and evaluate realistic agent systems.

## Transformation

From "I can build one agent" to "I can design a system of agents with the right pattern and with guardrails around it."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

Agents as tools, handoffs, prompt chaining, plan-and-execute, evaluator-optimizer loop, parallel calls with asyncio, orchestrator-workers, guardrail checks as tool calls and as parallel tasks

### How it's used in the exercises

The learner starts from a single overloaded agent and refactors it step by step: a router in front, a two-step pipeline, an evaluator that sends work back, then an input guardrail. After each step they run the same set of requests and compare behaviour.

### Model / release

Python 3.13; pydantic-ai>=1.55.0, openai>=2.38.0. Small model for workers and guardrails, a stronger model only for the orchestrator.

### Source material

- AI Engineering Buildcamp (Maven course; repo ai-engineering-buildcamp, curriculum.md) Week 4: Multi-Agent Systems (Groups 1–4), Agentic Graphs; Week 7: Guardrails with PydanticAI, Guardrails with OpenAI Agents SDK
- LLM Zoomcamp (github.com/DataTalksClub/llm-zoomcamp) 03-orchestration/02-context-engineering.md, 07-multi-agent.md

### Notes

Good place to teach 'most efficient model for the job': cheap models for routing and guardrails. LLM Zoomcamp's orchestration module uses Kestra (a server); only its concepts are used here.

## Lesson outline and source map

LZ = LLM Zoomcamp path, BC = AI Engineering Buildcamp path. 'new' = no lesson in either source.

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 8.1 | Workflows vs agents | BC v2/04-testing/06-multi-agent/02-workflows-and-orchestrated.md; LZ 03-orchestration/02-context-engineering.md |
| 8.2 | Routing: simple routing, agents as tools, handoffs | BC 06-multi-agent/03–06 |
| 8.3 | Pipelines: prompt chaining and plan-and-execute | BC 06-multi-agent/07–10 |
| 8.4 | Feedback: human in the loop and evaluator-optimizer | BC 06-multi-agent/11–14 |
| 8.5 | Coordination: parallelization and orchestrator-workers | BC 06-multi-agent/15–18; LZ 03-orchestration/07-multi-agent.md |
| 8.6 | Input guardrails | BC v2/07-project-bonus/05-guardrails-pydantic/01–03 |
| 8.7 | Output guardrails and when not to go multi-agent | BC v2/07-project-bonus/04-guardrails-sdk/01–02 |
