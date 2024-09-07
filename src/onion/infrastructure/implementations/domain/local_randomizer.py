from __future__ import annotations

from random import Random, SystemRandom
from typing import Any


class LocalRandomizer:
    """
    Class that returns random elements from a given list of values,
    using the local random number generator.
    """

    def __init__(self, random: Random | None = None) -> None:
        self._random = SystemRandom() if random is None else random

    def choice(self, *values: Any) -> Any:
        """
        Returns a random element from the given values.

        :param values: values to choose from randomly
        :return: a random element from the given values
        """
        return self._random.choice(values)
