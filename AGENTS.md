# Agent Guidance

## Project intent
This project is meant to complement Air-Fit Engine.

Air-Fit Engine answers:
- Which companies are likely good fits for Air?

Air Outbound Copilot answers:
- What should the GTM team do with those accounts?

## Development priorities
1. Strong typed schemas
2. Clean LLM abstraction
3. Explainable persona and pain outputs
4. Workflow-ready payloads
5. Minimal but usable API

## Constraints
- Backend-first MVP
- No dashboard unless explicitly requested
- No production auth
- No unnecessary dependencies
- No ungrounded claims in generated content

## Output philosophy
Generated content should be:
- structured
- concise
- persona-aware
- plausible for B2B SaaS outbound
- clearly separate from deterministic input facts

## Repo hygiene
- keep `main` stable
- use small commits
- avoid placeholder code that pretends to be finished
