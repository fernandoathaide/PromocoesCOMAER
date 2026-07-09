"""
Classe base do SQLAlchemy ORM.
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Classe base utilizada por todas as entidades ORM."""

    pass
