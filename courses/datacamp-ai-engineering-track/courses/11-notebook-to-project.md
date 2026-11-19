# 11. From Notebooks to Python Projects

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 4. Application quality. 5 lessons, 2-3 hours.

## Summary

Learners turn the internal support assistant notebook into a reproducible Python project that can run from a terminal and be imported by tests or a web service.

## Learning objectives

- Identify reusable functions and separate them from notebook setup and exploration
- Define dependencies in `pyproject.toml` and reproduce the environment with `uv`
- Separate tools, configuration, and the agent entry point into Python modules
- Run the same sample request from a fresh environment

## Why here

The agent is ready to move out of the notebook. Testing, tracing, and deployment use the resulting project.

## Transformation

Learners can run the assistant from a fresh checkout and import its components individually.

## Theory or application

Application

## Build details

### Syntax / functionality involved

Python modules and imports, `pyproject.toml`, `uv.lock`, environment variables, CLI entry point, Pydantic output model

### How it's used in the exercises

Learners extract the assistant’s tools and agent into modules, move runtime configuration into environment variables, and wire up a command that accepts a question and prints a structured response. Grading imports the tools and calls the entry point with fixed model and document fixtures.

### Model / release

Python 3.13, `uv`, Pydantic, and the agent stack from the preceding courses.

### Source material

- Buildcamp Week 4, Preparing the Project

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 11.1 | Identify reusable notebook code | BC `v2/04-testing/02-preparing-project/01-section-overview.md` |
| 11.2 | Create the project and lock dependencies | BC `v2/04-testing/02-preparing-project/02-converting-to-project.md` |
| 11.3 | Split tools and agent logic into modules | BC `v2/04-testing/02-preparing-project/02-converting-to-project.md` |
| 11.4 | Define the assistant's output | BC `v2/04-testing/02-preparing-project/05-structured-output.md` |
| 11.5 | Run the assistant from a fresh environment | Adapted from BC `v2/04-testing/02-preparing-project/02-converting-to-project.md` |
