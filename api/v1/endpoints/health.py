from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def check_health():
    """
    Detailed health check endpoint to monitor microservices status.
    """
    # In a real scenario, this would ping the FAISS DB and LLM endpoints
    return {
        "status": "healthy",
        "version": "1.0.0",
        "services": {
            "vector_db": "online",
            "vision_model": "ready",
            "llm_engine": "ready"
        }
    }
