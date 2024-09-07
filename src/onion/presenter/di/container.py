import logging
import sys

from onion.domain.dataclasses_.dimension import Dimension
from onion.domain.entities.board import Board
from onion.domain.entities.game import Game
from onion.domain.entities.player import Player
from onion.domain.enums_.cell_value import CellValue
from onion.domain.interfaces.domain.board import IBoard
from onion.domain.interfaces.domain.game import IGame
from onion.domain.interfaces.domain.player import IPlayer
from onion.domain.interfaces.infrastructure.logger import ILogger
from onion.domain.interfaces.infrastructure.randomizer import IRandomizer
from onion.infrastructure.factories.logger import logger_factory
from onion.infrastructure.implementations.domain.local_randomizer import LocalRandomizer
from onion.infrastructure.implementations.domain.logger import Logger
from onion.infrastructure.implementations.domain.remote_randomizer import (
    RemoteRandomizer,
)
from onion.infrastructure.implementations.infrastructure.http_requester import (
    HttpRequester,
)
from onion.infrastructure.interfaces.http_requester import IHttpRequester
from onion.presenter.cli.validators.randomizer import RandomizerType


def create_logger_dependency(log_level: int) -> ILogger:
    common_logger: logging.Logger = logger_factory(
        name="common", level=log_level, stream=sys.stdout
    )
    error_logger: logging.Logger = logger_factory(
        name="error", level=logging.ERROR, stream=sys.stderr
    )
    return Logger(logger=common_logger, error_logger=error_logger)


def create_http_requester_dependency(logger: ILogger) -> IHttpRequester:
    return HttpRequester(logger=logger)


def create_randomizer_dependency(
    randomizer_type: RandomizerType,
    http_requester: IHttpRequester,
    query_string_key: str,
    randomizer_api_url: str,
) -> IRandomizer:
    if randomizer_type == RandomizerType.REMOTE:
        return RemoteRandomizer(
            http_requester=http_requester,
            query_string_key=query_string_key,
            api_url=randomizer_api_url,
        )

    elif randomizer_type == RandomizerType.LOCAL:
        return LocalRandomizer()

    else:
        raise ValueError(f"Unsupported randomizer type: {randomizer_type}")


def create_player_dependency(
    name: str, cell_value: CellValue, randomizer: IRandomizer, logger: ILogger
) -> IPlayer:
    return Player(
        name=name,
        cell_value=cell_value,
        randomizer=randomizer,
        logger=logger,
    )


def create_demension_dependency(rows_number: int, cols_number: int) -> Dimension:
    return Dimension(rows=rows_number, cols=cols_number)


def create_board_dependency(dimension: Dimension) -> IBoard:
    return Board.create(dimension=dimension)


def create_game_dependency(
    player_one: IPlayer,
    player_two: IPlayer,
    board: IBoard,
    randomizer: IRandomizer,
    logger: ILogger,
) -> IGame:
    return Game(
        player_one=player_one,
        player_two=player_two,
        board=board,
        randomizer=randomizer,
        logger=logger,
    )
