from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

SAMPLE_INPUT = {
    "domain": "figma.com",
    "fit_score": 78,
    "confidence": "high",
    "persona_guess": "Brand Operations Lead",
    "signals": ["brand operations", "creative workflow"],
    "reason_summary": "Strong design collaboration signals.",
    "evidence": [{"source": "homepage", "snippet": "Figma helps teams design and collaborate."}],
}


def test_healthcheck() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_generate_returns_200() -> None:
    response = client.post("/generate", json=SAMPLE_INPUT)
    assert response.status_code == 200


def test_generate_response_shape() -> None:
    response = client.post("/generate", json=SAMPLE_INPUT)
    data = response.json()
    assert data["company"] == "figma.com"
    assert data["persona"] == "Brand Operations Lead"
    assert isinstance(data["outreach_openers"], list)
    assert len(data["outreach_openers"]) > 0
    assert "pain_hypothesis" in data
    assert "account_brief" in data
    assert "next_best_action" in data


def test_generate_rejects_invalid_confidence() -> None:
    bad_input = {**SAMPLE_INPUT, "confidence": "very_high"}
    response = client.post("/generate", json=bad_input)
    assert response.status_code == 422
