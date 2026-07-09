"""
Engine de conexão com Oracle.
"""

from sqlalchemy import create_engine

from backend.app.core.settings import settings

ORACLE_URL = (
    "oracle+oracledb://"
    f"{settings.ORACLE_USER}:"
    f"{settings.ORACLE_PASSWORD}@"
    f"{settings.ORACLE_HOST}:"
    f"{settings.ORACLE_PORT}/"
    f"?service_name={settings.ORACLE_SERVICE}"
)

oracle_engine = create_engine(
    ORACLE_URL,
    echo=False,
    future=True,
)
