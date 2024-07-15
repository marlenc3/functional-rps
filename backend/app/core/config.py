import secrets

from pydantic import (
    computed_field,
)
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_ignore_empty=True, extra="ignore"
    )
    API_V1_STR: str = "/api/v1"

    DOMAIN: str = "localhost"
    ENVIRONMENT: Literal["local", "staging", "production"] = "local"
    GAME_API_KEY: str = secrets.token_urlsafe(32)

    PROJECT_NAME: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_NAME: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str

    @computed_field
    @property
    def postgres_db(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}/{self.POSTGRES_NAME}"


settings = Settings()  # type: ignore
