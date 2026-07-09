from pathlib import Path

from sqlalchemy import text

from backend.app.core.database import engine
from backend.app.core.logging import logger

MIGRATIONS_DIR = (
    Path(__file__)
    .resolve()
    .parents[4]
    / "database"
    / "migrations"
)


class MigrationRunner:
    """
    Executa automaticamente todas as migrações SQL
    ainda não aplicadas ao banco.
    """

    def __init__(self):
        self.engine = engine

    def run(self):

        logger.info("Verificando migrações...")

        self._create_schema_version_table()

        executed = self._executed_versions()

        migrations = sorted(
            MIGRATIONS_DIR.glob("V*.sql")
        )

        for migration in migrations:

            version = migration.stem.split("__")[0]

            if version in executed:
                continue

            logger.info(f"Executando {migration.name}")

            sql = migration.read_text(
                encoding="utf-8"
            )

            with self.engine.begin() as conn:

                conn.execute(text(sql))

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
                            true
                        )
                        """
                    ),
                    {
                        "version": version,
                        "description": migration.name,
                    },
                )

        logger.info("Migrações concluídas.")

    def _create_schema_version_table(self):

        with self.engine.begin() as conn:

            conn.execute(
                text(
                    """
                    CREATE SCHEMA IF NOT EXISTS config;

                    CREATE TABLE IF NOT EXISTS config.schema_version
                    (
                        id BIGSERIAL PRIMARY KEY,

                        version VARCHAR(50) UNIQUE,

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

            return {row[0] for row in rows}