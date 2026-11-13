# 4. Vector Search and Embeddings

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 2. Retrieval. 7 lessons, 2–3 hours.

## Summary

Keyword search misses questions phrased differently from the documents. Learners compute embeddings (required in 23.2% of AI-First roles; 36% co-occurrence with RAG), search by meaning, and store vectors in a persistent database (Vector Databases: 2,201 jobs, #1 database skill; PostgreSQL/`pgvector`: 1,020 jobs, #2).

## Learning objectives

- Explain what embeddings are and compute them for queries and documents
- Implement vector search with cosine similarity and compare it with keyword search
- Replace the search step of a RAG pipeline with vector search
- Store and query vectors in a persistent SQL/vector database (`sqlitesearch` / `pgvector`)

## Why here

Comes after the learner has a working keyword-search RAG, so the benefit of semantic search and vector databases is visible on the same queries.

## Transformation

From "my search only matches exact words" to "my assistant finds the right document by meaning and stores vectors in a database."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

`sentence-transformers` / ONNX embedding models, `numpy` dot product and cosine similarity, `minsearch` VectorSearch, `sqlitesearch` vector index, `pgvector` SQL operators

### How it's used in the exercises

The learner embeds sentences and compares similarities by hand, embeds the document dataset, runs the same queries through keyword and vector search and compares results, swaps vector search into RAG, and queries a persistent vector database.

### Model / release

Python 3.13; `sentence-transformers>=5.5.0`, `minsearch>=0.1.0`, `sqlitesearch>=0.0.5`, `psycopg[binary]>=3.3.4` (only if `pgvector` is available), `numpy` (version TBC). Embedding model runs locally on CPU; no LLM-specific requirement.

### Source material

- **FG** (AI Engineering Field Guide, 9,760 jobs): Vector Databases 2,201 jobs (#1 database skill), PostgreSQL 1,020 (#2), Pinecone 678, Weaviate 463, Embeddings 16.3% (23.2% AI-First; 36% co-occurrence with RAG), SQL 14.6%
- **LZ**: LLM Zoomcamp (`github.com/DataTalksClub/llm-zoomcamp`) Module 2 Vector Search (all lessons)
- **BC**: AI Engineering Buildcamp (`ai-engineering-buildcamp/curriculum.md`) Week 1: Search Bonus Materials: Vector search; Week 2: Vector Search with Qdrant

### Notes

Embeddings are computed locally (no GPU, per LLM Zoomcamp). `pgvector` needs a Postgres service in the environment; if that is not possible, keep the database lesson on `sqlitesearch` and cover how managed vector databases (Pinecone, Weaviate, Qdrant, `pgvector`) fit the production stack.

## Lesson outline and source map

FG = AI Engineering Field Guide, LZ = LLM Zoomcamp path, BC = AI Engineering Buildcamp path. `'new'` = no lesson in LZ or BC.

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 4.1 | Why keyword search is not enough | LZ `02-vector-search/01-intro.md` |
| 4.2 | Embeddings | LZ `02-embeddings.md`; FG Embeddings (23.2% AI-First) |
| 4.3 | Embedding a dataset | LZ `03-embeddings-dataset.md`; `09-onnx-embedder.md` |
| 4.4 | Vector search from scratch | LZ `04-vector-search.md`; BC `v2/01-foundation/05-advanced-search/02-vector-search.md` |
| 4.5 | Vector search with a library | LZ `05-minsearch-vector.md` |
| 4.6 | RAG with vector search | LZ `06-rag-vector.md` |
| 4.7 | Vectors in a database (`sqlitesearch` & `pgvector`) | LZ `07-sqlitesearch-vector.md`, `08-pgvector.md`; FG Vector DBs / PostgreSQL |
