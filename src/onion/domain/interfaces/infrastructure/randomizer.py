from typing import Any, Protocol


class IRandomizer(Protocol):
    """
    Interface for class that returns random elements from a given list of values
    """

    def choice(self, *values: Any) -> Any:
        """
        Returns a random element from the given values.

        :param values: values to choose from randomly
        :return: a random element from the given values
        """
