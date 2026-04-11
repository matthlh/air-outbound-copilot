from fastapi import APIRouter
from app.schemas import AccountInput, OutboundResult
from app.services.account_brief import generate_account_brief

router = APIRouter()


@router.post("/generate", response_model=OutboundResult)
def generate(account: AccountInput) -> OutboundResult:
    return generate_account_brief(account)
