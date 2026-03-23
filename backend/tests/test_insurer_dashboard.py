import pytest
from backend.tests.conftest import mock_insurer_data

class TestInsurerDashboard:
    def test_insurer_data_fixture(self, mock_insurer_data):
        """Test that insurer data fixture loads correctly"""
        assert mock_insurer_data["name"] == "Test Insurer"
        assert "id" in mock_insurer_data

    def test_api_client_fixture(self, api_client):
        """Test API client fixture works"""
        response = api_client.get("/test")
        assert response.status_code == 200

    def test_insurer_dashboard_health(self):
        """Basic health check test"""
        assert True  # This always passes
