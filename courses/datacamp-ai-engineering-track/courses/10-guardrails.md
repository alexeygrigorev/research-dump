# 10. Guardrails for AI Agents

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 3. Agents. 5 lessons, 2-3 hours.

## Summary

Learners add policy checks to the internal support assistant. They validate requests, enforce tool permissions before execution, route ticket submission to human approval, and check the assistant's output before returning it.

## Learning objectives

- Translate an application policy into checks at the input, tool, and output boundaries
- Validate tool arguments and enforce permissions using trusted application data
- Pause for a human decision before a workflow action writes to a ticket store
- Validate output fields and check cited document IDs against retrieved evidence
- Verify behavior on allowed, rejected, and approval-required requests

## Why here

The earlier agent courses give learners a workflow with retrieval and action tools. Learners can see which boundary catches each policy violation before integrating those checks into the capstone.

## Transformation

From building an assistant that can use tools to enforcing when it may use them and what it may return.

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

Typed validation, policy functions, tool preconditions, human approval, structured refusals, output schemas, and citation checks.

### How it's used in the exercises

Give learners a small support policy and a local ticket store. They validate requests before routing, check permission and approval before changing the store, and verify citation IDs against the evidence returned by the search tools. Bundle allowed and denied requests, an approval and a rejection, and a knowledge document containing an instruction to submit a ticket. Grade the returned decision and inspect the fixture store to verify which requests caused a write.

### Model / release

Python 3.13, LangChain or LangGraph for the existing assistant, and Pydantic for structured validation. Use deterministic cases to grade policy enforcement.

### Source material

- **BC** Week 7 Guardrails, `v2/07-project-bonus/04-guardrails-sdk/02-guardrails-sdk.md` and `v2/07-project-bonus/05-guardrails-pydantic/02-guardrails-tool-calls.md`. Adapt the policy and tool-call patterns to the existing assistant.
- **BC** Week 4 Multi-Agent Systems, human-in-the-loop exercises.
- **FG** Guardrails appear in 19.8% of AI-First roles and rose from 10.2% to 17.5% of all roles during the sampled period.

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 10.1 | Turning policy into checks | BC `v2/07-project-bonus/05-guardrails-pydantic/01-introduction.md` |
| 10.2 | Validating requests | BC `v2/07-project-bonus/04-guardrails-sdk/02-guardrails-sdk.md` |
| 10.3 | Checking tool arguments and permissions | BC `v2/07-project-bonus/05-guardrails-pydantic/02-guardrails-tool-calls.md` |
| 10.4 | Approval before a workflow action | BC `v2/04-testing/06-multi-agent/11-14` |
| 10.5 | Checking outputs and citations | BC `v2/07-project-bonus/04-guardrails-sdk/02-guardrails-sdk.md`; new citation exercise |
