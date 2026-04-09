from pydantic import BaseModel, Field
from typing import List, Optional

# --- Sub-models for Explainability ---
class RedFlagItem(BaseModel):
    ingredient: str = Field(..., description="The name of the harmful ingredient identified.")
    reason: str = Field(..., description="Medical or FSSAI reason for flagging.")

class MisleadingClaimItem(BaseModel):
    claim: str = Field(..., description="The marketing claim made on the packet.")
    reality: str = Field(..., description="The actual truth based on the ingredient list.")

class SafeElementItem(BaseModel):
    ingredient: str = Field(..., description="Ingredient that is safe to consume.")
    reason: str = Field(..., description="Why it is considered safe.")

class ExplainabilityData(BaseModel):
    red_flags: List[RedFlagItem]
    misleading_claims: List[MisleadingClaimItem]
    safe_elements: List[SafeElementItem]

# --- Sub-models for Scores & Metadata ---
class RiskScores(BaseModel):
    toxicity_score: int = Field(..., ge=0, le=100, description="0 is safe, 100 is highly toxic.")
    hidden_sugar_score: int = Field(..., ge=0, le=100)
    ultra_processed_score: int = Field(..., ge=0, le=100)
    deception_score: int = Field(..., ge=0, le=100, description="Mismatch between marketing claims and actual ingredients.")

class ProductInfo(BaseModel):
    provided_name: str
    ocr_confidence: float = Field(..., ge=0.0, le=100.0)

class AnalysisMetadata(BaseModel):
    inference_time_ms: int
    routing: str = Field(..., description="The AI pipeline route taken.")

# --- Master Response Model ---
class AnalysisResponse(BaseModel):
    """
    Standardized response payload for the Risk Intelligence Engine.
    """
    status: str = Field(default="success")
    product_info: ProductInfo
    risk_scores: RiskScores
    explainability: ExplainabilityData
    metadata: AnalysisMetadata
