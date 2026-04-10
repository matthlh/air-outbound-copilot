"""
Account brief orchestration.

Derives a brief and outreach openers from account signals.
Currently deterministic stub logic — real generation will go through app/llm/
once the LLM provider is wired in.
"""

from app.schemas import AccountInput, OutboundResult

# Maps signal keywords to plausible pain hypotheses.
# Deterministic facts only — no invented claims.
_SIGNAL_PAIN_MAP: list[tuple[str, str]] = [
    ("brand operations", "Brand workflow coordination and approval overhead"),
    ("creative workflow", "Creative production and review cycle friction"),
    ("design systems", "Maintaining design system consistency across growing teams"),
    ("cross-functional collaboration", "Cross-functional handoff and stakeholder alignment friction"),
    ("hiring", "Coordinating multi-team hiring workflows at scale"),
    ("engineering", "Developer workflow overhead and deployment coordination"),
    ("product", "Product-to-design-to-engineering handoff gaps"),
]

_DEFAULT_PAIN = "Workflow coordination and collaboration friction"


def _infer_persona(signals: list[str]) -> str:
    lowered = " ".join(signals).lower()
    if "brand" in lowered or "creative" in lowered or "design" in lowered:
        return "Creative Director / Brand Operations Lead"
    if "engineering" in lowered or "developer" in lowered:
        return "Engineering Manager / VP Engineering"
    if "product" in lowered:
        return "VP Product / Product Operations Lead"
    if "hiring" in lowered or "talent" in lowered:
        return "Head of Talent / People Operations Lead"
    return "VP Operations / Chief of Staff"


def _derive_pain_hypothesis(signals: list[str]) -> str:
    lowered_signals = " ".join(signals).lower()
    for keyword, pain in _SIGNAL_PAIN_MAP:
        if keyword in lowered_signals:
            return pain
    return _DEFAULT_PAIN


def _compose_brief(account: AccountInput) -> str:
    signals_str = ", ".join(account.signals[:3])
    return (
        f"{account.domain} shows signals of {signals_str} "
        f"(fit score: {account.fit_score}, confidence: {account.confidence}). "
        f"{account.reason_summary}"
    )


def _compose_openers(account: AccountInput, pain: str) -> list[str]:
    signals = account.signals
    domain = account.domain
    openers = []

    if signals:
        openers.append(
            f"Saw signals of {signals[0]} at {domain} that suggest your team may be "
            f"navigating {pain.lower()}."
        )
    if len(signals) >= 2:
        openers.append(
            f"Your public signals around {signals[0]} and {signals[1]} caught our attention — "
            f"we work with teams managing similar coordination friction."
        )
    openers.append(f"{account.reason_summary} That context is exactly where Air tends to help.")

    return openers


def generate_account_brief(account: AccountInput) -> OutboundResult:
    """Derive a brief and openers from account signals.

    Uses deterministic stub logic. persona_guess from input is passed through
    unchanged; signals drive pain hypothesis and opener templates.
    Real LLM generation will replace _compose_openers and _derive_pain_hypothesis
    via app/llm/ once the provider is wired in.
    """
    persona = account.persona_guess or _infer_persona(account.signals)
    pain_hypothesis = _derive_pain_hypothesis(account.signals)
    account_brief = _compose_brief(account)
    openers = _compose_openers(account, pain_hypothesis)
    next_best_action = f"Send signal-based opener to {persona}"

    return OutboundResult(
        company=account.domain,
        persona=persona,
        pain_hypothesis=pain_hypothesis,
        reason_summary=account.reason_summary,
        account_brief=account_brief,
        outreach_openers=openers,
        next_best_action=next_best_action,
    )
