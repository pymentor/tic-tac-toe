from enum import Enum

from onion.domain.dataclasses_.dimension import Dimension


class SupportedDimensions(Enum):
    """
    Represents supported dimensions for a board. Board must be a square,
    so only equal number of rows and columns is allowed.
    """

    THREE_ON_THREE = Dimension(rows=3, cols=3)
    FIVE_ON_FIVE = Dimension(rows=5, cols=5)
    SEVEN_ON_SEVEN = Dimension(rows=7, cols=7)
    NINE_ON_NINE = Dimension(rows=9, cols=9)
