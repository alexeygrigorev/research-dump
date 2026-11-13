# 8. Multi-Agent Patterns and Guardrails

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 3. Agents. 7 lessons, 2–3 hours.

## Summary

One agent with many tools gets unreliable. Learners build stateful multi-agent workflows in **LangGraph** (Agentic Workflows appear in 32.8% of all jobs; LangGraph in 71.0% of framework adopters) using named patterns (routing, pipelines, evaluator-optimizer, orchestrator-workers), add human-in-the-loop approval, and protect the system with input and output **guardrails** (19.8% of AI-First roles, rising 10.2% → 17.5% overall).

## Learning objectives

- Distinguish deterministic workflows from autonomous agents and choose between them for a task
- Implement routing, pipeline, feedback and coordination patterns in LangGraph
- Add human-in-the-loop approval to an agent action
- Add input and output guardrails that stop unsafe, off-topic or policy-violating requests
- Decide when a multi-agent design is justified

## Why here

Needs LangGraph/framework skills (course 7). Closes the Agents stage by combining enterprise workflow automation (58.8% of jobs) with safety, security, and guardrails (37.5% security/compliance responsibilities in Nov).

## Transformation

From "I can build one agent" to "I can design a stateful multi-agent workflow with guardrails around it."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

LangGraph `StateGraph`, nodes, conditional edges, agents as tools, handoffs, prompt chaining, plan-and-execute, evaluator-optimizer loop, parallel calls with `asyncio`, human-in-the-loop interrupts, input/output guardrail checks

### How it's used in the exercises

The learner starts from a single overloaded agent and refactors it step by step in LangGraph: a router in front, a two-step pipeline, an evaluator-optimizer loop with human approval, and parallel input/output guardrails. After each step they run the same set of requests and compare behaviour and cost.

### Model / release

Python 3.13; `langgraph`, `langchain-core` (versions TBC), `pydantic-ai>=1.55.0`, `openai>=2.38.0`. Small model for workers, routing and guardrails; a stronger model only for the orchestrator.

### Source material

- **FG** (AI Engineering Field Guide, 9,760 jobs): Agentic Workflows 32.8% (3,199 jobs), LangGraph 71.0% of framework adopters, Guardrails 19.8% AI-First (10.2% → 17.5% overall, +0.77 pp/scrape), Security/Safety/Compliance 37.5%, Automating Manual Workflows 58.8%
- **BC**: AI Engineering Buildcamp (`ai-engineering-buildcamp/curriculum.md`) Week 4: Multi-Agent Systems (Groups 1–4), Agentic Graphs; Week 7: Guardrails with PydanticAI, Guardrails with OpenAI Agents SDK
- **LZ**: LLM Zoomcamp (`github.com/DataTalksClub/llm-zoomcamp`) `03-orchestration/02-context-engineering.md`, `07-multi-agent.md`

### Notes

Good place to teach 'most efficient model for the job': cheap models for routing and guardrails. LLM Zoomcamp's orchestration module uses Kestra (a server); only its concepts are used here, implemented directly in LangGraph.

## Lesson outline and source map

FG = AI Engineering Field Guide, LZ = LLM Zoomcamp path, BC = AI Engineering Buildcamp path. `'new'` = no lesson in LZ or BC.

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 8.1 | Workflows vs agents | BC `v2/04-testing/06-multi-agent/02-workflows-and-orchestrated.md`; LZ `03-orchestration/02-context-engineering.md` |
| 8.2 | Routing: conditional edges, agents as tools, handoffs | BC `06-multi-agent/03–06`; LangGraph `StateGraph` |
| 8.3 | Pipelines: prompt chaining and plan-and-execute | BC `06-multi-agent/07–10` |
| 8.4 | Feedback: human in the loop and evaluator-optimizer | BC `06-multi-agent/11–14` |
| 8.5 | Coordination: parallelization and orchestrator-workers | BC `06-multi-agent/15–18`; LZ `03-orchestration/07-multi-agent.md` |
| 8.6 | Input guardrails | BC `v2/07-project-bonus/05-guardrails-pydantic/01–03`; FG Guardrails (17.5%) |
| 8.7 | Output guardrails and when not to go multi-agent | BC `v2/07-project-bonus/04-guardrails-sdk/01–02` |
