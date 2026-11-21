# 10. Testing AI Applications - DONE

Part of the [DataCamp AI Engineering track plan](../README.md). Stage: 4. Application quality. 6 lessons, 2-3 hours. Each lesson is designed for approximately 20-25 minutes.

## Summary

Learners write tests for the behavior of an AI application. They check tool calls and output contracts, use a judge for claims that require semantic assessment, and reproduce failures across conversation turns. They finish with a regression suite and an understanding of its model-call costs.

## Learning objectives

- Write regression tests around agent and API behavior
- Check tool arguments and output contracts
- Use an LLM judge to assess answer quality
- Test multi-turn behavior and account for live-test costs

## Why here

Starts from importable application code so failures can be reproduced and caught on subsequent changes.

## Transformation

From "I check answers manually" to "I can run tests that catch a known regression."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

Pytest fixtures, parameterized cases, scripted model turns, tool-call records, FastAPI test client, Pydantic, judge rubrics, token accounting.

### How it's used in the exercises

Supply the module from course 9, two similar handbook sections (“Draft Slides” and “Final Slides”), recorded model turns, and a local tool-call recorder. Learners call the production answer function. Their tests inspect the arguments that actually reached the tools and the response that reached the HTTP client. For the judge exercise they also receive paired human labels and recorded judge responses.

### Model / release

Python 3.13. `pytest==9.2.0`, `httpx==0.28.1`, `openai==3.57.0`, `pydantic==2.14.4`, `fastapi==0.165.0`. Use DataCamp-funded model API calls. Select the lowest-cost available model that meets the exercise criteria; no fixed model release is required.

### Source material

- The AI Engineering Field Guide reports evaluation and testing in 79.0% of November job responsibilities. Its portfolio guide asks for a deterministic test suite with one entry point.
- Buildcamp Week 4 covers testing tools, output properties, LLM judges, and costs. [Buildcamp testing lessons](https://github.com/alexeygrigorev/ai-bootcamp/tree/60cc917c776e74d3aaeffb2d24f8f93c320e4b8b/v2/04-testing)

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 10.1 | Testing Agents | BC Week 4 `03-testing/02-first-test.md` |
| 10.2 | Testing Tool Calls | BC `03-testing/03-testing-tool-calls.md` |
| 10.3 | Testing Output Quality | BC `03-testing/04-refactoring-tests.md` and `05-testing-output-quality.md` |
| 10.4 | LLM Judges | BC `04-llm-judges/02-creating-judge.md` |
| 10.5 | Multi-Turn Tests | BC `04-llm-judges/03-thinking-about-test-cases.md` and `05-improving-judge-tests.md` |
| 10.6 | Tracking Test Costs | BC `03-testing/06-tracking-costs.md` |

## Detailed lesson outline

### 10.1 Testing Agents

Compare two responses to the final-slides question. Both state the right date, but one loses the source ID when the application constructs the response. Invoke the answer function with a local handbook and a scripted model. Write an assertion for the expected section ID.

**Check.** Run the same test against the working and broken response builders. Show the actual and expected source IDs in the failure output.

### 10.2 Testing Tool Calls

Record calls at the tool boundary. For an open question, verify that fetch receives an ID returned by search. For “Show me section X,” exercise the valid direct-fetch path. Use a second handbook fixture with different IDs.

**Check.** Make the dispatcher substitute the draft-slides ID for the selected final-slides ID. The tool assertion must fail even when the recorded model still produces a plausible deadline.

### 10.3 Testing Output Quality

Move repeated setup into fixtures. Send the question through the API's test client. Validate the response schema and check that citations identify sections actually fetched during that request. Parameterize two supported phrasings and an out-of-scope question on travel reimbursement.

**Check.** Both supported answers pass with different wording. A well-formed response citing an unfetched section fails. The reimbursement case returns an explicit insufficient-evidence answer without a fabricated source.

### 10.4 LLM Judges

Give a judge the speaker's question, fetched text and answer. Ask for a verdict and the specific claim that lacks support. Compare a paraphrase of the real deadline with an otherwise identical answer claiming speakers have a one-week extension. Both carry the correct citation ID.

**Check.** Label both answers by hand, then inspect a recorded judge response for each. Write the pytest assertion that fails on an unsupported claim and displays the reason. Capture the constructed judge request to verify that both the answer and supporting passage reached it.

### 10.5 Multi-Turn Tests

A speaker first asks about draft slides, then asks about final slides. The application carries the previous response's source IDs into the follow-up. Encode both turns in a regression test, find the code that accumulates citations, and scope the response's citations to the current answer.

**Check.** Demonstrate that the test fails on the original implementation and passes after the fix. The final answer cites only “Final Slides,” while the conversation history still contains the first turn.

### 10.6 Tracking Test Costs

Compare an offline regression run with a recorded live run of the same cases. Attribute input and output tokens to assistant and judge calls, including one retry. Apply the supplied per-model rates.

**Check.** Report assistant cost, judge cost, and total for the live run. Identify the case responsible for the retry from its call records. Verify the offline suite made zero provider calls.
