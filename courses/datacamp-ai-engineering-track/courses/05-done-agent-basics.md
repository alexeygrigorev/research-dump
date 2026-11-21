# 5. Agent Basics: Tool Calling and the Agent Loop - DONE

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 3. Agents. 6 lessons, 2–3 hours.

## Summary

A speaker asks “How do I move my rehearsal?” The handbook index can find candidate sections, but the assistant needs the full passage to cite the procedure. When the speaker supplies a section ID, it can fetch the passage directly. Learners give a model both tools and write the Python loop that executes its choices.

## Learning objectives

- Describe search and fetch functions with tool schemas and dispatch a model's request to Python.
- Return results to the matching tool calls and continue until the model answers.
- Preserve the evidence and conversation history needed for a follow-up.
- Report a missing section and stop a run that repeatedly requests tools.

## Why here

Courses 2–4 supply an index and stable source IDs. This course changes who chooses the next retrieval step. The loop becomes the reference implementation when learners adopt LangChain in course 6.

## Transformation

Learners can trace how a speaker's question becomes a tool request, a Python result and a cited answer.

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

OpenAI Responses API function schemas, JSON arguments, dispatch by tool name, `function_call_output`, call IDs, message history and a tool-round limit.

### How it's used in the exercises

Provide the index and two functions. Search returns section headings and IDs. Fetch returns the passage and its source ID. Learners implement the dispatcher and loop, then inspect the recorded inputs to each model call. The scripted model requests the next step only after receiving the expected tool result.

### Model / release

Python 3.13, OpenAI Python SDK and MinSearch from course 2. Demonstrate tool selection with a small tool-calling model. Graded runs use scripted Responses API turns.

### Source material

- **BC** Week 3 Agent Basics, especially the agentic loop, Q&A loop and Wikipedia homework.
- **LZ** Module 1 Agentic RAG, lessons 11–14.
- **FG** The AI Agents learning path starts with function calling and the tool-call loop. Agents and RAG appear together in 51.0% of the sampled AI-First postings in November.

## Exercise adapted from the Buildcamp

The Buildcamp homework searches Wikipedia for a page and fetches the selected page. Here a speaker gives either a handbook section ID or a question in their own words. Learners must pass the ID returned by search into fetch, pair each result with the original call ID, and stop after the cited answer. The fixture supplies different IDs on a second run to catch hard-coded arguments. [Buildcamp Week 3 homework](https://github.com/alexeygrigorev/ai-bootcamp/blob/60cc917c776e74d3aaeffb2d24f8f93c320e4b8b/v2/03-agents/homework/01-homework.md)

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
