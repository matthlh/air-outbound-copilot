"""Schema validation tests."""

import pytest
from pydantic import ValidationError
from app.schemas import AccountInput, OutboundResult, WorkflowPayload


def test_account_input_valid() -> None:
    account = AccountInput(
        domain="figma.com",
        fit_score=78,
        confidence="high",
        signals=["brand operations", "creative workflow"],
        reason_summary="Strong signals.",
        evidence=[{"source": "homepage", "snippet": "Figma helps teams collaborate."}],
    )
    assert account.domain == "figma.com"
    assert account.persona_guess is None


def test_account_input_persona_guess_optional() -> None:
    account = AccountInput(
        domain="linear.app",
        fit_score=65,
        confidence="medium",
        persona_guess="VP Engineering",
        signals=["engineering", "product"],
        reason_summary="Engineering-heavy signals.",
        evidence=[],
    )
    assert account.persona_guess == "VP Engineering"


def test_account_input_rejects_invalid_confidence() -> None:
    with pytest.raises(ValidationError):
        AccountInput(
            domain="figma.com",
            fit_score=78,
            confidence="very_high",
            signals=[],
            reason_summary="...",
            evidence=[],
        )


def test_outbound_result_valid() -> None:
    result = OutboundResult(
        company="figma.com",
        persona="Creative Director",
        pain_hypothesis="Review friction",
        reason_summary="Strong signals.",
        account_brief="Figma has strong design signals.",
        outreach_openers=["Opener one.", "Opener two."],
        next_best_action="Send opener",
    )
    assert len(result.outreach_openers) == 2


def test_workflow_payload_defaults_source() -> None:
    payload = WorkflowPayload(
        company="figma.com",
        persona="Creative Director",
        pain_hypothesis="Review friction",
        account_brief="Brief.",
        outreach_openers=["Opener."],
        next_best_action="Send opener",
        fit_score=78,
        confidence="high",
    )
    assert payload.source == "air-outbound-copilot"


def test_workflow_payload_rejects_invalid_confidence() -> None:
    with pytest.raises(ValidationError):
        WorkflowPayload(
            company="figma.com",
            persona="Creative Director",
            pain_hypothesis="Review friction",
            account_brief="Brief.",
            outreach_openers=["Opener."],
            next_best_action="Send opener",
            fit_score=78,
            confidence="unknown",
        )
