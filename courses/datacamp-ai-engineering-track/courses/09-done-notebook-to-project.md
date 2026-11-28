# 9. From Notebooks to Production - DONE

Part of the [DataCamp AI Engineering track plan](../README.md). Stage: 4. Application quality. 6 lessons, 2-3 hours. Each lesson is designed for approximately 20-25 minutes.

## Summary

Learners move a working notebook into an application that another program can call. They organize Python code, load data and models, and expose a validated API. They manage configuration and dependencies, then package the service in a reproducible container.

## Learning objectives

- Move notebook code into importable Python modules
- Load application data, models, and configuration in a fresh process
- Accept requests and return validated responses through an API
- Recreate the environment and run the service in a container

## Why here

Produces the application used by the testing, monitoring, and release courses.

## Transformation

From "my code works in a notebook" to "another program can call my reproducible service."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

Python packages and imports, a read-only SQLite handbook index, a local query embedder, FastAPI, Pydantic, HTTP requests, `pyproject.toml`, `uv.lock`, Docker.

### How it's used in the exercises

Supply a working notebook, a prebuilt handbook index, its matching local embedding model, and a recorded model client for sample speaker questions. Reuse the small schedule and draft store from course 6. Learners keep the real search and fetch tools in the request path. Only the model's choices and final wording are replayed. The index and embedder ship with the example so a clean run can retrieve evidence without downloading a model.

### Model / release

Python 3.13. `openai==3.57.0`, `pydantic==2.14.4`, `minsearch==0.2.0`, `sqlitesearch==0.3.0`, `sentence-transformers==6.3.0`, `fastapi==0.165.0`, `uvicorn==0.54.0`, `uv==0.13.9`, `python-dotenv==1.2.4`. Use DataCamp-funded model API calls. Select the lowest-cost available model that meets the exercise criteria; no fixed model release is required. Docker and local runtime tools are supplied by the exercise workspace; see [Runtime requirements](../runtime.md).

### Source material

The ML Zoomcamp workshop takes a churn prediction from a notebook to a Python script, an HTTP service, a locked environment, and a container. Here the saved file is the searchable handbook, and the request is a speaker question. The Buildcamp supplies the assistant-to-package example. [ML Zoomcamp Module 5 workshop](https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/main/05-deployment/workshop) · [Buildcamp project preparation](https://github.com/alexeygrigorev/ai-bootcamp/tree/60cc917c776e74d3aaeffb2d24f8f93c320e4b8b/v2/04-testing/02-preparing-project)

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 9.1 | From Notebooks to Python Code | ML Zoomcamp Module 5 workshop, starter notebook and script conversion. BC Week 4, converting to a project |
| 9.2 | Loading Data and Models | ML Zoomcamp 5.2, saving and loading. Course 3.7, persistent SQLite search |
| 9.3 | Application Configuration | Course 1 configuration; course 9 application startup |
| 9.4 | Building APIs with FastAPI | ML Zoomcamp workshop, `predict.py` and `test.py`. BC Week 4, structured output |
| 9.5 | Dependency Management with uv | ML Zoomcamp workshop, `pyproject.toml` and `uv.lock` |
| 9.6 | Containerizing with Docker | ML Zoomcamp workshop, Dockerfile and client request |

## Detailed lesson outline

### 9.1 From Notebooks to Python Code

Run the final-slides example in the supplied notebook. Read a sample HTTP request and response for the same question to see what the conference website will need. Move the existing tool functions and the LangChain answer function into a Python package. Take the model client and search dependency as arguments so a script can use the small starter fixtures.

**Check.** From another Python process, import the answer function and call it twice with different questions. The import makes zero model calls. Each call uses its own question and returns the associated answer and source IDs.

### 9.2 Loading Data and Models

The notebook prepared its search data in earlier cells. Configure the script to open the SQLite index from course 3, embed the question with the matching local model, and fetch the text of the highest-ranked section by ID.

**Check.** Start from a directory outside the package and ask “Where do I send my deck?” Resolve the returned ID against the stored section and show the upload instructions. Point the script at a missing index and check that startup identifies the missing file.

### 9.3 Application Configuration

Read asset paths, the model name, and API credentials from the supplied environment configuration. Keep secrets outside source code and load the search index and embedding model once at startup.

**Check.** Start from a different working directory, select another supplied asset path, and verify that a missing credential produces a clear configuration error without printing its value.

### 9.4 Building APIs with FastAPI

Load the search and model dependencies at startup. Define a Pydantic request with a required question and the course 6 response with answer text, source IDs and an optional draft ID. Call the same answer function from `POST /answer` and expose `GET /health` for a startup check.

**Check.** Send the deadline question from a separate client. Its response contains October 15, 2027 and a citation to “Final Slides.” A recorded draft request also returns the ID in the local store. Send a request missing the question and verify that validation rejects it before the model is called.

### 9.5 Dependency Management with uv

Declare the libraries the service imports in `pyproject.toml`, generate `uv.lock`, and recreate the environment with `uv sync --locked` in a clean checkout. Document how to select the recorded client and locate the two search assets.

**Check.** Start the API from that checkout and rerun the client request. Inspect a checkout with a dependency declaration changed after locking and identify why the locked install stops.

### 9.6 Containerizing with Docker

Write a Dockerfile that installs the locked dependencies, copies the package and search assets, and starts Uvicorn. Build the image from a clean checkout, publish the service port and call it from the host.

**Check.** Run the container without mounting the checkout. Check its health, then send the same deadline request and follow its citation back to the handbook. A second image missing the index must fail the startup check before accepting questions.
