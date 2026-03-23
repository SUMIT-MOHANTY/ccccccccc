import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import pytest
from fastapi.testclient import TestClient

def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_policy_creation(client, sample_policy_data):
    response = client.post("/api/policies", json=sample_policy_data)
    assert response.status_code == 201
    data = response.json()
    assert data["policy"]["policy_number"] == sample_policy_data["policy_number"]

def test_policy_listing(client):
    response = client.get("/api/policies")
    assert response.status_code == 200
    assert isinstance(response.json()["policies"], list)
