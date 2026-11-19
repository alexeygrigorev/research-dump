# 4. Processing PDFs with LLMs

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 2. Retrieval and document processing. 6 lessons, 2-3 hours.

## Summary

Learners convert a text-based handbook PDF into typed records that retain supporting excerpts. The exercises follow the Buildcamp chapter on books from text extraction through structured output and batch processing.

## Learning objectives

- Extract Markdown from a PDF and preserve document IDs
- Choose the pages to process and check for empty or incomplete extracts
- Use structured output and Pydantic to turn page text into validated records
- Process a group of pages and export records with their source references and extraction errors

## Why here

The preceding RAG preparation work establishes the shape of a searchable document record. This course handles PDF-specific extraction and teaches the typed document pipeline used for invoice processing in the capstone.

## Transformation

From having a PDF to having validated records that can be traced back to the supporting excerpts.

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

PyMuPDF page extraction, Markdown, Pydantic schemas, structured output, bounded thread pools, and JSONL.

### How it's used in the exercises

Learners extract the text from the conference speaker handbook PDF, then use a typed schema to extract speaker deliverables, deadlines, and submission destinations. They run the code over multiple pages, record failed extractions by page, and export JSONL for later indexing. Assessment checks the supporting excerpts, field values and error records against fixtures.

### Model / release

Python 3.13, `pymupdf>=1.26.7`, `openai>=2.38.0` and Pydantic. Use a small OpenAI model with structured output for the demonstration and recorded responses for grading.

### Source material

- **BC**: Week 2 Books module, PDF extraction, structured output, processing all pages and parallel processing. Week 1 document processing homework supplies the exercise pattern.
- **FG**: Document processing rose from 13.3% to 16.0% of postings between February and November.

### Notes

Bundle a text-based PDF with a table, a multi-page submission section and an empty page so learners can verify extraction quality before parsing.

## Exercise adapted from the Buildcamp

Extract a text-based PDF to Markdown, retain the supporting text, and validate a speaker deliverable with a Pydantic schema. Extend the exercise to several pages, then grade extraction boundaries, supporting excerpts and validated records against fixtures.

[Buildcamp Week 1 source](https://github.com/alexeygrigorev/ai-bootcamp/blob/60cc917c776e74d3aaeffb2d24f8f93c320e4b8b/v2/01-foundation/homework/01-homework.md)

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 4.1 | Extract text from the speaker handbook PDF | `v2/02-rag-usecases-tech/04-books/02-extracting-text-from-pdfs.md` |
| 4.2 | Clean headers and line breaks in the extracted text | `v2/02-rag-usecases-tech/04-books/02-extracting-text-from-pdfs.md`; `v2/01-foundation/homework/01-homework.md` |
| 4.3 | Extract speaker deliverables and deadlines | `v2/02-rag-usecases-tech/04-books/03-structured-output.md` |
| 4.4 | Extract records from all handbook pages | `v2/02-rag-usecases-tech/04-books/06-processing-all-pages.md` |
| 4.5 | Retry failed PDF extractions | `v2/02-rag-usecases-tech/04-books/07-parallel-processing.md` |
| 4.6 | Export speaker deliverables as JSONL | `v2/02-rag-usecases-tech/04-books/06-processing-all-pages.md` |

## Detailed lesson outline

### 4.1 Extract text from the speaker handbook PDF

Extract text from the PDF version of the conference speaker handbook and compare it with the rendered handbook.

**Check.** Confirm the final-slides instructions appear in the extract.

### 4.2 Clean headers and line breaks in the extracted text

Remove repeating headers and repair line wraps before passing the text to the model.

**Check.** Verify that cleaning preserves the upload instructions and deadline.

### 4.3 Extract speaker deliverables and deadlines

Use a Pydantic schema with deliverable, due date, and submission destination to parse slide and bio instructions.

**Check.** Match extracted values to the handbook and check that an omitted date stays null.

### 4.4 Extract records from all handbook pages

Run typed extraction over the complete PDF and collect records.

**Check.** Compare the collected deliverables with the supplied expected set.

### 4.5 Retry failed PDF extractions

Process PDF pages with bounded concurrency and save failed inputs for a retry.

**Check.** Verify that a retry adds the missing record without duplicating successful records.

### 4.6 Export speaker deliverables as JSONL

Write the validated records with the handbook document ID and supporting text.

**Check.** Reload the file and match a deadline to the corresponding passage.
