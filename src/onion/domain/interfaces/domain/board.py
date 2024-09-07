from __future__ import annotations

from typing import Protocol

from onion.domain.dataclasses_.cell import Cell
from onion.domain.dataclasses_.cell_position import CellPosition
from onion.domain.dataclasses_.dimension import Dimension


class IBoard(Protocol):
    """
    Interface for class that represents a board in the game.
    """

    def get_cells(self) -> list[list[Cell]]:
        """
        Returns a list of all cells on the board at the current moment.

        :return: a list of all cells
        """

    def get_cells_hr_representation(self) -> str:
        """
        Returns a human readable representation of the board.
        """

    def get_empty_cells_positions(self) -> list[CellPosition]:
        """
        Returns a list of positions of all empty cells on the board at the current moment.

        :return: a list of positions of all empty cells
        """

    @classmethod
    def create(cls, dim: Dimension) -> IBoard:
        """
        Factory method to create a board of a given dimension.

        :param dim: dimension of the board
        :return: a new board with the given dimension
        """
