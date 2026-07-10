"""
Oracle Extractor

Responsável pela leitura das tabelas Oracle.
"""

from __future__ import annotations

from pathlib import Path

import oracledb
import pandas as pd
import yaml

from backend.app.core.logging import logger
from backend.app.core.settings import settings


class OracleExtractor:
    """
    Classe responsável pela conexão e leitura do Oracle.
    """

    def __init__(self):

        self.connection = None

    def connect(self) -> None:
        """
        Abre conexão Oracle.
        """

        logger.info("Conectando Oracle...")

        dsn = oracledb.makedsn(
            host=settings.ORACLE_HOST,
            port=settings.ORACLE_PORT,
            service_name=settings.ORACLE_SERVICE,
        )

        self.connection = oracledb.connect(
            user=settings.ORACLE_USER,
            password=settings.ORACLE_PASSWORD,
            dsn=dsn,
        )

        logger.info("Oracle conectado.")

    def disconnect(self) -> None:
        """
        Fecha conexão Oracle.
        """

        if self.connection is not None:
            self.connection.close()

            logger.info("Oracle desconectado.")

    def load_config(
        self,
        config_file: str | Path,
    ) -> dict:
        """
        Carrega configuração YAML.
        """

        with open(
            config_file,
            "r",
            encoding="utf-8",
        ) as file:
            return yaml.safe_load(file)

    def build_sql(
        self,
        config: dict,
        limit: int | None = None,
    ) -> str:
        """
        Gera dinamicamente o SQL.
        """

        source = config["source"]

        columns = ",\n    ".join(config["columns"])

        sql = f"""
SELECT
    {columns}
FROM {source["schema"]}.{source["table"]}
"""

        filters = config.get("filters")

        if filters:
            conditions = []

            for field, value in filters.items():
                if isinstance(value, list):
                    values = ", ".join(f"'{item}'" for item in value)

                    conditions.append(f"{field} IN ({values})")

                else:
                    conditions.append(f"{field} = '{value}'")

            sql += "\nWHERE\n    "

            sql += "\n    AND ".join(conditions)

        if limit:
            sql += f"\nFETCH FIRST {limit} ROWS ONLY"

        return sql

    def extract(
        self,
        config_file: str | Path,
        limit: int | None = None,
    ) -> pd.DataFrame:
        """
        Extrai dados do Oracle para DataFrame.
        """

        if self.connection is None:
            raise RuntimeError("Oracle não conectado.")

        config = self.load_config(config_file)

        sql = self.build_sql(
            config,
            limit,
        )

        print("\n========== SQL GERADA ==========")
        print(sql)
        print("================================\n")

        logger.info(sql)

        cursor = self.connection.cursor()

        try:
            cursor.execute(sql)

            columns = [column[0] for column in cursor.description]

            rows = cursor.fetchall()

            dataframe = pd.DataFrame(
                rows,
                columns=columns,
            )

            logger.info(
                "Registros encontrados: %s",
                len(dataframe),
            )

            return dataframe

        finally:
            cursor.close()
