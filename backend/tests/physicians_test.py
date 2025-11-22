from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_get_physicians_filter():
    response = client.get("/physicians?state=NY&specialty=Oncology")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
