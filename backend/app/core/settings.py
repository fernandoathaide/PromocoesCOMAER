"""
Configurações globais da aplicação.

Todas as configurações são carregadas automaticamente
do arquivo .env utilizando Pydantic Settings.
"""

from functools import lru_cache

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configurações da aplicação."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # ==========================================================
    # Aplicação
    # ==========================================================

    APP_NAME: str = "PromocoesCOMAER"

    APP_VERSION: str = "0.1.0"

    APP_ENV: str = "development"

    DEBUG: bool = True

    # ==========================================================
    # API
    # ==========================================================

    API_HOST: str = "0.0.0.0"

    API_PORT: int = 8000

    # ==========================================================
    # PostgreSQL
    # ==========================================================

    POSTGRES_HOST: str

    POSTGRES_PORT: int

    POSTGRES_DATABASE: str

    POSTGRES_USER: str

    POSTGRES_PASSWORD: str

    # ==========================================================
    # Oracle
    # ==========================================================

    ORACLE_HOST: str = ""

    ORACLE_PORT: int = 1521

    ORACLE_SERVICE: str = ""

    ORACLE_USER: str = ""

    ORACLE_PASSWORD: str = ""


@lru_cache
def get_settings() -> Settings:
    """Retorna uma instância singleton das configurações."""
    return Settings()


settings = get_settings()


@computed_field
@property
def postgres_url(self) -> str:
    return (
        "postgresql+psycopg2://"
        f"{self.POSTGRES_USER}:"
        f"{self.POSTGRES_PASSWORD}@"
        f"{self.POSTGRES_HOST}:"
        f"{self.POSTGRES_PORT}/"
        f"{self.POSTGRES_DATABASE}"
    )


@computed_field
@property
def oracle_url(self) -> str:
    return (
        "oracle+oracledb://"
        f"{self.ORACLE_USER}:"
        f"{self.ORACLE_PASSWORD}@"
        f"{self.ORACLE_HOST}:"
        f"{self.ORACLE_PORT}/"
        f"?service_name={self.ORACLE_SERVICE}"
    )
