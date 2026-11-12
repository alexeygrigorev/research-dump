# 9. Testing AI Applications

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 4. Quality. 7 lessons, 2–3 hours.

## Summary

A notebook that works once is not an application. Learners turn the agent into a Python project and write tests for it: tests for tool calls, tests for output properties, and LLM-judge tests for behaviour that cannot be checked with an assert.

## Learning objectives

- Refactor notebook code into a testable Python project
- Write tests that check which tools an agent called and with what arguments
- Write tests for output properties such as references and code blocks
- Create an LLM judge and use it inside tests
- Track the cost of a test run

## Why here

First Quality course: testing uses habits software engineers already have, and gives the project structure that evaluation, monitoring and CI/CD need.

## Transformation

From "it worked when I tried it" to "I have a test suite that tells me when my agent breaks."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

Project layout with uv, pytest tests and fixtures, inspecting agent messages for tool calls, assertion helpers, LLM judge with structured output (pass/fail + reasoning), usage and cost accounting

### How it's used in the exercises

The learner moves the agent into modules, writes a first test, adds tool-call tests, then writes a judge prompt, runs the suite, sees a failure, fixes the agent instructions and reruns. At the end they print the cost of the run.

### Model / release

Python 3.13; pytest (version TBC), pydantic-ai>=1.55.0, openai>=2.38.0, uv (version TBC). Small model for the agent; the judge may use a different model (discussed in the lesson).

### Source material

- AI Engineering Buildcamp (Maven course; repo ai-engineering-buildcamp, curriculum.md) Week 4: Preparing the Project, Testing for Agents, Test Judges

### Notes

Tests call real models, so they are non-deterministic and cost money: the course must say this openly and keep the suite small.

## Lesson outline and source map

LZ = LLM Zoomcamp path, BC = AI Engineering Buildcamp path. 'new' = no lesson in either source.

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 9.1 | From notebook to Python project | BC v2/04-testing/02-preparing-project/02-converting-to-project.md |
| 9.2 | Writing the first test | BC v2/04-testing/03-testing/02-first-test.md |
| 9.3 | Testing tool calls | BC 03-testing/03-testing-tool-calls.md |
| 9.4 | Refactoring tests and testing output quality | BC 03-testing/04-refactoring-tests.md, 05-testing-output-quality.md |
| 9.5 | Creating an LLM judge | BC v2/04-testing/04-llm-judges/02-creating-judge.md |
| 9.6 | Coming up with test cases and fixing the agent | BC 04-llm-judges/03–05 |
| 9.7 | Tracking costs | BC 03-testing/06-tracking-costs.md |
