"""
Extractor Oracle do PromocoesCOMAER.

Responsável pela leitura das tabelas Oracle e retorno dos
dados em DataFrame Pandas.
"""

from __future__ import annotations

import oracledb
import pandas as pd
import yaml

from backend.app.core.logging import logger
from backend.app.core.settings import settings


class OracleExtractor:
    """Classe responsável pela conexão e leitura do Oracle."""

    def __init__(self):
        self.connection = None

    def connect(self):
        """Abre conexão com o Oracle."""

        logger.info("Conectando ao Oracle...")

        dsn = oracledb.makedsn(
            settings.ORACLE_HOST,
            settings.ORACLE_PORT,
            service_name=settings.ORACLE_SERVICE,
        )

        self.connection = oracledb.connect(
            user=settings.ORACLE_USER,
            password=settings.ORACLE_PASSWORD,
            dsn=dsn,
        )

        logger.info("Oracle conectado.")

    def disconnect(self):
        """Fecha conexão."""

        if self.connection:
            self.connection.close()
            logger.info("Oracle desconectado.")

    def load_config(self, config_file: str) -> dict:
        """Carrega o arquivo YAML da tabela."""

        with open(config_file, encoding="utf-8") as file:
            return yaml.safe_load(file)

    def build_sql(
        self,
        config: dict,
        limit: int | None = None,
    ) -> str:
        """
        Monta dinamicamente o SELECT a partir do YAML.
        """

        columns = ",\n    ".join(config["columns"])

        source = config["source"]

        sql = f"""
SELECT
    {columns}
FROM {source["schema"]}.{source["table"]}
"""

        filters = config.get("filters")

        if filters:
            where = []

            for field, value in filters.items():
                if isinstance(value, list):
                    values = ", ".join(f"'{v}'" for v in value)

                    where.append(f"{field} IN ({values})")

                else:
                    where.append(f"{field} = '{value}'")

            sql += "\nWHERE\n    "
            sql += "\n    AND ".join(where)

        if limit is not None:
            sql += f"\nFETCH FIRST {limit} ROWS ONLY"

        return sql

    def fetch_dataframe(
        self,
        config_file: str,
        limit: int | None = None,
    ) -> pd.DataFrame:
        """
        Executa a consulta Oracle e retorna um DataFrame.
        """

        if self.connection is None:
            raise RuntimeError("Oracle não conectado.")

        config = self.load_config(config_file)

        sql = self.build_sql(
            config=config,
            limit=limit,
        )

        logger.info("SQL gerada:")
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
                "Consulta concluída (%s registros).",
                len(dataframe),
            )

            return dataframe

        finally:
            cursor.close()
