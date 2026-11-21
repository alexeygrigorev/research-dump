# 14. CI/CD for AI Applications - DONE

Part of the [DataCamp AI Engineering track plan](../README.md). Stage: 5. Production. 6 lessons, 2-3 hours. Each lesson is designed for approximately 20-25 minutes.

## Summary

Learners automate the checks needed to release an AI application. They run a local pipeline that executes tests, calls live models for evaluation, and stops when quality falls below the agreed criteria. A passing run produces a container image tied to the tested revision.

## Learning objectives

- Define and run a local CI workflow
- Manage model credentials and evaluation budgets
- Block packaging when tests or evaluations fail
- Build and tag an image for the tested revision

## Why here

Combines the application, regression suite, and evaluation report into a repeatable release process.

## Transformation

From "I run checks by hand" to "each change is checked and packaged through a repeatable pipeline."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

Local checkout, `act`, GitHub Actions workflow YAML (events, jobs, steps, job dependencies, secrets), `pytest` in CI, evaluation threshold script, `docker build`

### How it's used in the exercises

The learner writes a workflow for the application and invokes its push event locally with `act`. A broken tool call fails the deterministic tests. A separate change that drops a citation fails a small benchmark run against the candidate. A passing run produces an image tagged with the tested commit.

### Model / release

Python 3.13. `pytest==9.2.0`, `uv==0.13.9`, `PyYAML==6.0.4`, `openai==3.57.0`, `pydantic==2.14.4`. Use DataCamp-funded model API calls. Select the lowest-cost available model that meets the exercise criteria; no fixed model release is required. Docker and local runtime tools are supplied by the exercise workspace; see [Runtime requirements](../runtime.md).

### Source material

- [Local workflow runner usage](https://nektosact.com/usage/index.html)
- **FG** (AI Engineering Field Guide, 9,760 jobs): CI/CD 36.9% (3,603 jobs; 36.7% AI-First, 40.7% AI-Support), Docker 24.2% (2,366 jobs), Evaluation & Testing 79.0% of Nov responsibilities
- **FG learning paths / portfolio** (`learning-paths/README.md`, `portfolio/`, commit `1556dcb2`): "Testing, CI/CD, code quality - expected of every engineer"; CI/CD is "high value" and Docker "must have".
- Alexey's instruction for this track (use a local alternative for CI/CD)
- **BC**: AI Engineering Buildcamp (`ai-engineering-buildcamp/curriculum.md`) Week 4: Testing for Agents, Test Judges (what the pipeline runs); Week 6 evaluation (the quality gate)
- **AI Dev Tools Zoomcamp**: `03-deployment/01-test-containerize-and-deploy-an-ai-assisted-app.md` (module workflow) and `cohorts/2026/homework/03-deployment/homework.md`, Question 6 (local execution with `act`, tagged images, deployment gated on tests).

### Notes

Use a local workflow runner with a supplied checkout and Docker socket. No GitHub account, hosted Actions runner, or repository push is required. Use workspace-injected model credentials and real model/judge calls for evaluation; apply the supplied cost limit.

## Lesson outline and source map

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 14.1 | Introduction to CI/CD | AI Dev Tools Zoomcamp 2026 deployment homework, Question 6 |
| 14.2 | Running CI Locally | AI Dev Tools Zoomcamp 2026 deployment homework, Question 6 |
| 14.3 | Running Tests in CI | AI Dev Tools Zoomcamp 2026 deployment homework, Question 6; Buildcamp Week 4 |
| 14.4 | Managing API Keys in CI | Buildcamp Week 4 judge and cost exercises |
| 14.5 | Running Evaluations in CI | Buildcamp Week 6 `v2/06-evaluation/02-measure/06-running-evals.md` |
| 14.6 | Building and Tagging Docker Images | AI Dev Tools Zoomcamp 2026 deployment homework, Question 6 |

## Detailed lesson outline

### 14.1 Introduction to CI/CD

Start with two recorded runs of the same change workflow. One fails a model-independent test and produces no release image. The other passes its checks and produces a tagged image.

**Check.** Using the run output, identify the failed command, the skipped job, and the image produced by the successful run.

### 14.2 Running CI Locally

Read the GitHub Actions-compatible workflow YAML and invoke it on the current checkout with act, a local runner for that workflow format. Use the supplied checkout and Docker-capable environment, or inspect the recorded run.

**Check.** Find the push event, job, and completed command in the output.

### 14.3 Running Tests in CI

Add the existing pytest suite to the automatic workflow. Run a valid change and one that sends the wrong tool argument.

**Check.** Show the test failure and verify that downstream jobs do not start.

### 14.4 Managing API Keys in CI

Pass model and judge credentials to the evaluation job through CI secrets or the local runner's secret configuration. Keep credentials out of the workflow file and logs. Use a small evaluation set and a supplied spending limit for real API calls.

**Check.** Verify that the evaluation job can authenticate, that a missing key produces a clear configuration failure, and that secret values do not appear in run output.

### 14.5 Running Evaluations in CI

Run a small benchmark against the current checkout using real model and judge calls, with checks against the actual answers and citations. Attach the candidate commit to the report and pass it to the threshold command. A supplied candidate change drops required citations, giving learners a version whose citation checks fail even when its ordinary tests pass.

**Check.** Check that the candidate regression stops packaging and that a stale report for another commit cannot be reused.

### 14.6 Building and Tagging Docker Images

Build the existing Dockerfile only after the required jobs pass. Tag the image with the commit ID and hand that tag to the Kubernetes exercise.

**Check.** Verify that the tag identifies the tested revision and that a failing run does not produce an eligible release image.
