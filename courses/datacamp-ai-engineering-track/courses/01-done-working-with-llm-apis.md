# 1. Working with LLM APIs - DONE

Part of the [DataCamp AI Engineering track plan](../README.md). Stage: 1. Foundations. 6 lessons, 2-3 hours. Each lesson is designed for approximately 20-25 minutes.

## Summary

Learners move from asking an LLM questions to calling it from Python. They control instructions and conversation history, compare model costs, and turn model responses into validated data. By the end, they can build a small program that handles structured and streamed responses.

## Learning objectives

- Call an LLM API with instructions and conversation history
- Compare model quality and token costs for a defined task
- Extract and validate structured data with a typed schema
- Assemble a streamed response and handle an incomplete result

## Why here

Introduces the request and response mechanics used by retrieval, tool calling, and model-based evaluation.

## Transformation

From "I can use an LLM in a chat window" to "I can call a model from Python and validate its response."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

OpenAI Responses API calls, instructions and conversation messages, token usage fields, Pydantic models, structured output, and streaming.

### How it's used in the exercises

The learner sends a request about a supplied conference speaker handbook excerpt and carries it forward into a follow-up turn. They estimate cost using token counts and a supplied price table. They then define a Pydantic model for extracting a deliverable, due date, and submission destination, validate the extracted fields, and stream the response. Grade request construction and schema validation with fixed responses.

### Model / release

Python 3.13. `openai==3.57.0`, `pydantic==2.14.4`, `python-dotenv==1.2.4`. Use DataCamp-funded model API calls. Select the lowest-cost available model that meets the exercise criteria; no fixed model release is required.

### Source material

- **FG** Python appears in 71.6% of all AI engineer roles and integrating APIs and services appears in 55.8% of responsibilities.
- **BC** Week 1 OpenAI API, Documentation Agent, and Structured Output. Token cost practice draws on Week 4.
- **LZ** `01-agentic-rag/07-llm.md`.

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 1.1 | First OpenAI API Call | BC `v2/01-foundation/03-rag/03-openai-api.md`; LZ `01-agentic-rag/07-llm.md` |
| 1.2 | Instructions and Conversation History | BC `v2/01-foundation/03-rag/03-openai-api.md` |
| 1.3 | Tokens and Model Costs | BC `v2/04-testing/03-testing/06-tracking-costs.md` |
| 1.4 | Structured Output with Pydantic | BC `v2/01-foundation/04-structured-output/01-structured-output.md` |
| 1.5 | Extracting Structured Data | BC `v2/01-foundation/04-structured-output/02-documentation-rag-structured-output.md` |
| 1.6 | Streaming Responses | BC `v2/01-foundation/04-structured-output/03-streaming-structured-output.md` |

## Detailed lesson outline

### 1.1 First OpenAI API Call

Start with the speaker handbook excerpt below. Build a Responses API request that asks when final slides are due, then read the answer from the response.

> Final slides are due October 15, 2027. Upload them in the speaker portal under “Final Slides.”

**Check.** Inspect the request payload and extract the answer from a recorded API response.

### 1.2 Instructions and Conversation History

Ask when final slides are due, then follow up with “Where do I upload them?” Add instructions to answer from the supplied handbook and carry the original question and answer into the next request.

**Check.** Check that the payload includes the relevant history and that the follow-up is interpreted as a question about where to upload final slides.

### 1.3 Tokens and Model Costs

Read the input and output token counts for both turns. Use the supplied per-million-token rates to price the exchange. Compare recorded answers and usage for three models on those same questions.

**Check.** Calculate each model’s total cost and select the least expensive one that gives both the correct deadline and the upload destination.

### 1.4 Structured Output with Pydantic

Start with a rehearsal announcement from the handbook that gives the event name and date. Define an event schema, request a parsed response, and read the returned fields as Python values.

**Check.** Check the parsed name and date, and inspect the validation error from a fixture with an invalid date.

### 1.5 Extracting Structured Data

Use excerpts about final slides and speaker bios to build records containing a deliverable, due date, and submission destination. Normalize explicit dates and permit null for fields the excerpt omits.

**Check.** Run fixtures with complete and incomplete information. Check that an absent due date stays null and that an explicit date parses correctly.

### 1.6 Streaming Responses

Stream a short speaker handbook answer and display text as events arrive. Collect the deltas from a recorded event stream to reconstruct the finished answer.

**Check.** Check that the visible output matches the complete response, and handle a recorded failure without printing a completion message.
