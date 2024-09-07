import argparse
from enum import Enum


class RandomizerType(Enum):
    LOCAL: str = "local"
    REMOTE: str = "remote"


def randomizer_type(value: str) -> RandomizerType:
    try:
        return RandomizerType(value)
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"Invalid randomizer type: {value}. Choose from {[e.value for e in RandomizerType]}"
        )
