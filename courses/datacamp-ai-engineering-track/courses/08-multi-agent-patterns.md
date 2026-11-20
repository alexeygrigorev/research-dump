# 8. Multi-Agent Patterns with LangGraph

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 3. Agents. 6 lessons, 2–3 hours.

## Summary

“Can I move my rehearsal? If so, draft a ticket with my current slot and the change procedure.” One answer needs two kinds of evidence. The handbook says who can change a booking. The schedule says which booking belongs to this speaker. Learners build a LangGraph workflow that delegates those questions, brings the findings together and catches a draft that promises an unconfirmed change. They compare its results and cost with the single agent from course 6.

## Learning objectives

- Choose a fixed lookup, a single tool-using agent or a team of agents for a speaker request.
- Represent the request, policy evidence and booking in graph state and route work to the appropriate specialist.
- Delegate parts of a compound request and combine the workers' findings into one grounded reply.
- Bound a draft-review loop and measure when independent workers benefit from parallel execution.

## Why here

Course 6 supplies a single agent, the handbook and schedule tools, and a ticket draft function. Learners can now ask whether giving different workers their own instructions, evidence and tools improves a specific task. Course 7's MCP handbook tools or the equivalent local fixtures provide the same policy evidence.

## Transformation

Learners can trace who answered each part of a request, where evidence was lost, and whether the additional agents earned their cost.

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

LangGraph `StateGraph`, typed state, nodes and edges, conditional routing, agents used as tools, bounded evaluator feedback, parallel branches and a join.

### How it's used in the exercises

The policy agent may search and fetch handbook sections. The schedule agent may look up a speaker's booking. Each returns its finding and source ID. The coordinating step owns the final reply and writes a draft only when requested. Each lesson extends a supplied graph scaffold. The ordinary LangChain assistant remains the course 9 project starter and the baseline for these comparisons.

### Model / release

Python 3.13, LangGraph and the LangChain stack from course 6. Supply tool fixtures, scripted specialist and supervisor responses, and recorded timings for the comparison. Grade wiring, evidence, outcomes and call counts.

### Source material

- **BC** Week 4 Multi-Agent Systems supplies worked examples for routing, agents as tools, fixed evaluators and parallelization. Week 4 Agentic Graphs includes a LangGraph implementation.
- **LZ** Module 3 Orchestration, lessons 2 and 7, covers context and combining specialist results.
- The LangGraph guide illustrates the difference between a workflow with predetermined steps and an agent that selects its own tools. [LangGraph workflows and agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents)

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 8.1 | Choosing an Agent Architecture | BC `v2/04-testing/06-multi-agent/02-workflows-and-orchestrated.md` |
| 8.2 | Graph State with LangGraph | BC `v2/04-testing/08-agentic-graphs/05-langgraph.md` |
| 8.3 | Routing to Specialist Agents | BC `v2/04-testing/06-multi-agent/04-1a-simple-routing.md` |
| 8.4 | Supervisor and Worker Agents | BC `v2/04-testing/06-multi-agent/05-1b-agents-as-tools.md` and `17-4b-orchestrator-workers.md` |
| 8.5 | Evaluator Loops | BC `v2/04-testing/06-multi-agent/13-3b-fixed-evaluator.md` |
| 8.6 | Parallel Agents | BC `v2/04-testing/06-multi-agent/16-4a-parallelization.md`, LZ `03-orchestration/07-multi-agent.md` |

## Detailed lesson outline

### 8.1 Choosing an Agent Architecture

Compare a known-slot lookup with the compound rehearsal request. Run the lookup function and the course 6 agent, then inspect a supplied compound-answer trace in which the agent correctly quotes policy but overlooks which slot the speaker booked.

**Check.** Mark the evidence each request needs and locate the first missing result in the trace. Decide where a fixed lookup suffices and what a specialist would need to return to improve the incomplete answer.

### 8.2 Graph State with LangGraph

Build a small fixed graph for “When is my rehearsal?” Carry the speaker ID into the booking lookup and its result into a reply node. Inspect the state after each step. This gives learners working graph mechanics before they add any agents.

**Check.** Run two speaker IDs. Verify the booking read by the reply node belongs to the current request and includes the source row ID.

### 8.3 Routing to Specialist Agents

Wrap the handbook and schedule tools in separate agents, each with its own instructions and tool access. Add a router for a single policy or booking question. Route “Can you check that for me?” to a clarification when the topic is missing.

**Check.** Inspect three traces. Only the selected specialist should run on each clear request, and both tool logs should be empty on the clarification path.

### 8.4 Supervisor and Worker Agents

Extend the graph to handle the compound request. A supervisor delegates the change procedure to the policy agent and the speaker's current slot to the schedule agent. It combines their results into a proposed ticket with the current booking, requested change and contact named in the policy.

**Check.** Inspect the task sent to each worker and the proposed ticket. Match the change procedure to the returned handbook section and the booking to its schedule row. If the speaker ID is missing, the assistant should ask for it before drafting a ticket.

### 8.5 Evaluator Loops

Give a reviewer the proposed ticket and the two pieces of evidence. An exercise draft claims that the new time is confirmed. Use the reviewer's feedback to revise it into a request for a change. Only an accepted draft reaches the local draft store.

**Check.** Run an accepted draft, a corrected draft and a draft that keeps failing review. Check the number of revisions, the terminal status and the store. Repeated failure must stop at the limit without saving a draft.

### 8.6 Parallel Agents

For a compound request with a known speaker ID, dispatch the two independent lookups together. Give each branch its own state field and join both results before drafting. Run the fixed, single-agent and specialist designs on the same small set of requests using the same tools and success criteria.

**Check.** Verify that both evidence IDs reach the draft when workers finish in either order. Compare supported answers, model calls and elapsed time from supplied traces. Choose a design for simple lookups and one for compound requests, citing the measured trade-off for each.
