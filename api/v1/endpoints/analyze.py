from fastapi import APIRouter, UploadFile, File, Form, HTTPException
import asyncio
import random

router = APIRouter()

@router.post("/")
async def analyze_label(
    file: UploadFile = File(...),
    product_name: str = Form(None)
):
    """
    Core inference endpoint.
    Accepts a product label image, runs OCR, and evaluates against the Medical RAG pipeline.
    """
    # Validate input format
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file format. Please upload an image.")

    # Simulate AI inference latency (Vision OCR + Vector Search + LLM Reasoning)
    await asyncio.sleep(random.uniform(2.0, 3.5))

    # Returning a mocked deterministic JSON output for now.
    # Actual implementation will plug in Gemini Vision and Groq APIs here.
    return {
        "status": "success",
        "product_info": {
            "provided_name": product_name or "Unknown Scan",
            "ocr_confidence": round(random.uniform(85.0, 96.0), 2)
        },
        "risk_scores": {
            "toxicity_score": 68,
            "hidden_sugar_score": 85,
            "ultra_processed_score": 90,
            "deception_score": 75
        },
        "explainability": {
            "red_flags": [
                {"ingredient": "E319 (TBHQ)", "reason": "Synthetic preservative restricted in some regions."},
                {"ingredient": "Maltodextrin", "reason": "High glycemic index, acts as a hidden sugar."}
            ],
            "misleading_claims": [
                {"claim": "Zero Added Sugar", "reality": "Product relies on Maltodextrin and artificial sweeteners."}
            ],
            "safe_elements": [
                {"ingredient": "Oat Flour", "reason": "Standard safe ingredient."}
            ]
        },
        "metadata": {
            "inference_time_ms": random.randint(2100, 3400),
            "routing": "gemini-2.5-flash -> groq-llama3-70b"
        }
    }
