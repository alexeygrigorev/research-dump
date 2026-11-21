# Step 3: Database and Docker

An in-memory store resets on every restart. Next, we move persistence into SQLAlchemy so the same code works with local SQLite and production PostgreSQL.

## Switch to SQLite and SQLAlchemy

Configure the database URL through an environment variable (`WSWE_DATABASE_URL`). That way, tests, local runs, and containers can each use a different database without code changes.

```text
Replace the in-memory store with a database using SQLite and SQLAlchemy.

Use WSWE_DATABASE_URL to configure which DB the server connects to, and keep it database-agnostic so we can add Postgres later.
```

## Package frontend and backend in one image

A multi-stage `Dockerfile` builds the static frontend with Node (`npm run build:static` into `frontend/dist/client`). It then copies those static files into the Python backend image so FastAPI serves both the API and the SPA on port 8000.

```bash
make docker-build
```

## Add PostgreSQL and Docker Compose

Add `psycopg[binary]` and Alembic migrations to `backend/`, then create `docker-compose.yml` with two services: `db` (PostgreSQL) and the app image.

Start the full stack:

```bash
make up
```

Verify the app responds at `http://localhost:8000` and that new restaurants persist across container restarts. To run the backend locally against the Compose Postgres container during development, run `make db` followed by `make backend-pg`.
