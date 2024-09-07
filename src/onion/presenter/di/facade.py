from dataclasses import dataclass

from onion.domain.dataclasses_.dimension import Dimension
from onion.domain.enums_.cell_value import CellValue
from onion.domain.interfaces.domain.board import IBoard

from onion.domain.interfaces.domain.game import IGame
from onion.domain.interfaces.domain.player import IPlayer
from onion.domain.interfaces.infrastructure.logger import ILogger
from onion.domain.interfaces.infrastructure.randomizer import IRandomizer
from onion.infrastructure.interfaces.http_requester import IHttpRequester
from onion.presenter.cli.validators.randomizer import RandomizerType
from onion.presenter.di.container import (
    create_logger_dependency,
    create_http_requester_dependency,
    create_randomizer_dependency,
    create_player_dependency,
    create_demension_dependency,
    create_board_dependency,
    create_game_dependency,
)


@dataclass
class Dependencies:
    game: IGame
    logger: ILogger


def dependencies_facade(
    rows_number: int,
    cols_number: int,
    log_level: int,
    randomizer_type: RandomizerType,
    query_string_key: str,
    randomizer_api_url: str,
    player_one_name: str,
    player_two_name: str,
) -> Dependencies:
    logger: ILogger = create_logger_dependency(log_level=log_level)

    http_requester: IHttpRequester = create_http_requester_dependency(logger=logger)

    randomizer: IRandomizer = create_randomizer_dependency(
        randomizer_type=randomizer_type,
        http_requester=http_requester,
        query_string_key=query_string_key,
        randomizer_api_url=randomizer_api_url,
    )

    player_one: IPlayer = create_player_dependency(
        name=player_one_name,
        cell_value=CellValue.X,
        randomizer=randomizer,
        logger=logger,
    )

    player_two: IPlayer = create_player_dependency(
        name=player_two_name,
        cell_value=CellValue.O,
        randomizer=randomizer,
        logger=logger,
    )

    dimension: Dimension = create_demension_dependency(
        rows_number=rows_number, cols_number=cols_number
    )

    board: IBoard = create_board_dependency(dimension=dimension)

    game: IGame = create_game_dependency(
        player_one=player_one,
        player_two=player_two,
        board=board,
        randomizer=randomizer,
        logger=logger,
    )

    return Dependencies(game=game, logger=logger)
