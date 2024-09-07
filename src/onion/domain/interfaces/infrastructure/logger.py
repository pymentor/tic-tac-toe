from typing import Protocol


class ILogger(Protocol):
    """
    Interface for class that logs messages.
    """

    def info(self, message: str) -> None:
        """
        Logs an info message.

        :param message: message template
        :return: None
        """

    def error(self, message: str) -> None:
        """
        Logs an error message.

        :param message: message template
        :return: None
        """

    def debug(self, message: str) -> None:
        """
        Logs a debug message.

        :param message: message template
        :return: None
        """
