from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ai_predict_requires_auth():
    res = client.post("/ai/predict", json={"text": "hello"})
    assert res.status_code in [401, 403]