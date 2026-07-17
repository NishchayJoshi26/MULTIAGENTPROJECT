from functools import lru_cache
from typing import List
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "TechMart Support AI"
    app_env: str = "development"
    debug: bool = True
    jwt_secret: str = "replace-with-a-secure-secret"
    jwt_refresh_secret: str = "replace-with-a-secure-refresh-secret"
    gemini_api_key: str = ""
    mongodb_uri: str = "mongodb://localhost:27017"
    mongodb_db_name: str = "customer_support_ai"
    allowed_origins: List[str] = ["http://localhost:3000"]
    log_level: str = "INFO"
    rate_limit_per_minute: int = 60

    class Config:
        env_file = ".env"
        extra = "ignore"


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
