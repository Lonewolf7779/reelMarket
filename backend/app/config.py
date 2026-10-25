from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "reelMarket API"
    database_url: str = "sqlite:///./reelmarket.db"
    api_prefix: str = "/api/v1"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
