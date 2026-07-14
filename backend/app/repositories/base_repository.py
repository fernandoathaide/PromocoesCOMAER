"""
Repository base.

Contém operações comuns de acesso ao PostgreSQL.
"""

from __future__ import annotations

from sqlalchemy import text

from backend.app.core.db.session import SessionLocal


class BaseRepository:
    """
    Classe base para todos os repositories.
    """

    def __init__(self):

        self.session = SessionLocal()

    def close(self):

        self.session.close()

    def execute(
        self,
        sql: str,
        params: dict | None = None,
    ):

        return self.session.execute(
            text(sql),
            params or {},
        )

    def fetch_all(
        self,
        sql: str,
        params: dict | None = None,
    ):

        result = self.execute(sql, params)

        return result.mappings().all()

    def fetch_one(
        self,
        sql: str,
        params: dict | None = None,
    ):

        result = self.execute(sql, params)

        return result.mappings().first()

    def scalar(
        self,
        sql: str,
        params: dict | None = None,
    ):

        result = self.execute(sql, params)

        return result.scalar()

    def commit(self):

        self.session.commit()

    def rollback(self):

        self.session.rollback()
