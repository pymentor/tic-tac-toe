import logging
import sys

import pytest

from onion.domain.dataclasses_.cell import Cell
from onion.domain.dataclasses_.cell_position import CellPosition
from onion.domain.dataclasses_.dimension import Dimension
from onion.domain.entities.board import Board
from onion.domain.entities.game import Game
from onion.domain.entities.player import Player
from onion.domain.enums_.cell_value import CellValue

from onion.infrastructure.factories.logger import logger_factory
from onion.infrastructure.implementations.domain.local_randomizer import LocalRandomizer
from onion.infrastructure.implementations.domain.logger import Logger
from unit.objects import DeterminerRandomizer


@pytest.fixture
def randomizer() -> LocalRandomizer:
    yield LocalRandomizer()


@pytest.fixture
def logger() -> Logger:
    common_logger: logging.Logger = logger_factory(
        name="common", level=logging.INFO, stream=sys.stdout
    )
    error_logger: logging.Logger = logger_factory(
        name="error", level=logging.ERROR, stream=sys.stderr
    )
    yield Logger(logger=common_logger, error_logger=error_logger)


@pytest.fixture
def name1() -> str:
    yield "Player1"


@pytest.fixture
def name2() -> str:
    yield "Player2"


@pytest.fixture
def cell_value_one() -> CellValue:
    yield CellValue.X


@pytest.fixture
def cell_value_two() -> CellValue:
    yield CellValue.O


@pytest.fixture
def player_one(randomizer, logger, name1, cell_value_one) -> Player:
    yield Player(
        name=name1, cell_value=cell_value_one, randomizer=randomizer, logger=logger
    )


@pytest.fixture
def determined_randomizer() -> DeterminerRandomizer:
    yield DeterminerRandomizer()


@pytest.fixture
def player_with_determined_randomizer(
    determined_randomizer, logger, name1, cell_value_one
) -> Player:
    yield Player(
        name=name1,
        cell_value=cell_value_one,
        randomizer=determined_randomizer,
        logger=logger,
    )


@pytest.fixture
def player_two(randomizer, logger, name2, cell_value_two) -> Player:
    yield Player(
        name=name2, cell_value=cell_value_two, randomizer=randomizer, logger=logger
    )


@pytest.fixture
def dimension() -> Dimension:
    yield Dimension(rows=3, cols=3)


@pytest.fixture
def board(dimension) -> Board:
    yield Board.create(dimension=dimension)


@pytest.fixture
def cells_for_board() -> list[list[Cell]]:
    yield [
        [Cell(value=CellValue.E), Cell(value=CellValue.E), Cell(value=CellValue.E)],
        [Cell(value=CellValue.X), Cell(value=CellValue.E), Cell(value=CellValue.E)],
        [Cell(value=CellValue.E), Cell(value=CellValue.O), Cell(value=CellValue.E)],
    ]


@pytest.fixture
def empty_cells_for_board() -> list[list[Cell]]:
    yield [
        [Cell(value=CellValue.E), Cell(value=CellValue.E), Cell(value=CellValue.E)],
        [Cell(value=CellValue.E), Cell(value=CellValue.E), Cell(value=CellValue.E)],
        [Cell(value=CellValue.E), Cell(value=CellValue.E), Cell(value=CellValue.E)],
    ]


@pytest.fixture
def empty_cells_positions(cells_for_board) -> list[CellPosition]:
    yield [
        CellPosition(row_idx=row_idx, col_idx=col_idx)
        for row_idx, row in enumerate(cells_for_board)
        for col_idx, cell in enumerate(row)
        if cell.value == CellValue.E
    ]


@pytest.fixture
def board_with_cells(cells_for_board) -> Board:
    yield Board(cells=cells_for_board)


@pytest.fixture
def game(player_one, player_two, board, randomizer, logger) -> Game:
    yield Game(
        player_one=player_one,
        player_two=player_two,
        board=board,
        randomizer=randomizer,
        logger=logger,
    )
