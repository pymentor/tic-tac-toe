from enum import Enum
from typing import Any


class CellValue(Enum):
    """
    Enum class that represents a value of a cell on the board.

    E - empty cell
    X - cell filled with 'X'
    O - cell filled with 'O'
    """

    E: str = "E"
    X: str = "X"
    O: str = "O"  # noqa: E741

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Enum):
            return False
        return self.value == other.value
