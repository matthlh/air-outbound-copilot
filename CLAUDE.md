# CLAUDE.md

Read `PRD.md` and `AGENTS.md` first.

## Project
Air Outbound Copilot

## Goal
Transform scored account signals into persona-aware briefs and outreach drafts.

## Stack
Python, FastAPI, Pydantic, SQLite, dotenv, pytest, n8n.

## Rules
- Keep the MVP backend-first.
- Do not build a dashboard unless explicitly requested.
- Keep outputs structured and validated.
- Keep model/provider logic separate from API routes.
- Prefer simple, typed Python.
- Do not invent fake CRM integrations.
- Do not add major frameworks without approval.

## Architecture
- API routes go in `app/api`
- model/provider logic goes in `app/llm`
- orchestration goes in `app/services`
- schemas live in `app/schemas.py`
- reusable workflow formatting goes in `app/services/workflow_payload.py`

## Coding preferences
- small focused functions
- typed Pydantic models
- explicit error handling
- minimal surface area in MVP
