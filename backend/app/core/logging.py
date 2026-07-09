import logging

from rich.logging import RichHandler


def configure_logging():

    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        handlers=[
            RichHandler(
                rich_tracebacks=True
            )
        ],
    )


logger = logging.getLogger("PromocoesCOMAER")
