"""Application Configuration"""

import os
from typing import List
from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Application Settings"""

    app_name: str = os.getenv("APP_NAME", "AI Classroom Monitoring System")
    app_version: str = os.getenv("APP_VERSION", "1.0.0")
    debug: bool = os.getenv("DEBUG", "False").lower() == "true"
    environment: str = os.getenv("ENVIRONMENT", "development")

    database_url: str = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://root:password@localhost:3306/classroom_monitoring",
    )
    database_host: str = os.getenv("DATABASE_HOST", "localhost")
    database_port: int = int(os.getenv("DATABASE_PORT", 3306))
    database_user: str = os.getenv("DATABASE_USER", "root")
    database_password: str = os.getenv("DATABASE_PASSWORD", "password")
    database_name: str = os.getenv("DATABASE_NAME", "classroom_monitoring")

    redis_url: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    redis_host: str = os.getenv("REDIS_HOST", "localhost")
    redis_port: int = int(os.getenv("REDIS_PORT", 6379))

    jwt_secret_key: str = os.getenv(
        "JWT_SECRET_KEY", "your-super-secret-key-change-in-production"
    )
    jwt_algorithm: str = os.getenv("JWT_ALGORITHM", "HS256")
    jwt_expiration_hours: int = int(os.getenv("JWT_EXPIRATION_HOURS", 24))

    allowed_hosts: List[str] = [
        "localhost",
        "127.0.0.1",
        "localhost:3000",
        "localhost:8000",
    ]
    cors_origins: List[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
    ]

    max_upload_size_mb: int = int(os.getenv("MAX_UPLOAD_SIZE_MB", 100))
    upload_folder: str = os.getenv("UPLOAD_FOLDER", "./uploads")

    ai_model_phone: str = os.getenv("AI_MODEL_PHONE", "yolov8n.pt")
    ai_confidence_threshold: float = float(
        os.getenv("AI_CONFIDENCE_THRESHOLD", "0.45")
    )
    ai_max_faces: int = int(os.getenv("AI_MAX_FACES", 10))
    ai_frame_rate: int = int(os.getenv("AI_FRAME_RATE", 30))

    websocket_heartbeat_interval: int = int(
        os.getenv("WEBSOCKET_HEARTBEAT_INTERVAL", 30)
    )
    websocket_timeout: int = int(os.getenv("WEBSOCKET_TIMEOUT", 300))

    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    log_file: str = os.getenv("LOG_FILE", "./logs/app.log")

    class Config:
        env_file = ".env"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    """Get application settings (cached)"""
    return Settings()
