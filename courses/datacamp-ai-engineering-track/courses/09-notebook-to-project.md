# 9. From Notebooks to Python Projects

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 4. Application quality. 5 lessons, 2-3 hours.

## Summary

Learners turn the internal support assistant notebook into a reproducible Python project that can be imported by tests and run as a containerized FastAPI service.

## Learning objectives

- Identify reusable functions and separate them from notebook setup and exploration
- Define dependencies in `pyproject.toml` and reproduce the environment with `uv`
- Separate tools, configuration, and the agent entry point into Python modules
- Serve a typed answer through FastAPI and smoke-test it in Docker

## Why here

The agent is ready to move out of the notebook. Testing, tracing, and deployment use the resulting project.

## Transformation

Learners can run the assistant from a fresh checkout and import its components individually.

## Theory or application

Application

## Build details

### Syntax / functionality involved

Python modules and imports, `pyproject.toml`, `uv.lock`, environment variables, FastAPI, Pydantic, saved retrieval index, Dockerfile

### How it's used in the exercises

Learners extract the assistant into modules, save its retrieval index, package the API in Docker, and exercise its answer and health endpoints using fixed fixtures.

### Model / release

Python 3.13, `uv`, Pydantic, and the agent stack from the preceding courses.

### Source material

- Buildcamp Week 4, Preparing the Project
- ML Zoomcamp Module 5, `02-pickle.md`, `04-flask-deployment.md`, `05-pipenv.md`, and `06-docker.md`. Adapt the artifact-to-service sequence to FastAPI and uv.

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 9.1 | Extract assistant code and save its retrieval index | ML Zoomcamp Module 5 `05-deployment` (save and load artifacts); BC Week 4 |
| 9.2 | Lock Python dependencies with uv | ML Zoomcamp Module 5 `05-deployment` (isolated environments); BC Week 4 |
| 9.3 | Expose the assistant through FastAPI | ML Zoomcamp Module 5 `05-deployment` (serve predictions); adapted from Flask to FastAPI |
| 9.4 | Build a Docker image for the assistant | ML Zoomcamp Module 5 `05-deployment` (containerization) |
| 9.5 | Smoke-test the container from a fresh checkout | ML Zoomcamp Module 5 `05-deployment` (local service verification) |

## Detailed lesson outline

### 9.1 Extract assistant code and save its retrieval index

Move reusable assistant logic into Python modules and export a local retrieval index as a documented artifact.

**Check.** Load the saved index from a fresh process and retrieve a known article.

### 9.2 Lock Python dependencies with uv

Create a Python project with uv and lock dependencies for a supplied checkout.

**Check.** Create a fresh environment from the lockfile and import the package.

### 9.3 Expose the assistant through FastAPI

Wrap the modules in a FastAPI endpoint with a typed request and response.

**Check.** Send a fixture request and verify the returned answer and source IDs.

### 9.4 Build a Docker image for the assistant

Write a Dockerfile that installs locked dependencies and starts FastAPI with the packaged retrieval index.

**Check.** Build the image and check that its health endpoint responds.

### 9.5 Smoke-test the container from a fresh checkout

Run the container with fixture configuration and send a question to its answer endpoint.

**Check.** Verify that the documented commands reproduce the expected answer and sources.
