"""account_brief service tests."""

from app.schemas import AccountInput
from app.services.account_brief import generate_account_brief
from app.services.workflow_payload import build_workflow_payload

SAMPLE_ACCOUNT = AccountInput(
    domain="figma.com",
    fit_score=78,
    confidence="high",
    persona_guess="Brand Operations Lead",
    signals=["brand operations", "creative workflow", "cross-functional collaboration"],
    reason_summary="Strong design collaboration signals.",
    evidence=[{"source": "homepage", "snippet": "Figma helps teams design and collaborate."}],
)


def test_generate_uses_persona_guess() -> None:
    result = generate_account_brief(SAMPLE_ACCOUNT)
    assert result.persona == "Brand Operations Lead"


def test_generate_infers_persona_without_guess() -> None:
    account = SAMPLE_ACCOUNT.model_copy(update={"persona_guess": None})
    result = generate_account_brief(account)
    assert result.persona
    assert "Creative" in result.persona or "Brand" in result.persona


def test_generate_openers_populated() -> None:
    result = generate_account_brief(SAMPLE_ACCOUNT)
    assert isinstance(result.outreach_openers, list)
    assert len(result.outreach_openers) >= 2


def test_generate_company_matches_domain() -> None:
    result = generate_account_brief(SAMPLE_ACCOUNT)
    assert result.company == "figma.com"


def test_generate_reason_summary_passed_through() -> None:
    result = generate_account_brief(SAMPLE_ACCOUNT)
    assert result.reason_summary == SAMPLE_ACCOUNT.reason_summary


def test_build_workflow_payload_shape() -> None:
    result = generate_account_brief(SAMPLE_ACCOUNT)
    payload = build_workflow_payload(result, SAMPLE_ACCOUNT)
    assert payload.company == "figma.com"
    assert payload.fit_score == 78
    assert payload.confidence == "high"
    assert payload.source == "air-outbound-copilot"
    assert "reason_summary" not in payload.model_fields_set
