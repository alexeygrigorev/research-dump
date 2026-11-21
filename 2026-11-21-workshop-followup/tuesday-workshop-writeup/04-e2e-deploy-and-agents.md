# Step 4: E2E Tests, Deploy, and Agent Roles

Once the app runs in Docker Compose, we verify the main user flow with a browser test. Then we automate deployment and structure our coding agents so they check each other's work.

## Add a Playwright end-to-end test

Write one Playwright test in `e2e/` that spins up a throw-away Compose stack on isolated ports (18000 and 15432). It signs in as `anna@example.com`, adds a restaurant, reloads the page, and verifies the record stays in Postgres.

```bash
make e2e
```

## Deploy to a VPS with CI/CD and zero-downtime rollout

For a single-VM deployment on Hetzner Cloud, use `deploy/docker-compose.prod.yml` behind Caddy for automatic HTTPS, and disable demo seed data in production with `WSWE_SEED_DEMO_DATA=false`.

In `.github/workflows/ci-cd.yml`, run the test suites first, then build the Docker image once. Run the Playwright e2e test against that image and deploy the exact tested image. Add a zero-downtime rollout script (`deploy/rollout.sh`) so live users don't hit connection errors during updates.

## Structure PM, engineer, and QA agent roles

To keep quality high as the backlog grows, split agent work into three roles under `.claude/agents/` and reference them in `AGENTS.md`:

- `pm` (`pm.md`): grooms each request into requirements, out-of-scope items, and testable acceptance criteria. Never writes code.
- `software-engineer` (`software-engineer.md`): implements the task in an isolated git worktree (`git worktree add ../wt/<slug> -b task/<slug>`).
- `qa-engineer` (`qa-engineer.md`): runs every `Verify:` step in a fresh session and returns `ACCEPT` or `REJECT`.

The coordinator only rebases and merges to `main` after QA accepts and CI passes.
