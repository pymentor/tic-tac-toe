from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CellPosition:
    """
    Represents a position of a cell on the board.
    """

    row_idx: int
    col_idx: int

    def __str__(self) -> str:
        return f"({self.row_idx}, {self.col_idx})"

    def __repr__(self) -> str:
        return self.__str__()

    def __hash__(self) -> int:
        return hash((self.row_idx, self.col_idx))
