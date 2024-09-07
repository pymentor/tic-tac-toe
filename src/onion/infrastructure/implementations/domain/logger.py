import logging


class Logger:
    """
    Class that logs messages.
    """

    def __init__(self, logger: logging.Logger, error_logger: logging.Logger) -> None:
        """
        Initializes the logger. It uses two loggers: one for info/debug messages and one for
        error messages. Error logger is a separate logger because we need to write error
        messages to stderr and info/debug messages to stdout.
        """
        self._logger = logger
        self._error_logger = error_logger

    def info(self, message: str) -> None:
        """
        Logs an info message.

        :param message: message template
        :return: None
        """
        self._logger.info(message)

    def error(self, message: str) -> None:
        """
        Logs an error message.

        :param message: message template
        :return: None
        """
        self._error_logger.error(message)

    def debug(self, message: str) -> None:
        """
        Logs a debug message.

        :param message: message template
        :return: None
        """
        self._logger.debug(message)
