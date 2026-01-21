from fastapi.testclient import TestClient
from app import app

client=TestClient(app)

def test_home_endpoint():
    response=client.get("/")
    assert response.status_code==200
    assert response.json()["status"]=="healthy"
    
def test_positive_sentiment():
    payload={"text": "I absolutely love this amazing project!"}
    response=client.post("/analyze",json=payload)
    assert response.status_code==200
    assert response.json()["label"]=="Positive"
    
def test_negative_sentiment():
    payload={"text": "This is a terrible and bad error."}
    response=client.post("/analyze",json=payload)
    assert response.status_code==200
    assert response.json()["label"]=="Negative"
    
def test_empty_input_validation():
    payload={"text": "   "}
    response=client.post("/analyze",json=payload)
    assert response.status_code==400