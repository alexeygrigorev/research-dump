# 2. Building Your First RAG Application

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 1. Foundations. 7 lessons, 2–3 hours.

## Summary

An LLM does not know your company's internal data. Learners build a retrieval-augmented assistant (RAG appears in 40.1% of all jobs and 56.0% of AI-First roles; finding information in company data appears in 43.8% of jobs) over an internal knowledge base: search first, put the results into the prompt, then ask the model.

## Learning objectives

- Explain why RAG is needed for proprietary data and describe its search, prompt and LLM steps
- Index a document collection and query it with keyword search
- Build a prompt that grounds the answer in retrieved context
- Assemble search, prompt and LLM into one reusable RAG pipeline

## Why here

RAG is the most common named pattern in AI engineering postings and the running example for retrieval, agents, evaluation and monitoring later in the track.

## Transformation

From "I can call an LLM" to "I can build an assistant that answers questions from proprietary documents."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

`minsearch` Index (text and keyword fields, boosting, filtering), prompt templates, the `search → build_prompt → llm → rag` functions, loading JSON documents

### How it's used in the exercises

The learner loads an internal documentation/FAQ dataset, builds an index, runs searches and inspects the results, writes the grounded prompt template, and connects the three steps. They then ask questions the plain LLM gets wrong and see the grounded answer.

### Model / release

Python 3.13; `minsearch>=0.1.0`, `openai>=2.38.0`, `requests>=2.28.1`. Any small chat model.

### Source material

- **FG** (AI Engineering Field Guide, 9,760 jobs): RAG 40.1% overall (56.0% AI-First, rising 32.8% → 38.2%), Finding Information in Company Data 43.8% of jobs, RAG app builder archetype 26.6%
- **LZ**: LLM Zoomcamp (`github.com/DataTalksClub/llm-zoomcamp`) Module 1 Agentic RAG, lessons 03–10
- **BC**: AI Engineering Buildcamp (`ai-engineering-buildcamp/curriculum.md`) Week 1: Foundation: LLMs, RAG and Search; Week 2: FAQ Assistant, Reusable RAG class

### Notes

`minsearch` is Alexey's small in-memory search library: no server, runs inside the exercise environment. Dataset must ship with the course (the source fetches it from GitHub). Framing emphasizes internal company knowledge bases over consumer Q&A (which fell -13.8 pp in the field guide between Feb and Nov).

## Lesson outline and source map

FG = AI Engineering Field Guide, LZ = LLM Zoomcamp path, BC = AI Engineering Buildcamp path. `'new'` = no lesson in LZ or BC.

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 2.1 | What RAG is and when you need it | LZ `01-agentic-rag/03-rag.md`; BC `v2/01-foundation/03-rag/04-rag.md`; FG RAG (40.1%) |
| 2.2 | The dataset: internal knowledge documents | LZ `04-dataset.md`; BC `v2/02-rag-usecases-tech/02-faq-assistant/02-dataset.md` |
| 2.3 | Indexing and keyword search | LZ `05-search.md`; BC `03-rag/06-indexing-with-minsearch.md` |
| 2.4 | Building the grounded prompt | LZ `06-building-prompt.md` |
| 2.5 | Calling the LLM with context | LZ `07-llm.md` |
| 2.6 | A reusable RAG pipeline | LZ `08-rag-helper.md`; BC `v2/02-rag-usecases-tech/01-overview/02-rag-class.md` |
| 2.7 | Where simple RAG breaks | LZ `10-rag-next-steps.md` |
