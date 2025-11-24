from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)
#test physiicans endpoint with filters
def test_get_physicians_filter():
    response = client.get("/physicians?state=NY&specialty=Oncology")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
#test format is as expected
def test_get_messages_filter():
    response = client.get("/messages?physician_id=101")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    for item in data:
        assert "physician_id" in item
        assert item["physician_id"] == 101
        assert "timestamp" in item
        assert "topic" in item
        assert "sentiment" in item
#test physicians endpoint with no filters applied
def test_physicians_no_results():
    response = client.get("/physicians")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
#test messages endpoint with no filters applied
def test_messages_no_results():
    response = client.get("/messages")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
