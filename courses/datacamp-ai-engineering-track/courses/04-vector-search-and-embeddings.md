# 4. Vector Search and Embeddings

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 2. Retrieval. 7 lessons, 2–3 hours.

## Summary

Keyword search misses questions phrased differently from the documents. Learners turn text into embeddings, search by meaning, and plug vector search into the RAG pipeline, first in memory and then in a database.

## Learning objectives

- Explain what embeddings are and compute them for queries and documents
- Implement vector search with cosine similarity and compare it with keyword search
- Replace the search step of a RAG pipeline with vector search
- Store and query vectors in a persistent database

## Why here

Comes after the learner has a working keyword-search RAG, so the benefit of semantic search is visible on the same questions.

## Transformation

From "my search only matches exact words" to "my assistant finds the right document even when the wording differs."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

Sentence-transformers / ONNX embedding models, numpy dot product and cosine similarity, minsearch VectorSearch, sqlitesearch vector index, pgvector SQL operators

### How it's used in the exercises

The learner embeds a few sentences and compares similarities by hand, embeds the FAQ dataset, runs the same queries through keyword and vector search and compares results, then swaps vector search into the RAG function.

### Model / release

Python 3.13; sentence-transformers>=5.5.0, minsearch>=0.1.0, sqlitesearch>=0.0.5, psycopg[binary]>=3.3.4 (only if pgvector is available), numpy (version TBC). Embedding model runs locally on CPU; no LLM-specific requirement.

### Source material

- LLM Zoomcamp (github.com/DataTalksClub/llm-zoomcamp) Module 2 Vector Search (all lessons)
- AI Engineering Buildcamp (Maven course; repo ai-engineering-buildcamp, curriculum.md) Week 1: Search Bonus Materials: Vector search; Week 2: Vector Search with Qdrant

### Notes

Embeddings are computed locally (no GPU, per LLM Zoomcamp). pgvector needs a Postgres service in the environment; if that is not possible, keep the database lesson on sqlitesearch.

## Lesson outline and source map

LZ = LLM Zoomcamp path, BC = AI Engineering Buildcamp path. 'new' = no lesson in either source.

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 4.1 | Why keyword search is not enough | LZ 02-vector-search/01-intro.md |
| 4.2 | Embeddings | LZ 02-embeddings.md |
| 4.3 | Embedding a dataset | LZ 03-embeddings-dataset.md; 09-onnx-embedder.md |
| 4.4 | Vector search from scratch | LZ 04-vector-search.md; BC v2/01-foundation/05-advanced-search/02-vector-search.md |
| 4.5 | Vector search with a library | LZ 05-minsearch-vector.md |
| 4.6 | RAG with vector search | LZ 06-rag-vector.md |
| 4.7 | Vectors in a database | LZ 07-sqlitesearch-vector.md, 08-pgvector.md |
