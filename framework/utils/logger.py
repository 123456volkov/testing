import logging
from typing import Optional


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """Return a configured logger instance.

    The first call configures the root logger; subsequent calls simply fetch
    child loggers. This keeps logging setup in one place for both UI and
    backend tests.
    """

    if not logging.getLogger().handlers:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        )
    return logging.getLogger(name)
