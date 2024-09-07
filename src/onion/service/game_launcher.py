from onion.domain.dataclasses_.game_result import GameResult
from onion.domain.interfaces.domain.game import IGame
from onion.domain.interfaces.infrastructure.logger import ILogger


def launch_game(game: IGame, logger: ILogger) -> None:
    """
    Use case (scenario) that launches the game.

    :param game: game to launch
    :param logger: logger
    :return: None
    """
    logger.info("Launching game...")

    result: GameResult = game.start()

    logger.info(
        f"{'Winner is ' + result.winner.get_name() if result.winner else 'No winners, no loosers. Parity'}.\n"
        f"Board:\n{result.board.get_cells_hr_representation()}"
    )
