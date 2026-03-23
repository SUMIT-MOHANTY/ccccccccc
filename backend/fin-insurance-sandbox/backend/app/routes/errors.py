from fastapi import APIRouter, HTTPException
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/test-error")
async def trigger_error():
    """Test endpoint to verify error handling"""
    try:
        # Simulate db error
        raise ValueError("Database connection failed")
    except Exception as e:
        logger.error(f"Error triggered: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "component": "error-handler"}
