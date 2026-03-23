from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from backend.app.routes import api_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Bank Dashboard API",
    description="API for managing bank accounts and transactions",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router, prefix="/api")

@app.get("/")
async def health_check():
    return {"status": "healthy", "service": "Bank Dashboard API"}

@app.get("/health")
async def health():
    return {"status": "ok"}
