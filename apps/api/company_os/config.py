from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv(override=False)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    app_env: str = "development"
    database_url: str = "sqlite:///./data/company.db"
    jwt_secret: str = ""
    owner_email: str = "owner@local.test"
    owner_password: str = ""
    web_origin: str = "http://localhost:3000"
    mock_enabled: bool = True
    execution_enabled: bool = False
    artifact_root: Path = Path("artifacts")
    repository_root: Path = Path("data/repositories")
    provider_allowed_hosts: str = (
        "api.openai.com,api.anthropic.com,generativelanguage.googleapis.com,api.x.ai,localhost,127.0.0.1"
    )
    research_allowed_hosts: str = "cloud.google.com,lightning.ai,aws.amazon.com,azure.microsoft.com"
    oidc_issuer: str = ""
    oidc_audience: str = ""
    oidc_jwks_url: str = ""
    s3_bucket: str = ""
    s3_endpoint: str = ""
    login_window_seconds: int = Field(ge=10, le=3600, default=60)
    login_account_limit: int = Field(ge=1, le=100, default=10)
    login_source_limit: int = Field(ge=1, le=10000, default=100)
    worker_stale_seconds: int = Field(ge=15, le=600, default=90)

    def validate_startup(self) -> None:
        if len(self.jwt_secret) < 32:
            raise ValueError("JWT_SECRET must have at least 32 characters. Run bootstrap first.")
        if self.app_env == "production" and (self.mock_enabled or not self.oidc_issuer):
            raise ValueError("Production requires OIDC and MOCK_ENABLED=false.")


@lru_cache
def settings() -> Settings:
    return Settings()
