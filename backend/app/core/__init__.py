"""
Camada de acesso ao banco.
"""

from backend.app.core.db.postgres import engine
from backend.app.core.db.session import SessionLocal

__all__ = [
    "engine",
    "SessionLocal",
]
