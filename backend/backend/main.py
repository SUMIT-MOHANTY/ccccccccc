from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def create_app() -> FastAPI:
    app = FastAPI(
        title="Insurer Dashboard API",
        version="1.0.0",
        docs_url="/docs",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/health")
    async def health_check():
        return {"status": "healthy"}

    @app.post("/api/policies")
    async def create_policy(policy: dict):
        return {"policy": policy, "status": "created"}

    @app.get("/api/policies")
    async def list_policies():
        return {"policies": []}

    return app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:create_app", host="0.0.0.0", port=8000, reload=True)
