# Full-Stack Vibe Coding: From Spec to Deployed App

All 16 steps and prompts from the Berlin workshop to take an app from a product spec to a containerized, tested, and deployed full-stack product, in one place, with a checkbox for each step.

By Alexey Grigorev. PDF version: [full-stack-vibe-coding-kit.pdf](full-stack-vibe-coding-kit.pdf).

## How to use it

1. Copy the prompts into any coding agent (Claude Code, Codex, OpenCode, Cursor, or others). The kit is tool-agnostic.
2. Start a new session for each step, or delegate implementation to a subagent so only what matters stays in the context window.
3. Replace everything in `<angle brackets>` with your own project details.
4. Tick the box when the step works, not when the agent says it is done.

Reference repo from the workshop: [alexeygrigorev/workshop-berlin](https://github.com/alexeygrigorev/workshop-berlin). Want the agentic quality-control workflow? Get the [Agentic Quality Control for Android Apps Kit](../thursday-agentic-quality-control-kit/README.md).

## Stage 1: Spec and Frontend

### [ ] 1. Product discovery: let the agent interview you, then write `specs.md`

Start with a one-paragraph idea and let ChatGPT (or any chat model) ask the questions. This is the exact opening prompt from the workshop, for the "Where Should We Eat?" app:

```text
<App name>

<One-sentence description, for example: A collaborative restaurant voting app with ranked-choice voting, a countdown, and live results.>

I want to help you figure out what we want to build - this is an idea and I want to make it more concrete before I build it. Ask me as many questions as you like but keep them short and ask one question at a time
```

Answer in a word or two. In the workshop the interview took about a dozen short questions:

| # | Question | Answer |
|---|----------|--------|
| 1 | Who is the app for? | Coworkers |
| 2 | How often will they use it? | Daily |
| 3 | Who can suggest restaurants? | Anyone (plus a pre-filled list of known places) |
| 4 | How do people join a vote? | Both: a permanent team and a shared link |
| 5 | Do saved restaurants appear in every vote? | Automatically |
| 6 | How does a vote start? | Automatically every workday |
| 7 | When does voting close? | 11:30 |
| 8 | When does voting open? | 8:00 |
| 9 | How do people vote? | Rank their top 3 |
| 10 | Live results before closing? | Yes |
| 11 | Are votes anonymous? | No, voter names and choices are visible |

When you run out of opinions, hand the rest over:

```text
visible. make the rest of the choices for me
```

The model then returns a product spec with the decisions it made for you (mobile-first web app, teams with invite links, Borda-style points of 3/2/1 for first/second/third choice, tie-breakers, history, edge cases such as "no votes means no winner", a list of what to leave out of v1, and a definition of a successful MVP). Read it and push back where it feels wrong. In the workshop the drag-to-reorder ranking was the problem:

```text
I'm not sure if dragging will be user friendly if we have many choices
```

The model changed the interaction to tap-to-select the top 3 with search, plus "Recently visited" and "Popular with the team" sections. Only then ask for the file:

```text
now please prepare detailed specification file that I can give to my coding agent. save it to specs.md
```

If the chat can't attach the file, ask where it is ("where's the file?") or ask for the Markdown in the reply. Save the result as `specs.md` at the repository root.

The generated spec also picked a technology stack (Next.js, Supabase, Vercel). Remove those implementation details, or ignore them, before handing the file to a UI generator: you want the frontend builder to focus on user flows, and you choose the backend yourself in later steps.

**Decisions in the workshop spec (MVP v1):**

- Mobile-first responsive web app; Google sign-in or email magic link.
- Permanent teams with invite links; shared saved restaurant list included in every daily vote; any member can add restaurants.
- Voting opens at 8:00 and closes at 11:30 every workday, in the team's timezone; no automatic vote on weekends.
- Rank up to 3 restaurants (3/2/1 points); votes can be changed until 11:30; live rankings with voter names.
- Tie-break: more first-place votes, then a random pick.
- Screens: Today, Restaurants, History, Team.
- Left out of v1: reservations, delivery ordering, AI recommendations, Slack integration, dietary filters, native apps.
- Success: 5-20 coworkers can create a team, save their usual restaurants, rank their top three in under 15 seconds, and have a clear decision at 11:30.

### [ ] 2. Generate the frontend with a UI tool and export to GitHub

Paste `specs.md` into Lovable (or another UI builder with a built-in design system) so you get sensible React, Tailwind, and component defaults without designing from scratch. Export the project to GitHub, then pull it into `frontend/`:

```text
There's a link in README.md. Pull the code from there and put it in ./frontend, then commit and push.
```

### [ ] 3. Remove unwanted backend services and simplify auth

UI builders often wire up a managed backend (such as Supabase) even when you plan to build your own API. Strip it out and replace it with a single-file mock backend:

```text
Remove Supabase. Simplify authentication to login and password, and create a mock backend concentrated in one single file so the frontend runs standalone.
```

Verify locally with `cd frontend && npm install && npm run dev` (use `npm i --legacy-peer-deps` if peer dependencies conflict).

### [ ] 4. Fix UI layout friction with 3 layout options

When an interface feels cramped or jumps around on click, ask the agent to propose three layout options in a fresh session or subagent:

```text
When I interact with the page, adding items pushes other elements down and breaks the layout.

Commit what we have, then propose 3 different layout options so I can pick the cleanest UX.
```

Once you pick one:

```text
Let's go with option <B>. Remove the other options from the code, commit, and push.
```

## Stage 2: API Contract and Backend

### [ ] 5. Extract an OpenAPI contract from the frontend

Design the API so the web frontend, a CLI, or an AI agent can all perform the same actions:

```text
Analyze the frontend in frontend/ and extract every backend call it makes.

Create api/openapi.yaml at the repository root defining every endpoint, method, path, request body, response body, and which endpoints require authentication.
```

Use subagents to inspect the frontend routes and draft the schema.

### [ ] 6. Build a FastAPI backend with an in-memory store

```text
Build a FastAPI backend in backend/ using uv that implements api/openapi.yaml.

Use an in-memory store for now (no database yet) and seed it with a few fake users and sample records so the frontend has something to show.

Add authentication with hashed passwords and bearer tokens for the endpoints that need it.

Split the code into modules: routers, models, store, auth. Write tests.
```

### [ ] 7. Connect the frontend and add a Makefile

```text
Integrate the frontend with the FastAPI backend so it calls the real API instead of the single-file mock.

Create a Makefile so I can easily run `make frontend`, `make backend`, `make backend-test`, and `make frontend-test`.
```

Test the full user flow in the browser (sign in, create an item, reload) and fix any auth or missing-entity errors before moving on.

## Stage 3: Database and Containerization

### [ ] 8. Replace the in-memory store with SQLite and SQLAlchemy

```text
Replace the in-memory store with a database using SQLite and SQLAlchemy.

Use an environment variable (for example WSWE_DATABASE_URL) to configure which DB the server connects to, and keep it database-agnostic so we can add Postgres later.
```

### [ ] 9. Containerize frontend and backend in one image

```text
Create a multi-stage Dockerfile that builds the frontend with Node, then builds a Python image with the backend and the frontend static files. The backend should serve the frontend.
```

### [ ] 10. Add PostgreSQL and Docker Compose

```text
Add Postgres support (psycopg driver and Alembic migrations) so the backend runs against Postgres as well as SQLite.

Create docker-compose.yaml with two services: `db` (Postgres) and the app, and update the Makefile with `make up`, `make db`, `make down`, and `make backend-pg`.
```

Run `make up` and verify the app responds on `http://localhost:8000`.

## Stage 4: Testing, Deployment, and Agent Roles

### [ ] 11. Add an end-to-end Playwright test

```text
Start a subagent to create a Playwright end-to-end test in e2e/ that spins up a throw-away Docker Compose stack, signs in, adds a record, reloads the page, and verifies the record persisted in Postgres.
```

Add `make e2e` to the `Makefile` so the test runs in one command.

### [ ] 12. Propose deployment options and ship to a VPS

```text
I want to deploy this app. Propose 2-3 deployment options and compare cost and complexity.
```

For a single-VM deploy (such as Hetzner Cloud with Docker Compose and Caddy), add `deploy/` scripts (`docker-compose.prod.yml`, `Caddyfile`, `deploy.sh`), strip demo seed data in production (`WSWE_SEED_DEMO_DATA=false`), and verify the live URL.

### [ ] 13. Set up a CI/CD pipeline that deploys the tested image

```text
Create a GitHub Actions CI/CD pipeline (.github/workflows/ci-cd.yml) that:
- runs backend and frontend tests
- builds the Docker image once and runs the e2e test against it
- deploys the exact tested image to production
```

### [ ] 14. Add zero-downtime rollout

```text
What happens if users are using the app while we deploy? How can we avoid downtime?

Implement a zero-downtime rollout script for our Docker Compose deployment.
```

### [ ] 15. Structure your agent team with PM, Engineer, and QA roles

Create `.claude/agents/` with three specialized roles (`pm.md`, `software-engineer.md`, `qa-engineer.md`) and reference them in `AGENTS.md`:

```text
Set up a PM, software-engineer, and qa-engineer workflow in AGENTS.md and .claude/agents/:
- PM grooms each task with requirements, out-of-scope items, and testable acceptance criteria.
- Software engineer implements the task in an isolated git worktree (`git worktree add ../wt/<slug> -b task/<slug>`).
- QA engineer verifies every acceptance criterion in a fresh session and returns ACCEPT or REJECT.
```

### [ ] 16. Run parallel tasks in separate git worktrees

Once the team roles are in place, give the coordinator independent tasks and let it spawn one worktree and one PM -> Engineer -> QA pipeline per task, rebasing and merging only after QA accepts and CI passes.
