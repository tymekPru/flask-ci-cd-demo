# flask-ci-cd-demo

A minimal Flask app used to demonstrate a working CI/CD pipeline on GitHub Actions.

## What the pipeline does

On every push and pull request to `main` ([`.github/workflows/ci.yml`](.github/workflows/ci.yml)):

1. **Lint** — `ruff check .`
2. **Tests** — `pytest` (see [`app_test.py`](app_test.py))
3. **Docker build** — builds the image only after lint and tests pass (`needs: test`)

## The app

Two JSON endpoints:

| Endpoint | Response |
|---|---|
| `GET /` | `{"message": "hello from CI/CD", "environment": "<APP_ENV>"}` |
| `GET /health` | `{"status": "ok"}` |

`APP_ENV` defaults to `local` — set it to see the environment reflected in the response.

## Run locally

```bash
pip install -r requirements.txt
python app.py
# -> http://localhost:5123
```

## Run in Docker

```bash
docker build -t flask-ci-cd-demo .
docker run -p 5123:5123 -e APP_ENV=docker flask-ci-cd-demo
```

## Stack

Python 3.13 · Flask · pytest · ruff · Docker · GitHub Actions
