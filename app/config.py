from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    anthropic_api_key: str
    model: str = "claude-haiku-5-5"
    max_tokens: int = 400
    allowed_origins: list[str] = ["http://localhost:3000"]
    # Per-IP limit, because this public endpoint spends your money.
    rate_limit_per_minute: int = 8


settings = Settings()
