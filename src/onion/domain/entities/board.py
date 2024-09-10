from __future__ import annotations

from onion.domain.dataclasses_.cell import Cell
from onion.domain.dataclasses_.cell_position import CellPosition
from onion.domain.dataclasses_.dimension import Dimension
from onion.domain.enums_.cell_value import CellValue


class Board:
    """
    Represents a board in the game.
    """

    def __init__(self, cells: list[list[Cell]]) -> None:
        self._cells = cells

    def get_cells(self) -> list[list[Cell]]:
        """
        Returns a list of all cells on the board at the current moment.

        :return: a list of all cells
        """
        return self._cells

    def get_cells_hr_representation(self) -> str:
        """
        Returns a human readable representation of the board.
        """
        return "\n".join(
            " | ".join(str(cell.value) for cell in row) for row in self._cells
        )

    def get_empty_cells_positions(self) -> list[CellPosition]:
        """
        Returns a list of positions of all empty cells on the board at the current moment.

        :return: a list of positions of all empty cells
        """
        return [
            CellPosition(row_idx=row_idx, col_idx=col_idx)
            for row_idx, row in enumerate(self._cells)
            for col_idx, cell in enumerate(row)
            if cell.value == CellValue.E
        ]

    @classmethod
    def create(cls, dimension: Dimension) -> Board:
        """
        Factory method to create a board of a given dimension.

        [[E,E,E],  <- 1-st row
         [E,E,E],  <- 2-nd row
         [E,E,E]]  <- 3-rd row
          ^ ^ ^
          | | |
          | | 3-rd column
          |  2-nd column
          1-st column

        :param dimension: dimension of the board
        :return: a new board with the given dimension
        """
        # all cels are empty by default
        default_value: CellValue = CellValue.E

        cells: list[list[Cell]] = [
            [Cell(value=default_value) for _ in range(dimension.cols)]
            for _ in range(dimension.rows)
        ]

        return cls(cells=cells)
