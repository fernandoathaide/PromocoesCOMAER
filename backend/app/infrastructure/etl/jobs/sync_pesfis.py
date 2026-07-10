"""
Job responsável por sincronizar os militares do Oracle.
"""

from pathlib import Path
from time import perf_counter

from backend.app.infrastructure.etl.extract.oracle_extractor import (
    OracleExtractor,
)


def main():

    start = perf_counter()

    extractor = OracleExtractor()

    extractor.connect()

    config_file = Path("etl") / "config" / "T_PESFIS_COMGEP_DW.yml"

    df = extractor.extract(
        config_file=config_file,
        limit=10,
    )

    print()
    print(df.head())
    print()

    print(f"Linhas : {len(df)}")
    print(f"Colunas: {len(df.columns)}")

    print(f"\nTempo: {perf_counter() - start:.2f}s")

    extractor.disconnect()


if __name__ == "__main__":
    main()
