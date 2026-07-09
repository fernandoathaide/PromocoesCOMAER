from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Configurações globais da aplicação.
        Todos os valores são carregados automaticamente
    do arquivo .env.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # -------------------------------------------------
    # Aplicação
    # -------------------------------------------------

    APP_NAME: str = "PromocoesCOMAER"

    APP_VERSION: str = "0.1.0"

    APP_ENV: str = "development"

    DEBUG: bool = True

    # -------------------------------------------------
    # API
    # -------------------------------------------------

    API_HOST: str = "0.0.0.0"

    API_PORT: int = 8000

    # -------------------------------------------------
    # PostgreSQL
    # -------------------------------------------------

    POSTGRES_HOST: str

    POSTGRES_PORT: int

    POSTGRES_DATABASE: str

    POSTGRES_USER: str

    POSTGRES_PASSWORD: str

    # -------------------------------------------------
    # Oracle
    # -------------------------------------------------

    ORACLE_HOST: str = ""

    ORACLE_PORT: int = 1521

    ORACLE_SERVICE: str = ""

    ORACLE_USER: str = ""

    ORACLE_PASSWORD: str = ""


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
