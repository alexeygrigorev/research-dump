# 10. Testing AI Applications

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 4. Application quality. 6 lessons, 2-3 hours.

## Summary

A notebook that works once is not an application. Evaluation & Testing appears in **79.0%** of November job responsibilities (+9.6 pp since Feb), and LLM Evaluation is in 33.5% of AI-First roles. Learners start with the assistant’s Python project and write `pytest` suites for tool calls, output properties, and LLM-judge behaviour.

## Learning objectives

- Write `pytest` tests that check which tools an agent called and with what arguments
- Write tests for output properties such as citations, schemas and code blocks
- Create an LLM judge and use it inside `pytest`
- Track the token cost of a test run

## Why here

The preceding course supplies a runnable Python project. Its tests cover behavior that later changes to the assistant could break.

## Transformation

From "it worked when I tried it" to "I have a test suite that tells me when my agent breaks."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

`pytest` tests and fixtures, inspecting agent/LangGraph message history for tool calls, assertion helpers, LLM judge with structured output (pass/fail + reasoning), usage and cost accounting

### How it's used in the exercises

The learner writes a first test, adds tool-call tests, then writes a judge prompt, runs the `pytest` suite, sees a failure, fixes the agent instructions and reruns. At the end they print the cost of the run.

### Model / release

Python 3.13; `pytest`, `uv` (versions TBC), `langgraph`, `pydantic-ai>=1.55.0`, `openai>=2.38.0`. Small model for the agent; the judge may use a different model (discussed in the lesson).

### Source material

- **FG** (AI Engineering Field Guide, 9,760 jobs): Evaluation & Testing in 79.0% of Nov responsibilities (+9.6 pp), LLM Evaluation 33.5% AI-First (20.3% → 26.6% overall)
- **FG learning paths / portfolio** (`learning-paths/README.md`, `portfolio/`, commit `1556dcb2`): "Testing" block (tests for tool calls and output quality, LLM-as-judge) and "Converting notebooks to production projects" (Production block). `portfolio/04-polishing.md`: deterministic behaviour tested with one `pytest` command.
- **BC**: AI Engineering Buildcamp (`ai-engineering-buildcamp/curriculum.md`) Week 4: Preparing the Project, Testing for Agents, Test Judges

### Notes

Use scripted model outputs for graded tests. Demonstrate a live judge run separately and track its token use.

## Exercise adapted from the Buildcamp

Use the search-and-fetch agent from the tool-calling course in place of the homework’s DuckDB SQL agent. Have learners write pytest assertions for tool names and arguments using a scripted response, then apply a judge rubric to a grounded answer and an unsupported answer. Grade the tool assertions and expected rubric outcomes with fixed responses.

[Buildcamp Week 4 source](https://github.com/alexeygrigorev/ai-bootcamp/blob/60cc917c776e74d3aaeffb2d24f8f93c320e4b8b/v2/04-testing/homework/01-homework.md)

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 10.1 | Writing the first test | BC `v2/04-testing/03-testing/02-first-test.md` |
| 10.2 | Testing tool calls | BC `03-testing/03-testing-tool-calls.md` |
| 10.3 | Refactoring tests and testing output quality | BC `03-testing/04-refactoring-tests.md`, `05-testing-output-quality.md` |
| 10.4 | Creating an LLM judge | BC `v2/04-testing/04-llm-judges/02-creating-judge.md`; FG LLM Evaluation (33.5% AI-First) |
| 10.5 | Coming up with test cases and fixing the agent | BC `04-llm-judges/03-05` |
| 10.6 | Tracking costs | BC `03-testing/06-tracking-costs.md` |

## Detailed lesson outline

### 10.1 Writing the first test

Write a pytest test for a known support question using a scripted model response.

**Check.** Show a failure with a deliberately incorrect expected answer, then restore the correct assertion.

### 10.2 Testing tool calls

Capture the agent’s tool calls and assert the names, arguments, and order.

**Check.** Use a wrong-ID response to confirm the test detects the regression.

### 10.3 Refactoring tests and testing output quality

Refactor repeated setup into fixtures and add assertions for output schema and citations.

**Check.** Verify that a bad citation fails independently of the tool call assertions.

### 10.4 Creating an LLM judge

Define a judge that returns a verdict and reason using a grounding rubric.

**Check.** Apply it to scripted examples of grounded and unsupported answers.

### 10.5 Coming up with test cases and fixing the agent

Turn a reported assistant failure into a reproducible case, adjust the instructions, and run the suite again.

**Check.** Verify that the new case passes alongside the original cases.

### 10.6 Tracking costs

Read token counts from a recorded judge run and compute total cost with the supplied price table.

**Check.** Compare the test-run total against expected costs.
