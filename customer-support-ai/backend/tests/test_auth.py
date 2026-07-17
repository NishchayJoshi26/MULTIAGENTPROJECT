from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_register_returns_tokens() -> None:
    response = client.post(
        "/auth/register",
        json={"name": "Test User", "email": "test@example.com", "password": "Password123"},
    )
    assert response.status_code == 201
    payload = response.json()
    assert payload[0]["email"] == "test@example.com"
    assert payload[1]["access_token"]


def test_login_returns_tokens() -> None:
    response = client.post(
        "/auth/login",
        json={"email": "test@example.com", "password": "Password123"},
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload[1]["access_token"]


def test_me_requires_auth() -> None:
    response = client.get("/auth/me")
    assert response.status_code == 401
