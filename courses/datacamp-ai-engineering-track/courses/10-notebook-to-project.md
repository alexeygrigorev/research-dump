# 10. From Notebooks to Python Projects

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

not clear let's do soemthing similar to module 5 of ml zoomcsmp

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 10.1 | Identify reusable notebook code | BC `v2/04-testing/02-preparing-project/01-section-overview.md` |
| 10.2 | Create the project and lock dependencies | BC `v2/04-testing/02-preparing-project/02-converting-to-project.md` |
| 10.3 | Split tools and agent logic into modules | BC `v2/04-testing/02-preparing-project/02-converting-to-project.md` |
| 10.4 | Define the assistant's output | BC `v2/04-testing/02-preparing-project/05-structured-output.md` |
| 10.5 | Run the assistant from a fresh environment | Adapted from BC `v2/04-testing/02-preparing-project/02-converting-to-project.md` |

## Detailed lesson outline

### 10.1 Identify reusable notebook code

Open the support-assistant notebook and mark setup, reusable logic, and exploratory cells.

**Check.** Identify which functions can be imported without running a model call.

### 10.2 Create the project and lock dependencies

Create a Python project with uv and lock dependencies for a supplied checkout.

**Check.** Create a fresh environment from the lockfile and import the package.

### 10.3 Split tools and agent logic into modules

Move tools, configuration, and agent construction into modules with a separate command entry point.

**Check.** Import a tool in isolation and run it against a fixture.

### 10.4 Define the assistant's output

Define typed output and serialize the CLI answer and source IDs.

**Check.** Verify the resulting JSON against the project’s output schema.

### 10.5 Run the assistant from a fresh environment

Run the command from a clean checkout with the provided fixture configuration.

**Check.** Confirm the documented commands reproduce the expected result.
