import argparse

from onion.presenter.cli.validators.log_level import LogLevel, log_level_type
from onion.presenter.cli.validators.primitive import non_empty_string, positive_int
from onion.presenter.cli.validators.randomizer import RandomizerType, randomizer_type


def parse_args():
    parser = argparse.ArgumentParser(description="Tic Tac Toe game emulator")
    parser.add_argument(
        "--player-one-name",
        type=non_empty_string,
        help="Name of the first player",
        required=False,
        default="Player1",
    )
    parser.add_argument(
        "--player-two-name",
        type=non_empty_string,
        help="Name of the second player",
        required=False,
        default="Player2",
    )

    parser.add_argument(
        "--rows-number",
        type=positive_int,
        help="Rows number on the board",
        required=False,
        default=3,
    )
    parser.add_argument(
        "--cols-number",
        type=positive_int,
        help="Columns number on the board",
        required=False,
        default=3,
    )

    parser.add_argument(
        "--log-level",
        type=log_level_type,
        help="Log level",
        required=False,
        default=LogLevel.INFO.value,
    )

    parser.add_argument(
        "--randomizer-type",
        type=randomizer_type,
        help="Type of the randomizer service",
        required=False,
        default=RandomizerType.REMOTE.value,
    )
    parser.add_argument(
        "--query-string-key",
        type=non_empty_string,
        help="Query string key for the randomizer service",
        required=False,
        default="value",
    )
    parser.add_argument(
        "--randomize-service-api-url",
        type=non_empty_string,
        help="URL of the randomizer service",
        required=False,
        default="http://localhost:8000/choice",
    )

    return parser.parse_args()
