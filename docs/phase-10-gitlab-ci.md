# Phase 10 — GitLab CI: Basic test pipeline

What this is
- A minimal GitLab CI pipeline that runs the Python test suite on every push / merge request.

Why `.gitlab-ci.yml` exists
- GitLab reads this file to know how to run CI jobs for the repository.

Who reads this file
- CI systems (GitLab), reviewers, and engineers during interviews or code reviews.

What the pipeline currently does
- Uses `python:3.13-slim` image.
- Starts a Postgres service (`postgres:16-alpine`).
- Installs Python dependencies from `requirements.txt`.
- Runs Alembic migrations (`alembic upgrade head`) against the Postgres service.
- Runs `pytest` to execute the test suite.

Why this is useful before image build/deployment
- Validates application behavior (unit + integration) early.
- Catches regressions before building images or deploying infrastructure.

How to explain this in an interview
- Describe the pipeline as a simple CI gate: it provides an isolated, reproducible environment
  where dependencies and a real Postgres service are available so migrations can run and tests
  execute reliably. Emphasize running migrations in CI to keep schema management in Alembic
  (no `Base.metadata.create_all()`), and note that this stage focuses on fast feedback before
  adding image build or GitOps deployment stages.
