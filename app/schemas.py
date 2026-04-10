from pydantic import BaseModel
from typing import Literal


class EvidenceItem(BaseModel):
    source: str
    snippet: str


class AccountInput(BaseModel):
    domain: str
    fit_score: int
    confidence: Literal["low", "medium", "high"]
    persona_guess: str | None = None
    signals: list[str]
    reason_summary: str
    evidence: list[EvidenceItem]


class OutboundResult(BaseModel):
    company: str
    persona: str
    pain_hypothesis: str
    reason_summary: str
    account_brief: str
    outreach_openers: list[str]
    next_best_action: str
