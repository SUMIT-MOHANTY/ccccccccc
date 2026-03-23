import pytest
import asyncio
from typing import Generator
import sys
import os

# Ensure consistent path handling
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

@pytest.fixture
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture
def mock_insurer_data():
    """Mock insurer data for testing."""
    return {
        "id": "test-123",
        "name": "Test Insurer",
        "email": "test@insurer.com",
        "policies_count": 100
    }
