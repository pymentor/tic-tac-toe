import logging
from typing import TextIO


def logger_factory(name: str, level: int, stream: TextIO) -> logging.Logger:
    """
    Factory to create a logging.Logger instance with the given name,
    log level and stream to write to.

    :param name: name of the logger
    :param level: logging level
    :param stream: stream to write log messages to
    :return: a new logging.Logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    handler = logging.StreamHandler(stream=stream)
    handler.setLevel(level)

    formatter = logging.Formatter(
        fmt="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    handler.setFormatter(formatter)

    if handler not in logger.handlers:
        logger.addHandler(handler)

    return logger
