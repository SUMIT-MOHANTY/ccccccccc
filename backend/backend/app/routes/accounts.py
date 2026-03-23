from fastapi import APIRouter, HTTPException, Depends
from typing import List
import logging
from backend.app.models.models import BankAccount, Transaction

router = APIRouter()
logger = logging.getLogger(__name__)

# Mock data for testing
MOCK_ACCOUNTS = [
    BankAccount(
        id="acc001",
        user_id="user001",
        account_type="checking",
        balance=5000.0,
        currency="USD"
    ),
    BankAccount(
        id="acc002",
        user_id="user001",
        account_type="savings",
        balance=10000.0,
        currency="USD"
    )
]

MOCK_TRANSACTIONS = [
    Transaction(
        id="txn001",
        account_id="acc001",
        amount=100.0,
        type="credit",
        description="Paycheck deposit"
    ),
    Transaction(
        id="txn002",
        account_id="acc001",
        amount=50.0,
        type="debit",
        description="Grocery shopping"
    )
]

@router.get("/")
async def get_accounts():
    """Get all bank accounts"""
    logger.info("Fetching all accounts")
    return {"accounts": MOCK_ACCOUNTS}

@router.get("/{account_id}")
async def get_account(account_id: str):
    """Get specific account by ID"""
    logger.info(f"Fetching account: {account_id}")
    account = next((acc for acc in MOCK_ACCOUNTS if acc.id == account_id), None)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return {"account": account}

@router.get("/{account_id}/transactions")
async def get_account_transactions(account_id: str):
    """Get transactions for a specific account"""
    logger.info(f"Fetching transactions for account: {account_id}")
    if not any(acc.id == account_id for acc in MOCK_ACCOUNTS):
        raise HTTPException(status_code=404, detail="Account not found")

    transactions = [txn for txn in MOCK_TRANSACTIONS if txn.account_id == account_id]
    return {"transactions": transactions}

@router.post("/")
async def create_account(account: BankAccount):
    """Create a new bank account"""
    logger.info("Creating new account")
    if any(acc.id == account.id for acc in MOCK_ACCOUNTS):
        raise HTTPException(status_code=400, detail="Account ID already exists")
    return {"created": True, "account": account}
