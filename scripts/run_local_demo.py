"""
Local demo runner.

Loads data/sample_accounts.json, validates each entry with AccountInput,
and prints a deterministic OutboundResult for each. No LLM or server required.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from app.schemas import AccountInput
from app.services.account_brief import generate_account_brief
from app.services.workflow_payload import build_workflow_payload


def main() -> None:
    data_path = Path(__file__).parent.parent / "data" / "sample_accounts.json"
    accounts_raw: list[dict] = json.loads(data_path.read_text())

    for raw in accounts_raw:
        account = AccountInput(**raw)
        result = generate_account_brief(account)
        payload = build_workflow_payload(result, account)

        print(f"\n--- {account.domain} ---")
        print(json.dumps(result.model_dump(), indent=2))
        print("\n--- workflow payload ---")
        print(json.dumps(payload.model_dump(), indent=2))


if __name__ == "__main__":
    main()
