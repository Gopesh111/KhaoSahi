from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    """
    Application configuration settings.
    Automatically reads from the .env file in the root directory.
    """
    APP_NAME: str = "KhaoSahi Risk Intelligence API"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    API_PREFIX: str = "/api/v1"

    # AI Model Keys (Set as optional so the app doesn't crash if empty during mock phase)
    GEMINI_API_KEY: Optional[str] = None
    GROQ_API_KEY: Optional[str] = None

    # Database Paths
    FAISS_INDEX_PATH: str = "./data/fssai_index.faiss"
    
    # Logging/Alerts
    DISCORD_WEBHOOK_URL: Optional[str] = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

# Global settings instance to be imported across the app
settings = Settings()
