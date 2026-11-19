# 14. CI/CD for AI Applications

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 5. Production. 6 lessons, 2-3 hours.

## Summary

**CI/CD** is the most-requested ops skill in the field guide (**36.9%** of all jobs; 3,603 postings, ahead of Docker and Kubernetes), and **Docker** appears in **24.2%** (2,366 postings). Tests and evaluations only help if they run on every change. Learners run a workflow locally with `act` to run `pytest`, enforce an evaluation quality gate, and build a tagged container image.

## Learning objectives

- Write and run a push-triggered workflow locally with deterministic unit and LLM-judge fixtures
- Add an evaluation step that fails the pipeline when quality drops below a threshold
- Handle API keys, cost limits and non-deterministic tests in CI
- Build and tag a Docker image as a pipeline step

## Why here

Needs the test suite (9), evaluation set (10) and directly teaches the CI/CD + Docker skills required across both AI-First (36.7% CI/CD) and AI-Support (40.7% CI/CD) roles.

## Transformation

From "I run tests on my laptop when I remember" to "every change to my AI application is tested, evaluated and packaged automatically."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

Local checkout, `act`, GitHub Actions workflow YAML (events, jobs, steps, job dependencies, secrets), `pytest` in CI, evaluation threshold script, `docker build`

### How it's used in the exercises

The learner writes a workflow for the application and invokes its push event locally with `act`. A broken prompt fixture fails the evaluation gate and skips the image build. After fixing the prompt, the learner reruns the workflow, checks the tagged image, and identifies what would be promoted to a deployment environment.

### Model / release

Python 3.13; `act`, Docker, `pytest`, and `uv`. Graded runs use fixtures for model and judge responses.

### Source material

- **FG** (AI Engineering Field Guide, 9,760 jobs): CI/CD 36.9% (3,603 jobs; 36.7% AI-First, 40.7% AI-Support), Docker 24.2% (2,366 jobs), Evaluation & Testing 79.0% of Nov responsibilities
- **FG learning paths / portfolio** (`learning-paths/README.md`, `portfolio/`, commit `1556dcb2`): "Testing, CI/CD, code quality - expected of every engineer"; CI/CD is "high value" and Docker "must have".
- Alexey's instruction for this track (use a local alternative for CI/CD)
- **BC**: AI Engineering Buildcamp (`ai-engineering-buildcamp/curriculum.md`) Week 4: Testing for Agents, Test Judges (what the pipeline runs); Week 6 evaluation (the quality gate)
- **AI Dev Tools Zoomcamp**: `03-deployment/01-test-containerize-and-deploy-an-ai-assisted-app.md` (module workflow) and `cohorts/2026/homework/03-deployment/homework.md`, Question 6 (local execution with `act`, tagged images, deployment gated on tests).

### Notes

The local run uses a supplied checkout and Docker-capable runner. Exercises can grade the workflow and interpret paired failure/success run logs where container execution is unavailable. Use deterministic checks on every run and discuss a separate budgeted live-model evaluation job.

## Lesson outline and source map

FG = AI Engineering Field Guide, LZ = LLM Zoomcamp path, BC = AI Engineering Buildcamp path. `'new'` = no lesson in LZ or BC.

I don't like the titles they are bad

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 14.1 | Why AI applications need CI/CD | new; builds on BC `v2/04-testing`; FG CI/CD (36.9%) | I don't like titles that start with WHY etc let's find all of them and replace
| 14.2 | Run a workflow locally with act | AI Dev Tools Zoomcamp 2026 deployment homework, Question 6 | focus on what how tech 
| 14.3 | Add tests to the push workflow | AI Dev Tools Zoomcamp 2026 deployment homework, Question 6; BC `v2/04-testing/03-testing` | 
| 14.4 | Secrets, cost and flaky LLM tests in CI | new; BC `03-testing/06-tracking-costs.md`, `04-llm-judges/05-improving-judge-tests.md` |
| 14.5 | Evaluation as a quality gate | new; evaluation content from BC `v2/06-evaluation/02-measure/06-running-evals.md` |
| 14.6 | Build a tagged image after checks pass | AI Dev Tools Zoomcamp 2026 deployment homework, Question 6; FG Docker (24.2%) |

## Detailed lesson outline

### 14.1 Why AI applications need CI/CD

Inspect a change that breaks the assistant and map which check should stop it before image build.

**Check.** Order tests, evaluation, and image build in a workflow.

### 14.2 Run a workflow locally with act

Run a sample GitHub Actions-compatible workflow on the supplied checkout using act.

**Check.** Locate the local job result and verify a step completed.

### 14.3 Add tests to the push workflow

Add a pytest job to the push workflow and exercise it with good and broken fixtures.

**Check.** Check the expected pass and failure statuses.

### 14.4 Secrets, cost and flaky LLM tests in CI

Configure test inputs and secrets. Use scripted models for required checks and isolate optional live checks.

**Check.** Run the required checks without live credentials.

### 14.5 Evaluation as a quality gate

Implement an evaluation gate from a fixed metrics report and agreed thresholds.

**Check.** Verify exit status for a passing fixture and a regression.

### 14.6 Build a tagged image after checks pass

Build a tagged Docker image after the checks pass.

**Check.** Verify the expected tag and confirm the build step is skipped when a required check fails.
