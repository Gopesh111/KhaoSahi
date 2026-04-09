from fastapi import FastAPI
from fastapi.middleware.cors import HTTPMiddleware

# Initialize the FastAPI application
app = FastAPI(
    title="KhaoSahi API",
    description="Backend for Multimodal Food Label Intelligence System",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

# CORS configuration to allow frontend clients to interact with the API
app.add_middleware(
    HTTPMiddleware,
    allow_origins=["*"],  # For production, this should be restricted to specific domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Core API Routes
# The router will be imported and mounted here once the api module is initialized
from api.v1.router import api_router 
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    """
    Root endpoint verifying the service is online.
    """
    return {
        "status": "online",
        "service": "KhaoSahi Risk Intelligence Engine",
        "message": "API is running. Visit /api/docs for interactive documentation."
    }

@app.get("/health")
async def health_check():
    """
    Basic system health check for load balancers.
    """
    return {"status": "healthy", "version": "1.0.0"}

if __name__ == "__main__":
    import uvicorn
    # Entry point for running the server locally
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
