# 5. Agent Basics: Tool Calling and the Agent Loop - DONE

Part of the [DataCamp AI Engineering track plan](../README.md). Stage: 3. Agents. 6 lessons, 2-3 hours. Each lesson is designed for approximately 20-25 minutes.

## Summary

Learners give an LLM tools and build the loop that executes its choices. They connect tool calls to Python functions, return results to the model, and preserve the history needed for follow-up questions. They also handle tool failures and set limits on runs that do not finish.

## Learning objectives

- Describe callable tools with input schemas
- Execute model-selected tool calls and return matching results
- Maintain tool and conversation loops across turns
- Handle tool errors and stop runs at a defined limit

## Why here

Moves from a fixed retrieval pipeline to model-selected actions before introducing framework abstractions.

## Transformation

From "I can run a fixed pipeline" to "I can implement and inspect an agent loop."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

OpenAI Responses API function schemas, JSON arguments, dispatch by tool name, `function_call_output`, call IDs, message history and a tool-round limit.

### How it's used in the exercises

Provide the index and two functions. Search returns section headings and IDs. Fetch returns the passage and its source ID. Learners implement the dispatcher and loop, then inspect the recorded inputs to each model call. The scripted model requests the next step only after receiving the expected tool result.

### Model / release

Python 3.13. `openai==3.57.0`, `pydantic==2.14.4`. Use DataCamp-funded model API calls. Select the lowest-cost available model that meets the exercise criteria; no fixed model release is required.

### Source material

- **BC** Week 3 Agent Basics, especially the agentic loop, Q&A loop and Wikipedia homework.
- **LZ** Module 1 Agentic RAG, lessons 11–14.
- **FG** The AI Agents learning path starts with function calling and the tool-call loop. Agents and RAG appear together in 51.0% of the sampled AI-First postings in November.

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 5.1 | Introduction to Agents | LZ `01-agentic-rag/11-agents-intro.md` and `12-rag-revision.md` |
| 5.2 | Tool Calling in Python | BC `v2/03-agents/02-agent-basics/02-agentic-rag-tool-calling.md` |
| 5.3 | The Tool Call Loop | BC `v2/03-agents/02-agent-basics/03-agentic-loop.md`, LZ `01-agentic-rag/14-agentic-loop.md` |
| 5.4 | The Conversation Loop | BC `v2/03-agents/02-agent-basics/04-qna-loop.md` |
| 5.5 | Handling Tool Errors | New exercise extending the BC agent loop |
| 5.6 | Limiting Agent Runs | New exercise extending the BC agent loop |

## Detailed lesson outline

### 5.1 Introduction to Agents

Run the fixed RAG pipeline from course 2 on a rehearsal policy question. Compare its trace with an agent's traces for the same question and for “Show me the section you just cited.”

**Check.** Mark the first step where the two approaches choose differently. Explain when a section ID lets the agent skip search.

### 5.2 Tool Calling in Python

Describe the inputs to search and fetch. Inspect a model request to fetch a section, parse its JSON arguments, call the matching Python function and return its result.

**Check.** Inspect the dispatch log and outgoing message. The arguments must reach the right function and the result must carry the model's call ID.

### 5.3 The Tool Call Loop

Execute each requested tool call, add its output to the conversation, and call the model again. Stop when it provides the answer. Try both a known section and a rehearsal question that requires search followed by fetch.

**Check.** Verify each tool sequence, the ID passed from search to fetch and the source cited in the final answer. A completed answer must end the run.

### 5.4 The Conversation Loop

After answering a question about moving a rehearsal, handle “Who do I contact about that?” Carry the previous question, retrieved passage and response into the follow-up.

**Check.** Inspect the second turn for the earlier evidence and match the contact in the answer to the cited passage. Start a fresh conversation and verify that it has its own history.

### 5.5 Handling Tool Errors

Handle a fetch for an unknown section. Return the error to the model with the matching call ID so it can explain the missing evidence.

**Check.** Verify that the error is attached to the failed call and does not become a successful lookup result.

### 5.6 Limiting Agent Runs

Run a fixture in which the model repeatedly requests the same lookup. Add a round limit and return an incomplete status when the budget runs out.

**Check.** Count tool executions and confirm the run stops at the configured limit.
