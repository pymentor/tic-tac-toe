from onion.domain.dataclasses_.cell import Cell
from onion.domain.dataclasses_.cell_position import CellPosition
from onion.domain.enums_.cell_value import CellValue
from onion.domain.interfaces.infrastructure.logger import ILogger
from onion.domain.interfaces.infrastructure.randomizer import IRandomizer


class Player:
    """
    Class that represents a player in the game. It can make a move on the board
    by putting chosen value (CellValue.X or CellValue.O) to a cell with CellValue.E
    value. Chosen empty cell is determined by randomizer from the list of all
    empty cells available for the current moment.
    """

    def __init__(
        self, name: str, cell_value: CellValue, randomizer: IRandomizer, logger: ILogger
    ) -> None:
        self._name = name
        self._cell_value = cell_value
        self._randomizer = randomizer
        self._logger = logger

    def get_name(self) -> str:
        """
        Returns the name of the player.

        :return: name of the player
        """
        return self._name

    def get_cell_value(self) -> CellValue:
        """
        Returns the value of the cell that the player will put on the board on each move.

        :return: value of the cell
        """
        return self._cell_value

    def move(self, empty_cell_pos: list[CellPosition], cells: list[list[Cell]]) -> None:
        """
        Makes a move in the game by putting chosen value (CellValue.X or CellValue.O)
        to a cell with CellValue.E value.

        :param empty_cell_pos: list of positions of empty cells on the board at the current moment
        :param cells: list of all cells on the board
        :return None
        """
        self._logger.debug(
            f"{self._name} is making a move. Empty cells positions: {empty_cell_pos}"
        )

        random_cell_pos: CellPosition = self._randomizer.choice(*empty_cell_pos)

        cell: Cell = cells[random_cell_pos.row_idx][random_cell_pos.col_idx]
        cell.value = self._cell_value

        self._logger.info(
            f"{self._name} moved to {random_cell_pos} with {self._cell_value} value."
        )
