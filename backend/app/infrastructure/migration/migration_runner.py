from pathlib import Path

from sqlalchemy import text

from backend.app.core.db.postgres import engine
from backend.app.core.logging import logger

MIGRATIONS_DIR = Path(__file__).resolve().parents[4] / "database" / "migrations"


class MigrationRunner:
    """
    Executa automaticamente todas as migrations
    ainda não aplicadas ao banco.
    """

    def __init__(self):

        self.engine = engine

    def run(self):

        logger.info("=" * 70)
        logger.info("PROMOCOESCOMAER - Migration Runner")
        logger.info("=" * 70)

        self._create_schema_version_table()

        executed = self._executed_versions()

        migrations = sorted(MIGRATIONS_DIR.glob("V*.sql"))

        logger.info(
            "Encontradas %s migrations.",
            len(migrations),
        )

        for migration in migrations:
            version = migration.stem.split("__")[0]

            if version in executed:
                logger.info(
                    "%s já executada.",
                    migration.name,
                )

                continue

            sql = migration.read_text(
                encoding="utf-8",
            ).strip()

            if not sql:
                logger.warning(
                    "%s vazia. Ignorada.",
                    migration.name,
                )

                continue

            logger.info(
                "Executando %s",
                migration.name,
            )

            with self.engine.begin() as conn:
                raw = conn.connection

                cursor = raw.cursor()

                try:
                    statements = [stmt.strip() for stmt in sql.split(";") if stmt.strip()]

                    for statement in statements:
                        cursor.execute(statement)

                finally:
                    cursor.close()

                conn.execute(
                    text(
                        """
                        INSERT INTO config.schema_version
                        (
                            version,
                            description,
                            success
                        )
                        VALUES
                        (
                            :version,
                            :description,
                            TRUE
                        )
                        """
                    ),
                    {
                        "version": version,
                        "description": migration.name,
                    },
                )

            logger.info(
                "%s concluída.",
                migration.name,
            )

        logger.info("=" * 70)
        logger.info("Fim das migrations.")
        logger.info("=" * 70)

    def _create_schema_version_table(self):

        with self.engine.begin() as conn:
            conn.execute(
                text(
                    """
                    CREATE SCHEMA IF NOT EXISTS config;

                    CREATE TABLE IF NOT EXISTS config.schema_version
                    (
                        id BIGSERIAL PRIMARY KEY,

                        version VARCHAR(30) UNIQUE,

                        description VARCHAR(255),

                        installed_on TIMESTAMP
                            DEFAULT CURRENT_TIMESTAMP,

                        success BOOLEAN
                    );
                    """
                )
            )

    def _executed_versions(self):

        with self.engine.connect() as conn:
            rows = conn.execute(
                text(
                    """
                    SELECT version
                    FROM config.schema_version
                    """
                )
            )

            return {row.version for row in rows}
