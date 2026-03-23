from pydantic import BaseModel, field_validator
from typing import Optional
import re

class TestConfig(BaseModel):
    """Test configuration model for bank dashboard"""
    name: str
    email: Optional[str] = None
    max_transactions: int = 1000
    environment: str = "test"

    @field_validator('email')
    @classmethod
    def validate_email(cls, v):
        if v is None:
            return v
        if not re.match(r"[^@]+@[^@]+\.[^@]+", v):
            raise ValueError('Invalid email format')
        return v

    @field_validator('max_transactions')
    @classmethod
    def validate_max_transactions(cls, v):
        if v <= 0 or v > 10000:
            raise ValueError('max_transactions must be between 1 and 10000')
        return v

class BankTransaction(BaseModel):
    """Bank transaction model for dashboard"""
    transaction_id: str
    amount: float
    currency: str = "USD"
    merchant: Optional[str] = None
    category: str = "general"

    @field_validator('transaction_id')
    @classmethod
    def validate_transaction_id(cls, v):
        if not v or len(v) < 3:
            raise ValueError('Transaction ID must be at least 3 characters')
        return v

    @field_validator('amount')
    @classmethod
    def validate_amount(cls, v):
        if v < 0:
            raise ValueError('Amount cannot be negative')
        return round(v, 2)

class BankDashboard(BaseModel):
    """Main bank dashboard model"""
    user_id: str
    balance: float
    currency: str = "USD"
    transactions: list[BankTransaction] = []

    @field_validator('user_id')
    @classmethod
    def validate_user_id(cls, v):
        if not v:
            raise ValueError('User ID is required')
        return v
