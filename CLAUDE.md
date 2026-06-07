# Soccer Data Project — Claude Guide

This file gives Claude Code the context it needs to work productively in this repo.
Keep it short. Anything that grows large belongs in a dedicated doc under `.claude/`.

## Project overview

Python project to ingest soccer statistics from the API-Sports Football API (v3).
Current phase: building and expanding the API client.

Longer-term scope: ingestion → storage → transformation → analytics, but we are
not there yet. Add layers only when the need is real.

## API

- **Provider:** API-Sports — `https://v3.football.api-sports.io`
- **Auth:** custom header `x-apisports-key: <key>`
- **Free tier:** 100 requests/day
- **Key env var:** `API_SPORTS_KEY` (in `.env`, never committed)
- **Docs:** https://www.api-football.com/documentation-v3

Endpoints implemented so far:
- `GET /leagues` → `LeaguesResponse`

## Repository layout

```
.
├── CLAUDE.md
├── README.md
├── pyproject.toml          # deps + tool config (ruff, mypy, pytest)
├── .env.example            # documents required env vars (never commit .env)
├── .gitignore
├── src/
│   └── soccer_data/
│       ├── client.py       # SoccerDataClient — one method per endpoint
│       └── models.py       # Pydantic models matching API response shapes
├── tests/
│   └── test_client.py
└── .claude/
    ├── skills/
    └── commands/
```

## Working conventions

- One method per endpoint in `client.py`. Keep each method small: call, raise_for_status, validate.
- Models in `models.py` mirror the exact API response shape. Use `| None` for fields the API documents as optional.
- Never commit `.env`. Secrets go there; `.env.example` documents the required keys.
- Free tier is 100 req/day — avoid loops that hit the API repeatedly during development.
- `pip install -e ".[dev]"` to install all dependencies. `uv` is preferred when available.
- Run tests with `pytest` from the project root.

## How to extend Claude's behavior here

- **Skills** → `.claude/skills/<skill-name>/SKILL.md`
- **Commands** → `.claude/commands/<name>.md` — callable as `/<name>`

Update the "Endpoints implemented" list above each time a new endpoint is added.
