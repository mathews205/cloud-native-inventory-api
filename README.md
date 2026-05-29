# Cloud Native Inventory API

A simple FastAPI backend project built step by step for interview learning.

## Run Locally

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up .env file:
```bash
cp .env.example .env
```

3. Run the app:
```bash
uvicorn app.main:app --reload
```

4. Apply Alembic migrations (if needed):
```bash
alembic upgrade head
```

## Run with Docker Compose

1. Build and start the containers:
```bash
docker compose up --build
```

2. Stop the containers:
```bash
docker compose down
```

3. View logs:
```bash
# API logs
docker compose logs api

# PostgreSQL logs
docker compose logs postgres
```

4. Apply Alembic migrations in Docker:
```bash
docker compose exec api alembic upgrade head
```

The API will be available at `http://localhost:8000`
