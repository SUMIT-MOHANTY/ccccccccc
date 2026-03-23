import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

@pytest.fixture(scope="session")
def app():
    """Create FastAPI test application"""
    from backend.main import create_app
    return create_app()

@pytest.fixture(scope="session")
def client(app):
    """Create test client"""
    return TestClient(app)

@pytest.fixture
def sample_policy_data():
    """Provide sample policy data for testing"""
    return {
        "policy_number": "POL-2024-001",
        "holder_name": "John Doe",
        "premium": 1000.00,
        "coverage_amount": 50000.00,
        "start_date": "2024-01-01",
        "end_date": "2024-12-31"
    }
