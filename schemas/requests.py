from pydantic import BaseModel, Field
from typing import Optional

class TextAnalysisRequest(BaseModel):
    """
    Payload for analyzing ingredients via manual text input instead of an image.
    """
    product_name: Optional[str] = Field(default=None, max_length=100)
    ingredients_text: str = Field(..., min_length=5, description="Comma-separated list of ingredients.")
    claims_text: Optional[str] = Field(default=None, description="Marketing claims written on the package.")

class FeedbackRequest(BaseModel):
    """
    Payload for capturing user feedback on AI predictions.
    """
    analysis_id: str
    is_accurate: bool
    user_comment: Optional[str] = Field(default=None, max_length=500)
