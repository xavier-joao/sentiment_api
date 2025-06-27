import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Sentiment API is up and running"}

def test_create_review():
    payload = {
        "customer_name": "John Doe",
        "review_date": "2024-06-27",
        "text": "I love this product!"
    }
    response = client.post("/reviews", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["customer_name"] == "John Doe"
    assert data["review_date"] == "2024-06-27"
    assert data["sentiment"] in ["positive", "neutral", "negative"]
    assert isinstance(data["confidence"], float)

def test_get_all_reviews():
    response = client.get("/reviews")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_review_by_id():
    payload = {
        "customer_name": "Jane Doe",
        "review_date": "2024-06-27",
        "text": "Not bad."
    }
    create_resp = client.post("/reviews", json=payload)
    assert create_resp.status_code == 200
    review_id = create_resp.json()["id"]

    get_resp = client.get(f"/reviews/{review_id}")
    assert get_resp.status_code == 200
    data = get_resp.json()
    assert data["id"] == review_id

def test_get_review_report():
    response = client.get("/reviews/report?start_date=2024-01-01&end_date=2025-01-01")
    print("RESPONSE JSON:", response.json())  
    assert response.status_code == 200
    data = response.json()
    assert "start_date" in data
    assert "end_date" in data
    assert "total_reviews" in data
    assert "summary" in data