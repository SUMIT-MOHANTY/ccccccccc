import pytest
from models import TestConfig, BankTransaction, BankDashboard
import uuid

class TestTestConfig:
    """Test cases for TestConfig model"""

    def test_valid_config(self):
        config = TestConfig(name="test_config")
        assert config.name == "test_config"
        assert config.environment == "test"

    def test_valid_config_with_email(self):
        config = TestConfig(
            name="test",
            email="test@example.com",
            max_transactions=500
        )
        assert config.email == "test@example.com"
        assert config.max_transactions == 500

    def test_invalid_email(self):
        with pytest.raises(ValueError):
            TestConfig(name="test", email="invalid-email")

    def test_invalid_max_transactions(self):
        with pytest.raises(ValueError):
            TestConfig(name="test", max_transactions=0)
        with pytest.raises(ValueError):
            TestConfig(name="test", max_transactions=20000)

class TestBankTransaction:
    """Test cases for BankTransaction model"""

    def test_valid_transaction(self):
        tx = BankTransaction(transaction_id="TX123", amount=100.50)
        assert tx.transaction_id == "TX123"
        assert tx.amount == 100.50
        assert tx.category == "general"

    def test_invalid_transaction_id(self):
        with pytest.raises(ValueError):
            BankTransaction(transaction_id="", amount=50.0)

    def test_negative_amount(self):
        with pytest.raises(ValueError):
            BankTransaction(transaction_id="TX456", amount=-10.0)

class TestBankDashboard:
    """Test cases for BankDashboard model"""

    def test_valid_dashboard(self):
        dashboard = BankDashboard(
            user_id="user123",
            balance=1000.0
        )
        assert dashboard.user_id == "user123"
        assert dashboard.balance == 1000.0
        assert len(dashboard.transactions) == 0

    def test_invalid_user_id(self):
        with pytest.raises(ValueError):
            BankDashboard(user_id="", balance=1000.0)

    def test_with_transactions(self):
        tx1 = BankTransaction(transaction_id="TX1", amount=50.0)
        tx2 = BankTransaction(transaction_id="TX2", amount=-25.5)
        dashboard = BankDashboard(
            user_id="user456",
            balance=974.5,
            transactions=[tx1, tx2]
        )
        assert len(dashboard.transactions) == 2
        assert dashboard.transactions[0].transaction_id == "TX1"
