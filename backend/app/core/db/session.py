"""
Factory de sessões SQLAlchemy.
"""

from sqlalchemy.orm import sessionmaker

from backend.app.core.db.postgres import engine

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)
