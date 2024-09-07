import argparse
import logging
from enum import Enum


class LogLevel(Enum):
    INFO: int = "info"
    DEBUG: int = "debug"
    ERROR: int = "error"


LOG_LEVELS_MAP: dict[LogLevel, int] = {
    LogLevel.INFO: logging.INFO,
    LogLevel.DEBUG: logging.DEBUG,
    LogLevel.ERROR: logging.ERROR,
}


def log_level_type(value: str) -> int:
    try:
        return LOG_LEVELS_MAP[LogLevel(value)]
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"Invalid log level: {value}. Choose from {[e.value for e in LogLevel]}"
        )
    except KeyError:
        raise AssertionError(f"Log level {value} is not supported")
