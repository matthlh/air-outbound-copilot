"""
Workflow payload formatting.

Converts an OutboundResult into a WorkflowPayload for delivery to n8n, Slack, or export.
Webhook sending is not implemented here — this module only builds the typed payload.
"""

from app.schemas import AccountInput, OutboundResult, WorkflowPayload


def build_workflow_payload(result: OutboundResult, account: AccountInput) -> WorkflowPayload:
    """Convert an OutboundResult into a WorkflowPayload.

    Pulls fit_score and confidence from the original AccountInput so the delivery
    payload includes input context without coupling OutboundResult to it.
    """
    return WorkflowPayload(
        company=result.company,
        persona=result.persona,
        pain_hypothesis=result.pain_hypothesis,
        account_brief=result.account_brief,
        outreach_openers=result.outreach_openers,
        next_best_action=result.next_best_action,
        fit_score=account.fit_score,
        confidence=account.confidence,
    )
