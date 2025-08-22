import os
from pydantic import BaseModel
from typing import List

class Settings(BaseModel):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+psycopg2://attack_user:attack_password@db:5432/attack_vector")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "15"))
    REFRESH_TOKEN_EXPIRE_DAYS: int = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", "7"))
    JWT_SECRET: str = os.getenv("JWT_SECRET", "change-this")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    CORS_ORIGINS: List[str] = os.getenv("CORS_ORIGINS", "http://localhost,http://localhost:3000").split(",")
    ADMIN_EMAIL: str = os.getenv("ADMIN_EMAIL", "admin@example.com")
    ADMIN_PASSWORD: str = os.getenv("ADMIN_PASSWORD", "ChangeMe!123")

settings = Settings()
