from fastapi import FastAPI
from fastapi.middleware.cors import HTTPMiddleware


# from api.v1.router import api_router 
# from core.config import settings

app = FastAPI(
    title="KhaoSahi API",
    description="Backend for Multimodal Food Label Intelligence System",
    version="1.0.0",
    docs_url="/api/docs", # Swagger UI
    redoc_url="/api/redoc",
)

# CORS Middleware to allow frontend connection (e.g., Streamlit or React)
app.add_middleware(
    HTTPMiddleware,
    allow_origins=["*"], # In production, restrict this to specific domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the main API router
# app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {
        "status": "online",
        "service": "KhaoSahi Risk Intelligence Engine",
        "message": "Welcome to the API. Visit /api/docs for documentation."
    }

@app.get("/health")
async def health_check():
    """
    Basic health check endpoint for deployment monitoring.
    """
    return {"status": "healthy", "version": "1.0.0"}

if __name__ == "__main__":
    import uvicorn
    # Run the server locally
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
