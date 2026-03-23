import pytest
from backend.app.models.models import BankAccount, Transaction
from datetime import datetime

class TestBankAccount:
    """Test class for BankAccount model"""

    def test_bank_account_creation(self):
        account = BankAccount(
            id="acc123",
            user_id="user456",
            account_type="checking",
            balance=1000.0,
            currency="USD"
        )
        assert account.id == "acc123"
        assert account.balance == 1000.0

    def test_balance_validation(self):
        with pytest.raises(ValueError):
            BankAccount(
                id="acc124",
                user_id="user456",
                account_type="savings",
                balance=-100,
                currency="EUR"
            )

    def test_currency_validation(self):
        with pytest.raises(ValueError):
            BankAccount(
                id="acc125",
                user_id="user456",
                account_type="checking",
                balance=1000,
                currency="invalid"
            )

class TestTransaction:
    """Test class for Transaction model"""

    def test_transaction_creation(self):
        txn = Transaction(
            id="txn789",
            account_id="acc123",
            amount=50.0,
            type="credit",
            description="Test transaction"
        )
        assert txn.id == "txn789"
        assert txn.amount == 50.0

    def test_type_validation(self):
        with pytest.raises(ValueError):
            Transaction(
                id="txn790",
                account_id="acc123",
                amount=50,
                type="invalid",
                description="Test"
            )

    def test_amount_validation(self):
        with pytest.raises(ValueError):
            Transaction(
                id="txn791",
                account_id="acc123",
                amount=0,
                type="credit",
                description="Zero amount"
            )
