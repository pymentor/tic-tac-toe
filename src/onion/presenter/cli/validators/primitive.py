import argparse


def positive_int(value: str) -> int:
    val: int = int(value)
    if val <= 0:
        raise argparse.ArgumentTypeError(
            f"Invalid value: {value}. Must be a positive integer greater than 0."
        )
    return val


def non_empty_string(value: str) -> str:
    if not value:
        raise argparse.ArgumentTypeError("Empty string is not allowed.")
    return value
