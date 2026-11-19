# 4. Processing PDFs with LLMs

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 2. Retrieval and document processing. 6 lessons, 2-3 hours.

## Summary

Learners convert a text-based handbook PDF into typed records that retain page references. The exercises follow the Buildcamp chapter on books from text extraction through structured output and batch processing.

## Learning objectives

- Extract Markdown from a PDF and preserve document IDs and page numbers
- Choose the pages to process and check for empty or incomplete extracts
- Use structured output and Pydantic to turn page text into validated records
- Process a group of pages and export records with their source references and extraction errors

## Why here

The preceding RAG preparation work establishes the shape of a searchable document record. This course handles PDF-specific extraction and teaches the typed document pipeline used for invoice processing in the capstone.

## Transformation

From having a PDF to having validated records that can be traced back to the source pages.

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

PyMuPDF page extraction, Markdown, Pydantic schemas, structured output, bounded thread pools, and JSONL.

### How it's used in the exercises

Learners extract the text from a short help desk handbook, then use a typed schema to extract policy names, eligibility rules and exceptions. They run the code over multiple pages, record failed extractions by page, and export JSONL for later indexing. Assessment checks the page references, field values and error records against fixtures.

### Model / release

Python 3.13, `pymupdf>=1.26.7`, `openai>=2.38.0` and Pydantic. Use a small OpenAI model with structured output for the demonstration and recorded responses for grading.

### Source material

- **BC**: Week 2 Books module, PDF extraction, structured output, processing all pages and parallel processing. Week 1 document processing homework supplies the exercise pattern.
- **FG**: Document processing rose from 13.3% to 16.0% of postings between February and November.

### Notes

Bundle a text-based PDF with a table, a multi-page policy section and an empty page so learners can verify extraction quality before parsing.

## Exercise adapted from the Buildcamp

Extract a text-based PDF to Markdown, preserve page references, and validate a policy record with a Pydantic schema. Extend the exercise to several pages, then grade extraction boundaries, source pages and validated records against fixtures.

[Buildcamp Week 1 source](https://github.com/alexeygrigorev/ai-bootcamp/blob/60cc917c776e74d3aaeffb2d24f8f93c320e4b8b/v2/01-foundation/homework/01-homework.md)

## Lesson outline and source map

All paths are relative to the Buildcamp repository.

TODO let's make titles more concrete like what exactly are we extracting now not clear

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 4.1 | Extract text and page numbers from a PDF | `v2/02-rag-usecases-tech/04-books/02-extracting-text-from-pdfs.md` | TOOD remove page numbders
| 4.2 | Inspect and clean the Markdown extract | `v2/02-rag-usecases-tech/04-books/02-extracting-text-from-pdfs.md`; `v2/01-foundation/homework/01-homework.md` |
| 4.3 | Extract policy records with structured output | `v2/02-rag-usecases-tech/04-books/03-structured-output.md` |
| 4.4 | Process a document page by page | `v2/02-rag-usecases-tech/04-books/06-processing-all-pages.md` |
| 4.5 | Process pages concurrently and record failures | `v2/02-rag-usecases-tech/04-books/07-parallel-processing.md` |
| 4.6 | Export validated records with page citations | `v2/02-rag-usecases-tech/04-books/06-processing-all-pages.md` |

## Detailed lesson outline

### 4.1 Extract text and page numbers from a PDF

Open a text-based PDF and extract the text and page number for selected pages.

**Check.** Compare the extract with the original pages.

### 4.2 Inspect and clean the Markdown extract

Inspect a Markdown extract with repeated headers and broken line wraps. Clean those artifacts while keeping section text.

**Check.** Verify that the page heading and a target passage survive cleanup.

### 4.3 Extract policy records with structured output

Pass an extracted policy page to the model and parse a typed record using the schema from the exercise.

**Check.** Check the normalized fields and that omitted information remains absent.

### 4.4 Process a document page by page

Run the extraction over every page and attach each record to its page of origin.

**Check.** Verify that no page is skipped and the record points back to the right page.

### 4.5 Process pages concurrently and record failures

Process pages with bounded concurrency and use a fixture that fails on one page.

**Check.** Confirm that successful pages are retained and the failed page is recorded.

### 4.6 Export validated records with page citations

Export validated records as JSONL with the PDF name and page citation.

**Check.** Reload the export and match a cited field to the precise page.
