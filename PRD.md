# Product Requirements Document

## Project
Air Outbound Copilot

## Goal
Turn scored account signals into persona-aware outbound actions for a GTM team.

## User
Primary:
- GTM engineer
- SDR / AE
- RevOps / sales ops

Secondary:
- recruiter / hiring manager reviewing the project

## Problem
Scored accounts are useful, but GTM teams still need to know:
- who to target
- what pain to lead with
- what to say first
- how to route the result into a usable workflow

## Input
A high-fit account from Air-Fit Engine, including:
- company domain
- fit score
- matched signals
- reason summary
- supporting evidence

## Output
- persona guess
- pain hypothesis
- account brief
- 2 to 3 outreach opener variants
- next best action
- workflow payload for Slack/email/export

## MVP
- backend-first
- one account in
- structured JSON out
- provider-wrapped LLM generation
- FastAPI endpoints
- n8n workflow payload

## Non-goals
- dashboard
- CRM integration
- production hosting
- auth
- multi-user support

## Success criteria
- output is structured and explainable
- persona and pain hypothesis are plausible
- generated openers are differentiated and usable
- payload can be consumed by n8n cleanly
