from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_run_strategy():
    response = client.get("/run-strategy")

    assert response.status_code == 200

    data = response.json()

    assert "volatility_strategy" in data
    assert "mean_reversion_strategy" in data
    assert "market" in data