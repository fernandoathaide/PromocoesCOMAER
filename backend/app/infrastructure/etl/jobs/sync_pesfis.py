from pathlib import Path
from time import perf_counter

from backend.app.infrastructure.etl.extract.oracle_extractor import (
    OracleExtractor,
)


def main():

    start = perf_counter()

    extractor = OracleExtractor()

    extractor.connect()

    config = Path("etl") / "config" / "T_PESFIS_COMGEP_DW.yml"

    df = extractor.fetch_dataframe(
        str(config),
        limit=10,
    )

    print()

    print(df.head())

    print()

    print(f"Linhas: {len(df)}")

    print(f"Colunas: {len(df.columns)}")

    print()

    print(f"Tempo: {perf_counter() - start:.2f}s")

    extractor.disconnect()


if __name__ == "__main__":
    main()
