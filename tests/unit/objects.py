from typing import Any

from onion.domain.dataclasses_.cell import Cell
from onion.domain.enums_.cell_value import CellValue


def cells_with_winner_value_x_in_diag_1() -> list[list[Cell]]:
    """
    Returns a list of cells with a winner value in the first diagonal - from top left to bottom right.
    """
    return [
        [Cell(value=CellValue.X), Cell(value=CellValue.O), Cell(value=CellValue.X)],
        [Cell(value=CellValue.E), Cell(value=CellValue.X), Cell(value=CellValue.O)],
        [Cell(value=CellValue.E), Cell(value=CellValue.O), Cell(value=CellValue.X)],
    ]


def cells_with_winner_value_x_in_diag_2() -> list[list[Cell]]:
    """
    Returns a list of cells with a winner value in the second diagonal - from top right to bottom left.
    """
    return [
        [Cell(value=CellValue.X), Cell(value=CellValue.O), Cell(value=CellValue.X)],
        [Cell(value=CellValue.E), Cell(value=CellValue.X), Cell(value=CellValue.O)],
        [Cell(value=CellValue.X), Cell(value=CellValue.O), Cell(value=CellValue.E)],
    ]


def cells_with_winner_value_x_in_row_1() -> list[list[Cell]]:
    """
    Returns a list of cells with a winner value in the first row.
    """
    return [
        [Cell(value=CellValue.X), Cell(value=CellValue.X), Cell(value=CellValue.X)],
        [Cell(value=CellValue.E), Cell(value=CellValue.X), Cell(value=CellValue.O)],
        [Cell(value=CellValue.E), Cell(value=CellValue.O), Cell(value=CellValue.E)],
    ]


def cells_with_winner_value_x_in_row_2() -> list[list[Cell]]:
    """
    Returns a list of cells with a winner value in the second row.
    """
    return [
        [Cell(value=CellValue.E), Cell(value=CellValue.O), Cell(value=CellValue.X)],
        [Cell(value=CellValue.X), Cell(value=CellValue.X), Cell(value=CellValue.X)],
        [Cell(value=CellValue.E), Cell(value=CellValue.O), Cell(value=CellValue.E)],
    ]


def cells_with_winner_value_x_in_row_3() -> list[list[Cell]]:
    """
    Returns a list of cells with a winner value in the third row.
    """
    return [
        [Cell(value=CellValue.O), Cell(value=CellValue.O), Cell(value=CellValue.E)],
        [Cell(value=CellValue.E), Cell(value=CellValue.X), Cell(value=CellValue.O)],
        [Cell(value=CellValue.X), Cell(value=CellValue.X), Cell(value=CellValue.X)],
    ]


def cells_with_winner_value_x_in_col_1() -> list[list[Cell]]:
    """
    Returns a list of cells with a winner value in the first column.
    """
    return [
        [Cell(value=CellValue.X), Cell(value=CellValue.O), Cell(value=CellValue.E)],
        [Cell(value=CellValue.X), Cell(value=CellValue.X), Cell(value=CellValue.O)],
        [Cell(value=CellValue.X), Cell(value=CellValue.O), Cell(value=CellValue.E)],
    ]


def cells_with_winner_value_x_in_col_2() -> list[list[Cell]]:
    """
    Returns a list of cells with a winner value in the second column.
    """
    return [
        [Cell(value=CellValue.X), Cell(value=CellValue.X), Cell(value=CellValue.E)],
        [Cell(value=CellValue.E), Cell(value=CellValue.X), Cell(value=CellValue.O)],
        [Cell(value=CellValue.E), Cell(value=CellValue.X), Cell(value=CellValue.E)],
    ]


def cells_with_winner_value_x_in_col_3() -> list[list[Cell]]:
    """
    Returns a list of cells with a winner value in the third column.
    """
    return [
        [Cell(value=CellValue.O), Cell(value=CellValue.E), Cell(value=CellValue.X)],
        [Cell(value=CellValue.E), Cell(value=CellValue.O), Cell(value=CellValue.X)],
        [Cell(value=CellValue.E), Cell(value=CellValue.O), Cell(value=CellValue.X)],
    ]


def cells_with_parity() -> list[list[Cell]]:
    """
    Returns a list of cells with a parity of X and O values.
    """
    return [
        [Cell(value=CellValue.X), Cell(value=CellValue.E), Cell(value=CellValue.X)],
        [Cell(value=CellValue.O), Cell(value=CellValue.E), Cell(value=CellValue.O)],
        [Cell(value=CellValue.X), Cell(value=CellValue.O), Cell(value=CellValue.E)],
    ]


class DeterminerRandomizer:
    def choice(self, *args) -> Any:
        return args[0]
