# Soccer Data Project

A Python-based data engineering project to ingest and explore soccer statistics from the [API-Sports Football API](https://www.api-football.com/).

## What it does

Connects to the API-Sports v3 football API to pull soccer data — leagues, teams, fixtures, and player stats — and lays the groundwork for storage and analysis.

## Stack

| Tool | Purpose |
|---|---|
| Python 3.12 | Core language |
| httpx | HTTP client for API calls |
| Pydantic | Response validation and modeling |
| python-dotenv | Local environment variable loading |
| pytest | Testing |
| ruff | Linting and formatting |
| mypy | Static type checking |

## Project layout

```
src/soccer_data/
├── client.py       # SoccerDataClient — wraps API-Sports HTTP calls
└── models.py       # Pydantic models for API responses
tests/
└── test_client.py
```

## Setup

1. Install dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

2. Copy `.env.example` to `.env` and add your API key:
   ```bash
   cp .env.example .env
   ```

3. Run tests:
   ```bash
   pytest
   ```

## Usage

```python
import os
from dotenv import load_dotenv
from soccer_data.client import SoccerDataClient

load_dotenv()

with SoccerDataClient(api_key=os.environ["API_SPORTS_KEY"]) as client:
    leagues = client.get_leagues()
    print(f"{leagues.results} leagues available")
```

## API source

[API-Sports Football API v3](https://www.api-football.com/) — free tier, 100 requests/day.
Authentication via `x-apisports-key` header.
