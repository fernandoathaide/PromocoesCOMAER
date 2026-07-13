"""
PostgreSQL Loader

Responsável por persistir DataFrames na camada RAW.
"""

from __future__ import annotations

from typing import Optional

import pandas as pd
from sqlalchemy import text

from backend.app.core.db.postgres import engine
from backend.app.core.logging import logger


class PostgresLoader:
    """
    Responsável por gravar DataFrames no PostgreSQL.
    """

    def __init__(self):

        self.engine = engine

    def truncate(
        self,
        schema: str,
        table: str,
    ) -> None:
        """
        Remove todos os registros da tabela.
        """

        logger.info(
            "Limpando tabela %s.%s",
            schema,
            table,
        )

        with self.engine.begin() as conn:
            conn.execute(text(f"TRUNCATE TABLE {schema}.{table}"))

    def load_dataframe(
        self,
        dataframe: pd.DataFrame,
        schema: str,
        table: str,
        if_exists: str = "append",
        chunksize: int = 500,
    ) -> None:
        """
        Persiste um DataFrame no PostgreSQL.
        """

        logger.info(
            "Gravando %s registros em %s.%s",
            len(dataframe),
            schema,
            table,
        )

        dataframe.columns = [coluna.lower() for coluna in dataframe.columns]

        print("\n========== DATAFRAME ==========")
        print(dataframe.head())
        print(dataframe.shape)
        print("===============================\n")

        #
        # Usa a MESMA transação do SQLAlchemy
        #
        with self.engine.begin() as conn:
            dataframe.to_sql(
                name=table,
                schema=schema,
                con=conn,
                if_exists=if_exists,
                index=False,
                chunksize=chunksize,
                #method="multi",
            )

            total = conn.execute(
                text(
                    f"""
                    SELECT COUNT(*)
                    FROM {schema}.{table}
                    """
                )
            ).scalar()

            print(f"\n>>> Registros dentro da transação: {total}\n")

        logger.info("Carga concluída.")

    def replace(
        self,
        dataframe: pd.DataFrame,
        schema: str,
        table: str,
    ) -> None:
        """
        Estratégia inicial.

        TRUNCATE + INSERT
        """

        self.truncate(
            schema=schema,
            table=table,
        )

        self.load_dataframe(
            dataframe=dataframe,
            schema=schema,
            table=table,
        )

    def count(
        self,
        schema: str,
        table: str,
    ) -> Optional[int]:
        """
        Retorna a quantidade de registros.
        """

        with self.engine.connect() as conn:
            return conn.execute(
                text(
                    f"""
                    SELECT COUNT(*)
                    FROM {schema}.{table}
                    """
                )
            ).scalar()
