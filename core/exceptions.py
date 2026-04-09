from fastapi import Request
from fastapi.responses import JSONResponse

# Base Exception Class
class KhaoSahiException(Exception):
    """Base exception for all custom errors in the KhaoSahi system."""
    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code

# Specific Edge-Case Exceptions
class VisionProcessingError(KhaoSahiException):
    """Raised when the OCR confidence is too low or image is too blurry (Edge Case 1)."""
    def __init__(self, message: str = "Image is too blurry. Please retake the photo."):
        super().__init__(message=message, status_code=422)

class NormalizationError(KhaoSahiException):
    """Raised when an ingredient cannot be mapped or understood (Edge Case 5/6)."""
    def __init__(self, message: str = "Could not normalize ingredient list. Limited data available."):
        super().__init__(message=message, status_code=400)

class RAGRetrievalError(KhaoSahiException):
    """Raised when the FAISS DB fails to load or return context."""
    def __init__(self, message: str = "Knowledge base retrieval failed. Falling back to lightweight inference."):
        super().__init__(message=message, status_code=503)

# Global Exception Handler for FastAPI
async def khaosahi_exception_handler(request: Request, exc: KhaoSahiException):
    """
    Catches any custom KhaoSahiException and formats it into a clean JSON response.
    Prevents the server from crashing and gives clear feedback to the frontend.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": True,
            "type": exc.__class__.__name__,
            "message": exc.message,
            "path": request.url.path
        }
    )
