from argparse import Namespace

from onion.domain.dataclasses_.game_result import GameResult
from onion.presenter.cli.parser import parse_args
from onion.presenter.cli.validators.randomizer import RandomizerType
from onion.presenter.di.facade import Dependencies, dependencies_facade
from onion.service.game_launcher import launch_game


def entrypoint() -> GameResult:
    """
    Entry point of the application.
    """
    # Parse CLI arguments
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
    deps: Dependencies = dependencies_facade(
        rows_number=rows_number,
        cols_number=cols_number,
        log_level=log_level,
        randomizer_type=randomizer_type,
        query_string_key=query_string_key,
        randomizer_api_url=randomizer_api_url,
        player_one_name=player_one_name,
        player_two_name=player_two_name,
    )

    # run scenario
    return launch_game(game=deps.game, logger=deps.logger)
