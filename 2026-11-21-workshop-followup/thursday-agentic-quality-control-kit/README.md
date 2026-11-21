# Agentic Quality Control for Android Apps: Summary & Working Kit

The practical agentic development workflow from Alexey Grigorev's talk (**Scaling AI Agent Teams Without Quality Compromises**, 114 slides), distilled into a step-by-step kit with role prompts, issue format, verification loops, and a checklist for each stage.

By Alexey Grigorev. PDF version: [agentic-quality-control-android-kit.pdf](agentic-quality-control-android-kit.pdf).

- **Talk recording:** [Agentic Quality Control for Android Apps (YouTube)](https://youtu.be/RQuBX3OTiT4)
- **Slides (PDF):** [scaling-ai-agent-teams-slides.pdf](scaling-ai-agent-teams-slides.pdf)
- **Slides (Google Slides):** [Scaling AI Agent Teams Without Quality Compromises](https://docs.google.com/presentation/d/1wrH2we0J4atE3Dt2afbhygyoyATCLybGIBdfj84IMYM/edit)

## How to use it

1. Do not start with a heavy multi-agent pipeline on an empty repo. Build a working prototype first with a clear spec and one implementer agent.
2. Add the **implementer-verifier** loop as soon as the app has real user flows.
3. Copy the role prompts below into `.claude/agents/` or your agent harness of choice (`CLAUDE.md` / `AGENTS.md`).
4. Tick the box when the workflow step runs cleanly in your repo, not when an agent claims it is ready.

Companion resources mentioned in the talk & slides:
- Blog post: [I Built an AI Agent Team for Software Development](https://aishippingblog.com/p/i-built-an-ai-agent-team-for-software)
- Agent definitions: [AI-Shipping-Labs/website `.claude/agents`](https://github.com/AI-Shipping-Labs/website/tree/main/.claude/agents)
- Process doc: [AI-Shipping-Labs/website `_docs/PROCESS.md`](https://github.com/AI-Shipping-Labs/website/blob/main/_docs/PROCESS.md)
- Tuesday workshop kit: [Full-Stack Vibe Coding Kit](../tuesday-full-stack-vibe-coding-kit/README.md)

## Why Vibe Coding Fails Without Structure

Prompting "make android app pls no mistakes" and piling on features without structure fails for three reasons:
1. **No specs** — agents fill gaps with guesses and overcomplicate the codebase.
2. **No process** — no clear handoff between planning, implementation, and review.
3. **No quality control** — the same agent session rubber-stamps its own work.

The fix has four pillars: **Specs**, **Process**, **Quality control**, and an **Agent team**.

## Stage 1: Specifications Before Code

### [ ] 1. Brainstorm a crisp product specification

Start with a conversational model (for example, ChatGPT in thinking/pro mode) or voice dictation to nail down the user flow before writing code:

```text
I want to build <your app, for example: an Android habit tracker>.

Help me clarify the exact user flow and edge cases. Give me options where choices matter. Focus on product behavior, not implementation details.

Ask me one question at a time and keep your output short.
```

### [ ] 2. Add a PM agent and `issue-format.md`

A PM agent sits between your raw idea and the developer agent. It turns a task into a groomed, unambiguous spec with explicit **Out of scope** items and testable **Acceptance criteria (AC)**.

`.claude/agents/pm.md`:

```text
You are the PM on this project. You turn the task into a groomed, unambiguous spec that an engineer can implement without asking questions.
Read code to understand the current behavior and create a task definition that follows issue-format.md.
Never write application code.
```

`issue-format.md`:

```text
Context
<what exists today, relevant files, constraints, decisions>

Requirements
<numbered, concrete behaviours; what is in scope>

Out of scope
<what is deliberately not part of this task>

Acceptance criteria
AC1. <one verifiable statement: Given / When / Then, or an observable result>
AC2. <...>
```

## Stage 2: The Implementer-Verifier Pattern

Agents are lazy by default: if you ask the same session to verify its own work, it will often rubber-stamp it. Always verify in a **fresh session** with a separate agent.

### [ ] 3. Implement with a fresh Developer session (`.claude/agents/dev.md`)

```text
You are the software engineer on this project. You implement a groomed task so that every acceptance criterion in the task passes.

Make small, focused commits explaining your decisions. When done, add implementation notes and do not mark the task accepted yourself.
```

### [ ] 4. Verify in a fresh QA session (`.claude/agents/qa.md`, expect 2-4x overhead)

```text
You are the QA engineer on this project. You decide whether an implemented task meets its acceptance criteria (AC). You do not fix code.

Run every check against the actual app, tests, and diffs. Return either:
- ACCEPT (with exact command outputs and evidence), or
- REJECT (listing each failing AC with reproduction steps).
```

If QA returns `REJECT`, send only the failing criteria back to a fresh developer session and loop (typically 2-3 rounds). Expect QA loops to multiply task time and token usage by 2-4x, which is worth it for reliability.

### [ ] 5. Close with a PM acceptance pass

Before merging, let the PM agent review the QA evidence from the user's perspective and either approve closing the issue or send it back for one more pass.

### [ ] 6. Apply the same pattern to Design and Writing

The implementer-verifier pattern works beyond code:

- **Designer + Senior Designer** (`.claude/agents/designer.md`): Audit a page for visual consistency, hierarchy, spacing, color token usage, and accessibility, and read `_docs/design-system.md` before any audit so the UI agent stops inventing ad-hoc layouts.
- **Writer + Editor**: Dictate a rough brain dump, structure it into a draft, and run an Editor agent against a style guide to remove robotic phrasing before you edit by hand.

## Stage 3: CI/CD, On-Call, and Parallel Pipelines

### [ ] 7. Add an On-Call Engineer agent for CI/CD

When a push breaks GitHub Actions, an on-call agent inspects the failure, fixes small issues, or escalates to a developer session so `main` stays green:

```text
You are the on-call engineer. Monitor the CI/CD pipeline after each push.

If a workflow fails:
1. Read the failing job logs and reproduce the error locally.
2. If it is a small, clear fix, fix it, run the checks, and commit.
3. If it requires a larger change or product decision, escalate with the root cause.
```

### [ ] 8. Parallelize pipelines with an Orchestrator and git worktrees

Once individual tasks are reliable, use a main orchestrator session (`AGENTS.md` + `process.md`) to run non-overlapping tasks in parallel:

```text
Read `process.md` and fetch open issues.

Group non-overlapping issues that can run in parallel. For each task:
1. Create an isolated git worktree (`git worktree add ../wt/<slug> -b task/<slug>`).
2. Run PM -> Developer -> QA -> PM acceptance inside that worktree.
3. Rebase on `main`, verify CI is green, merge, and remove the worktree.
```

### [ ] 9. Keep `process.md` living and compact

Whenever the pipeline hits a new failure mode, tell the orchestrator:

```text
Analyze what went wrong in this run and update `process.md` so it does not happen again.
```

Periodically ask the agent to compress `process.md` by ~50% so instructions stay sharp without bloating the context window.

## Stage 4: Android-Specific Quality Control

Mobile QA is heavier than web QA because emulators consume significant RAM and CPU.

### [ ] 10. Run Android emulator checks in CI/CD

Local machines usually handle 1 emulator (or 3-4 on a 64 GB RAM cloud box), which bottlenecks parallel agent pipelines. Move emulator tests into CI/CD before merge so every branch gets its own parallel emulator runner.

### [ ] 11. Connect a real Android device for end-to-end QA

Emulators miss real-device quirks. Dedicate a low-cost mini PC connected to a real Android phone over USB debugging (`adb`):

1. Enable **Developer options** and **USB debugging** on the test phone.
2. Attach the phone to a dedicated QA host (for example, a mini PC running the QA agent).
3. Have the QA agent install the built APK via `adb install`, launch the app, tap through the acceptance-criteria flows, and inspect screenshots/logs before reporting `ACCEPT`.

## Key Takeaways (from the Slides)

1. **Use AI to help you with specs** — nail down user flows, edge cases, and testable acceptance criteria before coding.
2. **Implementer-verifier pattern** — never let the same session rubber-stamp its own work (Dev/QA, Designer/Sr. Designer, Writer/Editor).
3. **Create teams of agents** — specialized roles (`pm.md`, `dev.md`, `qa.md`, `designer.md`, `oncall.md`) following `_docs/PROCESS.md` (`Task -> PM -> Dev -> QA -> PM -> OnCall`).
4. **Use an orchestrator to manage them** — run non-overlapping tasks in parallel across isolated git worktrees.
