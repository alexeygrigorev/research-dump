# 12. CI/CD for AI Applications

Part of the [DRAFT DataCamp AI Engineering track plan](../README.md). Stage: 5. Production. 6 lessons, 2–3 hours.

## Summary

Tests and evaluations only help if they run on every change. Learners set up a local Git server with a pipeline runner and build a pipeline that tests the agent, runs the evaluation set as a quality gate, and builds a container image.

## Learning objectives

- Write a pipeline that runs unit and judge tests on every push
- Add an evaluation step that fails the pipeline when quality drops below a threshold
- Handle API keys, cost limits and non-deterministic tests in CI
- Build and tag a container image as a pipeline step

## Why here

Needs the test suite (9), evaluation set (10) and comes right before the deploy courses, which consume the image this pipeline builds.

## Transformation

From "I run tests on my laptop when I remember" to "every change to my AI application is tested, evaluated and packaged automatically."

## Theory or application

Theory and application

## Build details

### Syntax / functionality involved

Gitea repository, act_runner, GitHub-Actions-compatible workflow YAML (jobs, steps, secrets, caching), pytest in CI, evaluation threshold script, docker build

### How it's used in the exercises

The learner pushes the project to the local Gitea instance, writes the workflow file step by step, watches a run fail on a broken prompt, fixes it, then adds the evaluation gate and the image build.

### Model / release

Python 3.13; Gitea and act_runner (versions TBC), Docker, pytest (version TBC), uv (version TBC). Small model for the tests.

### Source material

- Alexey's instruction for this track (use a local alternative for CI/CD)
- AI Engineering Buildcamp (Maven course; repo ai-engineering-buildcamp, curriculum.md) Week 4: Testing for Agents, Test Judges (what the pipeline runs); Week 6 evaluation (the quality gate)
- MLOps Zoomcamp Module 6 Best Practices (CI/CD with GitHub Actions) — to be confirmed as source

### Notes

No-subscription constraint: GitHub Actions is excluded by the brief. Choice: Gitea + act_runner, because it runs fully locally in Docker and uses the same workflow syntax as GitHub Actions, so the skill transfers directly and the learner sees the full push → run → status loop. Fallback if the environment cannot host a service: nektos/act (runs the same workflow file from the command line). Woodpecker was not chosen because its syntax does not transfer to GitHub Actions. This topic is not covered in LLM Zoomcamp or the Buildcamp; the lesson outline is new and needs Alexey's review.

## Lesson outline and source map

LZ = LLM Zoomcamp path, BC = AI Engineering Buildcamp path. 'new' = no lesson in either source.

| Lesson | Title | Source |
| :---- | :---- | :---- |
| 12.1 | Why AI applications need CI/CD | new; builds on BC v2/04-testing |
| 12.2 | A local Git server and runner | new |
| 12.3 | The first pipeline: running tests on push | new; test content from BC v2/04-testing/03-testing |
| 12.4 | Secrets, cost and flaky LLM tests in CI | new; BC 03-testing/06-tracking-costs.md, 04-llm-judges/05-improving-judge-tests.md |
| 12.5 | Evaluation as a quality gate | new; evaluation content from BC v2/06-evaluation/02-measure/06-running-evals.md |
| 12.6 | Building a container image in the pipeline | new |
