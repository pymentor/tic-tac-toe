from dataclasses import dataclass

from onion.domain.interfaces.domain.board import IBoard
from onion.domain.interfaces.domain.player import IPlayer


@dataclass
class GameResult:
    """
    Represents the result of the game. If there is a winner, the winner is stored.
    If there is no winner, the winner is None and the game is a parity.
    """

    winner: IPlayer | None
    board: IBoard
