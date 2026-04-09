from fastapi.testclient import TestClient
from main import app
import io

# Initialize test client
client = TestClient(app)

def test_root_endpoint():
    """Test if the main entry point is working."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "online"

def test_health_endpoint():
    """Test the detailed health check."""
    response = client.get("/health")
    assert response.status_code == 200
    assert "services" in response.json()

def test_analyze_endpoint_invalid_file():
    """Test edge case: Uploading a text file instead of an image."""
    # Create a dummy text file
    dummy_file = io.BytesIO(b"this is not an image")
    
    response = client.post(
        "/api/v1/analyze/",
        files={"file": ("test.txt", dummy_file, "text/plain")}
    )
    
    assert response.status_code == 400
    assert "Invalid file format" in response.json()["detail"]
