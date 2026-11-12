# 5. Hybrid Search and Reranking

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 2. Retrieval. 6 lessons, 2–3 hours.

## Summary

Neither keyword nor vector search wins on every question. Learners combine both into hybrid search, rerank the candidates, and measure each change so that retrieval improvements are based on numbers, not impressions.

## Learning objectives

- Combine keyword and vector results into one hybrid ranking
- Add a reranking step and explain the precision/latency trade-off
- Measure retrieval quality with hit rate and MRR on a ground-truth set
- Choose a retrieval setup for a dataset and justify it with metrics

## Why here

Needs both search types (courses 2 and 4). It also gives a first, light contact with measurement before the full evaluation course.

## Transformation

From "I have two search methods" to "I can combine and tune retrieval and show that it got better."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

Score fusion (reciprocal rank fusion), reranking retrieved candidates, hit rate and MRR functions, boosting and parameter tuning, the same pipeline expressed with LangChain retrievers

### How it's used in the exercises

The learner runs keyword, vector and hybrid search on a provided ground-truth file, computes hit rate and MRR for each, adds a reranker, and fills in a comparison table to pick the best configuration.

### Model / release

Python 3.13; minsearch>=0.1.0, sentence-transformers>=5.5.0, pandas>=3.0.3, langchain (version TBC, one lesson). Reranking with a local cross-encoder or a small LLM.

### Source material

- LLM Zoomcamp (github.com/DataTalksClub/llm-zoomcamp) Module 6 Best Practices: 02-hybrid-search.md, 03-reranking.md, 04-langchain.md; Module 4: 05-search-metrics.md, 06-search-tuning.md

### Notes

The source notebooks use Elasticsearch for hybrid search; an Elasticsearch service is probably not available in the AI tutor environment, so the plan uses minsearch/sqlitesearch for the same concept.

## Lesson outline and source map

LZ = LLM Zoomcamp path, BC = AI Engineering Buildcamp path. 'new' = no lesson in either source.

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 5.1 | Where each search type fails | LZ 06-best-practices/01-intro.md |
| 5.2 | Hybrid search | LZ 06-best-practices/02-hybrid-search.md |
| 5.3 | Measuring retrieval: hit rate and MRR | LZ 04-evaluation/05-search-metrics.md |
| 5.4 | Reranking | LZ 06-best-practices/03-reranking.md |
| 5.5 | Tuning search parameters | LZ 04-evaluation/06-search-tuning.md |
| 5.6 | The same pipeline in a framework (LangChain) | LZ 06-best-practices/04-langchain.md |
