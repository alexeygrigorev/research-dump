# 9. Testing AI Applications

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 4. Quality. 7 lessons, 2–3 hours.

## Summary

A notebook that works once is not an application. Evaluation & Testing appears in **79.0%** of November job responsibilities (+9.6 pp since Feb), and LLM Evaluation is in 33.5% of AI-First roles. Learners turn the agent into a Python project with `uv` and write `pytest` suites for tool calls, output properties, and LLM-judge behaviour.

## Learning objectives

- Refactor notebook code into a testable Python project with `uv`
- Write `pytest` tests that check which tools an agent called and with what arguments
- Write tests for output properties such as citations, schemas and code blocks
- Create an LLM judge and use it inside `pytest`
- Track the token cost of a test run

## Why here

First Quality course: testing uses habits software engineers already have, and gives the project structure that offline evaluation, monitoring and CI/CD need.

## Transformation

From "it worked when I tried it" to "I have a test suite that tells me when my agent breaks."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

Project layout with `uv`, `pytest` tests and fixtures, inspecting agent/LangGraph message history for tool calls, assertion helpers, LLM judge with structured output (pass/fail + reasoning), usage and cost accounting

### How it's used in the exercises

The learner moves the agent into Python modules, writes a first test, adds tool-call tests, then writes a judge prompt, runs the `pytest` suite, sees a failure, fixes the agent instructions and reruns. At the end they print the cost of the run.

### Model / release

Python 3.13; `pytest`, `uv` (versions TBC), `langgraph`, `pydantic-ai>=1.55.0`, `openai>=2.38.0`. Small model for the agent; the judge may use a different model (discussed in the lesson).

### Source material

- **FG** (AI Engineering Field Guide, 9,760 jobs): Evaluation & Testing in 79.0% of Nov responsibilities (+9.6 pp), LLM Evaluation 33.5% AI-First (20.3% → 26.6% overall)
- **BC**: AI Engineering Buildcamp (`ai-engineering-buildcamp/curriculum.md`) Week 4: Preparing the Project, Testing for Agents, Test Judges

### Notes

Tests call real models, so they are non-deterministic and cost money: the course must say this openly and keep the suite small. Tool-call and message-inspection assertions should work cleanly with the LangGraph/LangChain agent from courses 7–8.

## Lesson outline and source map

FG = AI Engineering Field Guide, LZ = LLM Zoomcamp path, BC = AI Engineering Buildcamp path. `'new'` = no lesson in LZ or BC.

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 9.1 | From notebook to Python project | BC `v2/04-testing/02-preparing-project/02-converting-to-project.md` |
| 9.2 | Writing the first test | BC `v2/04-testing/03-testing/02-first-test.md` |
| 9.3 | Testing tool calls | BC `03-testing/03-testing-tool-calls.md` |
| 9.4 | Refactoring tests and testing output quality | BC `03-testing/04-refactoring-tests.md`, `05-testing-output-quality.md` |
| 9.5 | Creating an LLM judge | BC `v2/04-testing/04-llm-judges/02-creating-judge.md`; FG LLM Evaluation (33.5% AI-First) |
| 9.6 | Coming up with test cases and fixing the agent | BC `04-llm-judges/03–05` |
| 9.7 | Tracking costs | BC `03-testing/06-tracking-costs.md` |
