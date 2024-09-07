from typing import Protocol

from onion.domain.dataclasses_.cell import Cell
from onion.domain.dataclasses_.cell_position import CellPosition
from onion.domain.enums_.cell_value import CellValue


class IPlayer(Protocol):
    """
    Interface for class that represents a player.
    """

    def get_name(self) -> str:
        """
        Returns the name of the player.

        :return: name of the player
        """

    def get_cell_value(self) -> CellValue:
        """
        Returns the value of the cell that the player will put on the board on each move.

        :return: value of the cell
        """

    def move(self, empty_cell_pos: list[CellPosition], cells: list[list[Cell]]) -> None:
        """
        Makes a move in the game by putting chosen value (CellValue.X or CellValue.O)
        to a cell with CellValue.E value.

        :param empty_cell_pos: list of positions of empty cells on the board at the current moment
        :param cells: list of all cells on the board
        :return None
        """
