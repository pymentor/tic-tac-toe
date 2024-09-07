import logging
import sys
from argparse import Namespace

from onion.domain.dataclasses_.dimension import Dimension
from onion.domain.entities.board import Board
from onion.domain.entities.game import Game
from onion.domain.entities.player import Player
from onion.domain.enums_.cell_value import CellValue
from onion.infrastructure.factories.logger import logger_factory
from onion.infrastructure.implementations.domain.local_randomizer import LocalRandomizer
from onion.infrastructure.implementations.domain.logger import Logger
from onion.infrastructure.implementations.domain.remote_randomizer import (
    RemoteRandomizer,
)
from onion.infrastructure.implementations.infrastructure.http_requester import (
    HttpRequester,
)
from onion.presenter.cli.parser import parse_args
from onion.presenter.cli.validators.randomizer import RandomizerType
from onion.service.game_launcher import launch_game


def entrypoint() -> None:
    """
    Entry point of the application.
    """
    # Parse command line arguments
    args: Namespace = parse_args()

    player_one_name: str = args.player_one_name
    player_two_name: str = args.player_two_name

    rows_number: int = args.rows_number
    cols_number: int = args.cols_number

    log_level: int = args.log_level

    randomizer_type: RandomizerType = args.randomizer_type
    query_string_key: str = args.query_string_key
    randomizer_api_url: str = args.randomize_service_api_url

    # create required dependencies
    common_logger: logging.Logger = logger_factory(
        name="common", level=log_level, stream=sys.stdout
    )
    error_logger: logging.Logger = logger_factory(
        name="error", level=logging.ERROR, stream=sys.stderr
    )

    logger: Logger = Logger(logger=common_logger, error_logger=error_logger)

    if randomizer_type == RandomizerType.REMOTE:
        http_requester: HttpRequester = HttpRequester(logger=logger)

        randomizer: RemoteRandomizer = RemoteRandomizer(
            http_requester=http_requester,
            query_string_key=query_string_key,
            api_url=randomizer_api_url,
        )
    else:
        randomizer: LocalRandomizer = LocalRandomizer()

    player_one: Player = Player(
        name=player_one_name,
        cell_value=CellValue.X,
        randomizer=randomizer,
        logger=logger,
    )

    player_two: Player = Player(
        name=player_two_name,
        cell_value=CellValue.O,
        randomizer=randomizer,
        logger=logger,
    )

    dimension: Dimension = Dimension(rows=rows_number, cols=cols_number)

    board: Board = Board.create(dimension=dimension)

    game: Game = Game(
        player_one=player_one,
        player_two=player_two,
        board=board,
        randomizer=randomizer,
        logger=logger,
    )

    # run scenario
    launch_game(game=game, logger=logger)
