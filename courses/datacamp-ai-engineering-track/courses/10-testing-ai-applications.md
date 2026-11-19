# 10. Testing AI Applications

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 4. Application quality. 6 lessons, 2–3 hours.

## Summary

The speaker assistant returns a plausible deadline even when a change makes it fetch the wrong handbook section. Learners write tests that catch the mistake at three places in the Python project: the tool call, the citation returned by the API, and the factual claim in the answer. They finish with a regression suite they can run with one command.

## Learning objectives

- Write a pytest fixture that exercises the real agent loop with scripted model turns
- Assert a relationship between tool arguments, returned evidence, and citations
- Use a structured LLM judge to check a claim that a schema accepts
- Reproduce a reported failure and account for the cost of a live test run

## Why here

Course 9 provides an importable assistant and an HTTP endpoint. A regression test gives the maintainer a repeatable example of a broken requirement. Course 12 measures how often requirements hold across a collection of speaker requests.

## Transformation

Learners can change the assistant, run `uv run pytest`, and use the failed assertion to locate the behavior they changed.

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

Pytest fixtures, parameterized cases, scripted model turns, tool-call records, FastAPI test client, Pydantic, judge rubrics, token accounting.

### How it's used in the exercises

Supply the module from course 9, two similar handbook sections (“Draft Slides” and “Final Slides”), recorded model turns, and a local tool-call recorder. Learners call the production answer function. Their tests inspect the arguments that actually reached the tools and the response that reached the HTTP client. For the judge exercise they also receive paired human labels and recorded judge responses.

### Model / release

Python 3.13, pytest, FastAPI's test client, Pydantic, uv, and the assistant's existing model integration. Run one live judging demonstration with a supplied budget. Graded examples replay recorded model turns.

### Source material

- The AI Engineering Field Guide reports evaluation and testing in 79.0% of November job responsibilities. Its portfolio guide asks for a deterministic test suite with one entry point.
- Buildcamp Week 4 covers testing tools, output properties, LLM judges, and costs. [Buildcamp testing lessons](https://github.com/alexeygrigorev/ai-bootcamp/tree/60cc917c776e74d3aaeffb2d24f8f93c320e4b8b/v2/04-testing)

## Exercise adapted from the Buildcamp

The original SQL exercise checks which tools ran and what they produced. Here search returns a section ID, fetch accepts that ID, and the speaker receives a cited deadline. Learners deliberately introduce a bad fetch argument, a missing citation, and an invented deadline. Each failure should point to a different assertion. [Buildcamp Week 4 homework](https://github.com/alexeygrigorev/ai-bootcamp/blob/60cc917c776e74d3aaeffb2d24f8f93c320e4b8b/v2/04-testing/homework/01-homework.md)

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 10.1 | Writing a Test for a Missing Citation | BC Week 4 `03-testing/02-first-test.md` |
| 10.2 | Testing Tool Calls and Arguments | BC `03-testing/03-testing-tool-calls.md` |
| 10.3 | Testing the Answer and Its Citations | BC `03-testing/04-refactoring-tests.md` and `05-testing-output-quality.md` |
| 10.4 | Checking Answer Grounding with an LLM Judge | BC `04-llm-judges/02-creating-judge.md` |
| 10.5 | Testing Follow-Up Questions | BC `04-llm-judges/03-thinking-about-test-cases.md` and `05-improving-judge-tests.md` |
| 10.6 | Tracking the Cost of Model Tests | BC `03-testing/06-tracking-costs.md` |

## Detailed lesson outline

### 10.1 Writing a Test for a Missing Citation

Compare two responses to the final-slides question. Both state the right date, but one loses the source ID when the application constructs the response. Invoke the answer function with a local handbook and a scripted model. Write an assertion for the expected section ID.

**Check.** Run the same test against the working and broken response builders. Show the actual and expected source IDs in the failure output.

### 10.2 Testing Tool Calls and Arguments

Record calls at the tool boundary. For an open question, verify that fetch receives an ID returned by search. For “Show me section X,” exercise the valid direct-fetch path. Use a second handbook fixture with different IDs.

**Check.** Make the dispatcher substitute the draft-slides ID for the selected final-slides ID. The tool assertion must fail even when the recorded model still produces a plausible deadline.

### 10.3 Testing the Answer and Its Citations

Move repeated setup into fixtures. Send the question through the API's test client. Validate the response schema and check that citations identify sections actually fetched during that request. Parameterize two supported phrasings and an out-of-scope question on travel reimbursement.

**Check.** Both supported answers pass with different wording. A well-formed response citing an unfetched section fails. The reimbursement case returns an explicit insufficient-evidence answer without a fabricated source.

### 10.4 Checking Answer Grounding with an LLM Judge

Give a judge the speaker's question, fetched text and answer. Ask for a verdict and the specific claim that lacks support. Compare a paraphrase of the real deadline with an otherwise identical answer claiming speakers have a one-week extension. Both carry the correct citation ID.

**Check.** Label both answers by hand, then inspect a recorded judge response for each. Write the pytest assertion that fails on an unsupported claim and displays the reason. Capture the constructed judge request to verify that both the answer and supporting passage reached it.

### 10.5 Testing Follow-Up Questions

A speaker first asks about draft slides, then asks about final slides. The application carries the previous response's source IDs into the follow-up. Encode both turns in a regression test, find the code that accumulates citations, and scope the response's citations to the current answer.

**Check.** Demonstrate that the test fails on the original implementation and passes after the fix. The final answer cites only “Final Slides,” while the conversation history still contains the first turn.

### 10.6 Tracking the Cost of Model Tests

Compare an offline regression run with a recorded live run of the same cases. Attribute input and output tokens to assistant and judge calls, including one retry. Apply the supplied per-model rates.

**Check.** Report assistant cost, judge cost, and total for the live run. Identify the case responsible for the retry from its call records. Verify the offline suite made zero provider calls.
