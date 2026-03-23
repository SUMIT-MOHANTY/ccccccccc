import pytest
from backend.app.models import TestConfig, ErrorResponse, SuccessResponse

class TestTestConfig:
    def test_config_creation(self):
        config = TestConfig(name="test-name", value="test-value")
        assert config.name == "test-name"
        assert config.value == "test-value"

    def test_config_validation(self):
        with pytest.raises(ValueError):
            TestConfig(name="", value="invalid")

    def test_config_default_id(self):
        config1 = TestConfig(name="test1")
        config2 = TestConfig(name="test2")
        assert config1.id != config2.id

class TestErrorResponse:
    def test_error_response(self):
        error = ErrorResponse(detail="Test error")
        assert error.detail == "Test error"
        assert error.status == 400

class TestSuccessResponse:
    def test_success_response(self):
        success = SuccessResponse(data={"test": True})
        assert success.success is True
        assert success.data["test"] is True
