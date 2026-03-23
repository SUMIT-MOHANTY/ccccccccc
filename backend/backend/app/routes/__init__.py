from fastapi import APIRouter
from . import accounts

api_router = APIRouter()

# Include all route modules
api_router.include_router(accounts.router, prefix="/accounts", tags=["accounts"])
