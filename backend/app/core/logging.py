"""
Configuração centralizada do sistema de logs.
"""

import logging
from pathlib import Path

from rich.logging import RichHandler

from backend.app.core.config import LOG_DIR


def configure_logging() -> None:
    """Configura o sistema de logging."""

    Path(LOG_DIR).mkdir(
        parents=True,
        exist_ok=True,
    )

    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        handlers=[
            RichHandler(
                rich_tracebacks=True,
                markup=True,
            )
        ],
    )


logger = logging.getLogger("PromocoesCOMAER")
