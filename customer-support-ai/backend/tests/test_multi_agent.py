from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_agent_router_returns_selected_workflow() -> None:
    response = client.post(
        "/agents/route",
        json={"query": "I need help with my billing charge and a printer issue"},
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["intent"] == "billing+technical"
    assert payload["selected_agents"]
    assert payload["workflow"][0]["agent"] == "intent_detection"


def test_agent_workflow_summarizes_mock_responses() -> None:
    response = client.post(
        "/agents/route",
        json={"query": "Where can I find the product manual?"},
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["final_response"]
    assert "product" in payload["final_response"].lower() or "faq" in payload["final_response"].lower()
