# 2. Building Your First RAG Application

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 1. Foundations. 7 lessons, 2–3 hours.

## Summary

An LLM does not know your documents. Learners build a question-answering assistant over a real FAQ and documentation dataset: search first, put the results into the prompt, then ask the model. They finish with one small reusable RAG pipeline.

## Learning objectives

- Explain why RAG is needed and describe its search, prompt and LLM steps
- Index a document collection and query it with keyword search
- Build a prompt that grounds the answer in retrieved context
- Assemble search, prompt and LLM into one reusable RAG function

## Why here

RAG is the simplest useful LLM application and the running example for retrieval, agents, evaluation and monitoring later in the track.

## Transformation

From "I can call an LLM" to "I can build an assistant that answers questions from my own documents."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

minsearch Index (text and keyword fields, boosting, filtering), prompt templates, the search → build_prompt → llm → rag functions, loading JSON documents

### How it's used in the exercises

The learner loads a FAQ dataset, builds an index, runs searches and inspects the results, writes the prompt template, and connects the three steps. They then ask questions the plain LLM gets wrong and see the grounded answer.

### Model / release

Python 3.13; minsearch>=0.1.0, openai>=2.38.0, requests>=2.28.1. Any small chat model.

### Source material

- LLM Zoomcamp (github.com/DataTalksClub/llm-zoomcamp) Module 1 Agentic RAG, lessons 03–10
- AI Engineering Buildcamp (Maven course; repo ai-engineering-buildcamp, curriculum.md) Week 1: Foundation: LLMs, RAG and Search; Week 2: FAQ Assistant, Reusable RAG class

### Notes

minsearch is Alexey's small in-memory search library: no server, runs inside the exercise environment. Dataset must ship with the course (the source fetches it from GitHub).

## Lesson outline and source map

LZ = LLM Zoomcamp path, BC = AI Engineering Buildcamp path. 'new' = no lesson in either source.

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 2.1 | What RAG is and when you need it | LZ 01-agentic-rag/03-rag.md; BC v2/01-foundation/03-rag/04-rag.md |
| 2.2 | The dataset: FAQ documents | LZ 04-dataset.md; BC v2/02-rag-usecases-tech/02-faq-assistant/02-dataset.md |
| 2.3 | Indexing and keyword search | LZ 05-search.md; BC 03-rag/06-indexing-with-minsearch.md |
| 2.4 | Building the prompt | LZ 06-building-prompt.md |
| 2.5 | Calling the LLM with context | LZ 07-llm.md |
| 2.6 | A reusable RAG pipeline | LZ 08-rag-helper.md; BC v2/02-rag-usecases-tech/01-overview/02-rag-class.md |
| 2.7 | Where simple RAG breaks | LZ 10-rag-next-steps.md |
