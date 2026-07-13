"""
Job responsável pela sincronização da tabela
SIG.T_PESFIS_COMGEP_DW para o PostgreSQL.
"""

from pathlib import Path
from time import perf_counter

from backend.app.core.logging import logger
from backend.app.infrastructure.etl.extract.oracle_extractor import (
    OracleExtractor,
)
from backend.app.infrastructure.etl.load.postgres_loader import (
    PostgresLoader,
)
from backend.app.infrastructure.migration.migration_runner import (
    MigrationRunner,
)


def main():

    start = perf_counter()

    MigrationRunner().run()

    logger.info("=" * 70)
    logger.info("SINCRONIZAÇÃO T_PESFIS_COMGEP_DW")
    logger.info("=" * 70)

    extractor = OracleExtractor()

    loader = PostgresLoader()

    config_file = Path("etl") / "config" / "T_PESFIS_COMGEP_DW.yml"

    try:
        #
        # Conecta Oracle
        #
        extractor.connect()

        #
        # Carrega configuração
        #
        config = extractor.load_config(config_file)

        #
        # Extrai dados Oracle
        #
        df = extractor.extract(
            config_file=config_file,
            limit=None,
        )

        logger.info(
            "%s registros extraídos.",
            len(df),
        )

        #
        # Salva PostgreSQL
        #
        loader.replace(
            dataframe=df,
            schema=config["target"]["schema"],
            table=config["target"]["table"],
        )

        total = loader.count(
            schema=config["target"]["schema"],
            table=config["target"]["table"],
        )

        logger.info(
            "%s registros gravados.",
            total,
        )

        print()
        print(df.head())

        print()

        print(f"Registros Oracle : {len(df)}")

        print(f"Registros Postgre: {total}")

        print(f"\nTempo total: {perf_counter() - start:.2f}s")

    finally:
        extractor.disconnect()


if __name__ == "__main__":
    main()
