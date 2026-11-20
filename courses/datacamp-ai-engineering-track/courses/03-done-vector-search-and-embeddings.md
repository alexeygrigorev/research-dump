# 3. Vector Search and Embeddings - DONE

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 2. Retrieval and document processing. 8 lessons, 2-3 hours.

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

The learner embeds sentences and compares similarities by hand, embeds chunks from the same conference speaker handbook, compares search results on keyword-heavy queries and paraphrases using labeled expected source IDs, swaps vector search into RAG, and queries a persistent vector database.

### Model / release

Python 3.13; `sentence-transformers>=5.5.0`, `minsearch>=0.1.0`, `sqlitesearch>=0.0.5`, `psycopg[binary]>=3.3.4` (only if `pgvector` is available), `numpy` (version TBC). Embedding model runs locally on CPU; no LLM-specific requirement.

### Source material

- **FG** (AI Engineering Field Guide, 9,760 jobs): Vector Databases 2,201 jobs (#1 database skill), PostgreSQL 1,020 (#2), Pinecone 678, Weaviate 463, Embeddings 16.3% (23.2% AI-First; 36% co-occurrence with RAG), SQL 14.6%
- **FG learning paths / portfolio** (`learning-paths/README.md`, `portfolio/`, commit `1556dcb2`): PostgreSQL is "the default database"; vector databases (Pinecone, Weaviate, Qdrant, pgvector) are a "differentiator".
- **LZ**: LLM Zoomcamp (`github.com/DataTalksClub/llm-zoomcamp`) Module 2 Vector Search (all lessons)
- **BC**: AI Engineering Buildcamp (`ai-engineering-buildcamp/curriculum.md`) Week 1: Search Bonus Materials: Vector search; Week 2: Vector Search with Qdrant

### Notes

Embeddings run locally on CPU. Bundle the vectors for the graded comparisons. Learners can persist and reopen a real SQLite index in the exercise environment. For the PostgreSQL lesson, provide a service with the pgvector extension or a recorded query result to interpret alongside the SQL.

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 3.1 | Keyword vs. Semantic Search | LZ `02-vector-search/01-intro.md` |
| 3.2 | Embeddings and Similarity | LZ `02-embeddings.md`; FG Embeddings (23.2% AI-First) |
| 3.3 | Generating Document Embeddings | LZ `03-embeddings-dataset.md`; `09-onnx-embedder.md` |
| 3.4 | Vector Search from Scratch | LZ `04-vector-search.md`; BC `v2/01-foundation/05-advanced-search/02-vector-search.md` |
| 3.5 | Building a Vector Index | LZ `05-minsearch-vector.md` |
| 3.6 | Vector Search for RAG | LZ `06-rag-vector.md` |
| 3.7 | Vector Search with SQLite | LZ `07-sqlitesearch-vector.md` |
| 3.8 | Vector Search with pgvector | LZ `08-pgvector.md`; FG Vector DBs / PostgreSQL |

## Detailed lesson outline

### 3.1 Keyword vs. Semantic Search

Run two queries against the keyword index from course 2. One uses the heading “Final Slides” and the other asks “Where do I send in my deck?” Both speakers need the same section.

**Check.** Record the rank of the expected section in the first three results for each query. Mark it as missing if it falls outside those results. Save this baseline for lesson 3.5.

### 3.2 Embeddings and Similarity

Embed two paraphrases and an unrelated sentence. Compare their cosine similarities.

**Check.** Identify the closest pair from the computed scores.

### 3.3 Generating Document Embeddings

Batch-embed each handbook chunk’s heading and text. Keep each vector paired with its chunk ID and its parent section ID so a search hit can be turned back into a citation.

**Check.** Verify that there is one vector per chunk. Look up a supplied matrix row by position and confirm its associated chunk ID, text, and section against the source.

### 3.4 Vector Search from Scratch

Embed a query and rank the stored vectors by cosine similarity with NumPy.

**Check.** Compare the top IDs against a small fixture with known vectors.

### 3.5 Building a Vector Index

Index the same chunks with MinSearch VectorSearch. Use unit-length document and query vectors so a dot-product ranking agrees with the cosine ranking from lesson 3.4. Run both queries from lesson 3.1.

**Check.** Compare the rank of “Final Slides” under both methods for each query. Use the supplied embeddings for grading so everyone compares the same rankings.

### 3.6 Vector Search for RAG

Replace keyword retrieval in the RAG pipeline with vector retrieval. Keep the answer and citation format the same.

**Check.** Check that the paraphrased question retrieves and cites the supporting passage.

### 3.7 Vector Search with SQLite

Persist the conference handbook embeddings and source IDs in a local SQLite file using sqlitesearch. Reopen the file and rerun the final-slides query.

**Check.** Verify the persisted index returns the expected section ID.

### 3.8 Vector Search with pgvector

Load the same embeddings and source IDs into a provided PostgreSQL table with a pgvector column. Write a SQL query that orders results by cosine distance and limits the output to the top matches.

**Check.** Verify the expected section ID and inspect the returned distances. Use supplied query results if the exercise runner lacks PostgreSQL.
