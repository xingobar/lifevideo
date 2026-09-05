from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    APP_ENV: str = "development"
    APP_DEBUG: bool = True
    SECRET_KEY: str = "change-me-in-production"

    DATABASE_URL: str = (
        "postgresql+psycopg://lifevideo:lifevideo_pass@postgres:5432/lifevideo_db"
    )
    REDIS_URL: str = "redis://redis:6379/0"

    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int


settings = Settings()
