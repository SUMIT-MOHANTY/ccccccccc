import pytest
from backend.app.models.models import Configuration

class TestConfiguration:
    """Test cases for Configuration model"""

    def test_valid_configuration(self):
        """Test creating a valid configuration"""
        config = Configuration(name="test_name", value="test_value")
        assert config.name == "test_name"
        assert config.value == "test_value"

    def test_empty_name_raises_error(self):
        """Test that empty name raises validation error"""
        with pytest.raises(ValueError):
            Configuration(name="", value="some_value")

    def test_whitespace_name_raises_error(self):
        """Test that whitespace-only name raises validation error"""
        with pytest.raises(ValueError):
            Configuration(name="   ", value="some_value")

    def test_empty_value_raises_error(self):
        """Test that empty value raises validation error"""
        with pytest.raises(ValueError):
            Configuration(name="valid_name", value="")

    def test_whitespace_value_raises_error(self):
        """Test that whitespace-only value raises validation error"""
        with pytest.raises(ValueError):
            Configuration(name="valid_name", value="   ")
