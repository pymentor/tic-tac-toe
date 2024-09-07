from typing import Protocol

from onion.domain.dataclasses_.game_result import GameResult


class IGame(Protocol):
    """
    Interface for class that represents a game.
    """

    def start(self) -> GameResult:
        """
        Starts the game.

        :return: the result of the game
        """
