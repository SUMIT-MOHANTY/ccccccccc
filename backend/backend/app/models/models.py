from pydantic import BaseModel, field_validator, Field
from typing import Optional
from datetime import datetime

class BankAccount(BaseModel):
    id: str
    user_id: str
    account_type: str = Field(..., min_length=1)
    balance: float = Field(..., ge=0)
    currency: str = Field(..., min_length=3, max_length=3)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    @field_validator('balance')
    def validate_balance(cls, v):
        if v < 0:
            raise ValueError('Balance must be non-negative')
        return v

    @field_validator('currency')
    def validate_currency(cls, v):
        if len(v) != 3 or not v.isupper():
            raise ValueError('Currency must be 3 uppercase letters')
        return v

class Transaction(BaseModel):
    id: str
    account_id: str
    amount: float
    type: str = Field(..., pattern='^(credit|debit)$')
    description: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    @field_validator('amount')
    def validate_amount(cls, v):
        if v == 0:
            raise ValueError('Amount cannot be zero')
        return v
