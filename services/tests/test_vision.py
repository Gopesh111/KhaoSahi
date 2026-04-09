import pytest
from fastapi import UploadFile
import io
from services.vision_ocr.gemini_vision import GeminiVisionService
from core.exceptions import VisionProcessingError

# Use pytest-asyncio for async function testing
@pytest.mark.asyncio
async def test_low_quality_image_rejection():
    """
    Tests Edge Case 1: The system should reject files that are too small (blurry/low res).
    """
    vision_service = GeminiVisionService()
    
    # Create a dummy file that is smaller than 10KB
    small_file_content = b"fake image bytes" * 10
    file_obj = io.BytesIO(small_file_content)
    upload_file = UploadFile(filename="blurry_pic.jpg", file=file_obj)
    
    # We expect our custom VisionProcessingError to be raised
    with pytest.raises(VisionProcessingError) as exc_info:
        await vision_service.extract_label_data(upload_file)
    
    assert "Image resolution too low" in str(exc_info.value)
