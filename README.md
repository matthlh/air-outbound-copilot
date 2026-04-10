# Air Outbound Copilot

Backend-first GTM workflow prototype that turns scored account signals into persona-aware account briefs, pain hypotheses, and outreach openers.

Built as a companion project to **Air-Fit Engine**, which identifies and scores likely high-fit accounts for Air.

## Purpose

This project focuses on the "last mile" of GTM engineering:
- turning account research into actionable outbound context
- generating persona-aware messaging
- packaging results for workflow automation

## What it does

Given an account input with scored signals, the system:
1. infers the most likely target persona
2. identifies the top pain hypothesis
3. generates a concise account brief
4. creates 2 to 3 outbound opener variants
5. packages the result into a workflow payload for Slack, email, or export

## MVP Scope

- backend-first only
- no dashboard required
- structured JSON outputs
- n8n workflow handoff
- provider-wrapped LLM integration

## Status

- [x] Scaffold complete
- [x] Input/output schemas (`app/schemas.py`)
- [ ] Persona logic (stub only — real logic in `app/llm/persona.py`)
- [ ] Outreach generation (stub only — real logic in `app/llm/openers.py`)
- [x] Workflow payload schema + formatter (`app/services/workflow_payload.py`)
- [x] POST /generate route (deterministic stub)
- [ ] Real tests (lightweight tests in place; LLM integration tests pending)

## Example output

```json
{
  "company": "figma.com",
  "persona": "Creative Director",
  "pain_hypothesis": "Version control and cross-functional review friction",
  "reason_summary": "High creative workflow complexity with strong design collaboration signals.",
  "outreach_openers": [
    "Saw that your team is scaling design collaboration across multiple stakeholders...",
    "Noticed signs of heavy creative workflow coordination and review complexity..."
  ],
  "next_best_action": "Send creative-ops-focused opener to Brand Operations lead"
}
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Run

```bash
# start the API server
uvicorn app.main:app --reload

# run the local demo loop (no server required)
python scripts/run_local_demo.py

# run tests
pytest
```

## License

MIT
