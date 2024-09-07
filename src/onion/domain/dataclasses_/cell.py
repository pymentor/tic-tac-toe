from dataclasses import dataclass

from onion.domain.enums_.cell_value import CellValue


@dataclass
class Cell:
    """
    Represents a cell on the board.
    """

    value: CellValue
