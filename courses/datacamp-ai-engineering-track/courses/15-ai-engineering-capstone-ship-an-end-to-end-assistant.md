# 15. AI Engineering Capstone: Ship an End-to-End Assistant

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 6. Capstone. 7 lessons, 2–3 hours.

## Summary

Learners build one complete application from a new dataset: ingestion, retrieval, an agent with tools, tests, evaluation, an interface, monitoring and deployment. Each lesson adds one layer, and the result is a project they can show.

## Learning objectives

- Plan an AI application from a problem statement and a dataset
- Build the retrieval pipeline and agent and justify the design with evaluation results
- Add tests, monitoring and a user interface
- Package, deploy and document the application so that someone else can run it

## Why here

Final course: it combines every earlier stage on a new problem.

## Transformation

From "I know the individual techniques" to "I can own an AI-powered application from idea to production."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

Everything from courses 1–14: ingestion and chunking, hybrid retrieval, agent with tools, pytest and judge tests, evaluation table, logging and dashboard, Docker, README

### How it's used in the exercises

The learner receives a dataset and a problem statement and builds the application layer by layer with decreasing guidance. Each lesson ends with a check (retrieval metric above a threshold, tests passing, dashboard showing traffic).

### Model / release

Python 3.13; same packages as courses 2–13 (minsearch>=0.1.0, sentence-transformers>=5.5.0, pydantic-ai>=1.55.0, openai>=2.38.0, pytest TBC, streamlit>=1.58.0, pandas>=3.0.3). Model chosen by the learner and justified by evaluation.

### Source material

- LLM Zoomcamp (github.com/DataTalksClub/llm-zoomcamp) Module 7 End-to-End Project (fitness assistant, github.com/alexeygrigorev/fitness-assistant) and project.md
- AI Engineering Buildcamp (Maven course; repo ai-engineering-buildcamp, curriculum.md) Week 7: My Daily Tasks: End-To-End Project Example; Project guidelines, Evaluation criteria, Documentation tips

### Notes

Use a different dataset from the running example of courses 2–11 so the learner cannot copy earlier code. The LLM Zoomcamp project evaluation criteria can be reused as the checklist.

## Lesson outline and source map

LZ = LLM Zoomcamp path, BC = AI Engineering Buildcamp path. 'new' = no lesson in either source.

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 15.1 | The problem, the dataset and the plan | LZ 07-project-example/01-intro.md; project.md |
| 15.2 | Ingestion and retrieval | LZ 07-project-example/07-chunking.md, 02-evaluating-retrieval.md |
| 15.3 | The agent and its tools | BC v2/07-project-bonus/03-complete-example/03-tools.md, 04-agent.md |
| 15.4 | Tests and evaluation | LZ 03-evaluating-rag.md; BC 03-complete-example/06-testing.md, 07-test-judges.md, 09-evals-otel.md |
| 15.5 | Interface | LZ 04-interface.md; BC 03-complete-example/05-creating-app.md |
| 15.6 | Monitoring | LZ 05-monitoring.md; BC 03-complete-example/08-logfire.md |
| 15.7 | Deployment and documentation | BC 03-complete-example/10-deployment.md; v2/07-project-bonus/02-project-work/04-documentation-tips.md; LZ 06-summary.md |
