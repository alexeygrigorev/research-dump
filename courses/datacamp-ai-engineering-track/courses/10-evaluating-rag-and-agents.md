# 10. Evaluating RAG and Agents

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 4. Quality. 7 lessons, 2–3 hours.

## Summary

Tests say whether something broke; evaluation says how good the system is. Learners build a ground-truth dataset, generate synthetic questions, measure retrieval and answer quality, align an LLM judge with human labels, and use the numbers to choose between versions.

## Learning objectives

- Build an evaluation dataset from real and synthetic questions
- Measure retrieval quality and answer quality separately
- Create an LLM judge and check its agreement with human labels
- Run an evaluation over two versions of a system and decide which one ships

## Why here

Follows testing (judges are already familiar) and comes before monitoring, where the same judges run on live traffic.

## Transformation

From "the answers look fine to me" to "I can measure how good my application is and prove that a change improved it."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

Ground-truth generation with an LLM, batch runs over a dataset, hit rate/MRR, LLM-as-a-judge with structured output, judge-vs-human agreement, comparing prompts and models in a results table

### How it's used in the exercises

The learner generates questions for each document, runs the assistant over them, labels a small sample by hand, writes a judge, checks where the judge disagrees with their labels and fixes the judge prompt, then evaluates two prompt/model variants and picks one.

### Model / release

Python 3.13; pandas>=3.0.3, openai>=2.38.0, pydantic-ai>=1.55.0, tqdm>=4.67.3, minsearch>=0.1.0. Cheap model for generation; the judge model is a lesson topic.

### Source material

- LLM Zoomcamp (github.com/DataTalksClub/llm-zoomcamp) Module 4 Evaluation (all lessons)
- AI Engineering Buildcamp (Maven course; repo ai-engineering-buildcamp, curriculum.md) Week 6: Measure: Offline Evaluation for Agents, Synthetic Evaluation Data

### Notes

Dataset sizes must stay small (tens of questions) to keep API cost and run time inside a 20–30 minute lesson; a pre-computed larger result file can be provided for analysis.

## Lesson outline and source map

LZ = LLM Zoomcamp path, BC = AI Engineering Buildcamp path. 'new' = no lesson in either source.

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 10.1 | Why evaluate: offline and online | LZ 04-evaluation/01-intro.md, 11-evaluation-intro.md |
| 10.2 | Ground truth and synthetic questions | LZ 02-ground-truth.md, 03-ground-truth-batch.md; BC v2/06-evaluation/03-synthetic-data/02-generating-questions.md |
| 10.3 | Evaluating retrieval | LZ 04-search-evaluation.md, 05-search-metrics.md |
| 10.4 | Evaluating answers | LZ 12-rag-answers.md; BC v2/06-evaluation/02-measure/04-gold-standard-dataset.md |
| 10.5 | LLM as a judge and judge alignment | LZ 13-llm-as-judge.md; BC 02-measure/05-judge-alignment.md |
| 10.6 | Evaluating agents on scenarios | LZ 14-agent-evaluation.md; BC 02-measure/03-running-scenarios.md, 06-running-evals.md |
| 10.7 | Using results to choose a version | LZ 06-search-tuning.md; BC 03-synthetic-data/04-judging-synthetic-data.md |
