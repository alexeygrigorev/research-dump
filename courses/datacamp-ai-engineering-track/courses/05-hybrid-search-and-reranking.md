# 5. Hybrid Search and Reranking

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 2. Retrieval. 6 lessons, 2–3 hours.

## Summary

Neither keyword nor vector search wins on every query. Learners combine both into hybrid search, rerank the candidates, measure retrieval quality with hit rate and MRR, and express the pipeline using LangChain retrievers (LangChain appears in 21.1% of all jobs and 29.1% of AI-First roles).

## Learning objectives

- Combine keyword and vector results into one hybrid ranking
- Add a reranking step and explain the precision/latency trade-off
- Measure retrieval quality with hit rate and MRR on a ground-truth set
- Express and tune a hybrid retrieval pipeline in LangChain

## Why here

Needs both search types (courses 2 and 4). It also gives a first, metrics-driven contact with evaluation and introduces LangChain retrievers before agents.

## Transformation

From "I have two search methods" to "I can combine, tune and measure retrieval and express it in an industry-standard library."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

Score fusion (reciprocal rank fusion), reranking retrieved candidates, hit rate and MRR functions, boosting and parameter tuning, the same pipeline expressed with LangChain retrievers

### How it's used in the exercises

The learner runs keyword, vector and hybrid search on a provided ground-truth file, computes hit rate and MRR for each, adds a reranker, fills in a comparison table to pick the best configuration, and expresses the retriever in LangChain.

### Model / release

Python 3.13; `minsearch>=0.1.0`, `sentence-transformers>=5.5.0`, `pandas>=3.0.3`, `langchain` / `langchain-core` (version TBC). Reranking with a local cross-encoder or a small LLM.

### Source material

- **FG** (AI Engineering Field Guide, 9,760 jobs): RAG 40.1% (49% pull in vector DBs), LangChain 21.1% (29.1% AI-First), Model/LLM Evaluation (61.8% AI-First)
- **LZ**: LLM Zoomcamp (`github.com/DataTalksClub/llm-zoomcamp`) Module 6 Best Practices: `02-hybrid-search.md`, `03-reranking.md`, `04-langchain.md`; Module 4: `05-search-metrics.md`, `06-search-tuning.md`

### Notes

The source notebooks use Elasticsearch for hybrid search; an Elasticsearch service is probably not available in the AI tutor environment, so the plan uses `minsearch`/`sqlitesearch` + LangChain retrievers for the same concept.

## Lesson outline and source map

FG = AI Engineering Field Guide, LZ = LLM Zoomcamp path, BC = AI Engineering Buildcamp path. `'new'` = no lesson in LZ or BC.

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 5.1 | Where each search type fails | LZ `06-best-practices/01-intro.md` |
| 5.2 | Hybrid search | LZ `06-best-practices/02-hybrid-search.md` |
| 5.3 | Measuring retrieval: hit rate and MRR | LZ `04-evaluation/05-search-metrics.md`; FG Evaluation (61.8% AI-First) |
| 5.4 | Reranking | LZ `06-best-practices/03-reranking.md` |
| 5.5 | Tuning search parameters | LZ `04-evaluation/06-search-tuning.md` |
| 5.6 | The same pipeline in LangChain | LZ `06-best-practices/04-langchain.md`; FG LangChain (21.1%) |
