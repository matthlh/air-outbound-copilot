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
    """API response model. Includes internal reasoning fields like reason_summary."""
    company: str
    persona: str
    pain_hypothesis: str
    reason_summary: str
    account_brief: str
    outreach_openers: list[str]
    next_best_action: str


class WorkflowPayload(BaseModel):
    """Delivery model for n8n / Slack / export. Omits internal reasoning fields."""
    source: str = "air-outbound-copilot"
    company: str
    persona: str
    pain_hypothesis: str
    account_brief: str
    outreach_openers: list[str]
    next_best_action: str
    fit_score: int
    confidence: Literal["low", "medium", "high"]
