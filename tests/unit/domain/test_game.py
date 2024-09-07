import pytest

from onion.domain.dataclasses_.cell import Cell
from onion.domain.entities.game import Game
from onion.domain.enums_.cell_value import CellValue
from unit.objects import (
    cells_with_winner_value_x_in_diag_1,
    cells_with_winner_value_x_in_diag_2,
    cells_with_winner_value_x_in_row_1,
    cells_with_winner_value_x_in_row_2,
    cells_with_winner_value_x_in_row_3,
    cells_with_winner_value_x_in_col_1,
    cells_with_winner_value_x_in_col_2,
    cells_with_winner_value_x_in_col_3,
    cells_with_parity,
    cells_with_winner_value_o_in_diag_1,
    cells_with_winner_value_o_in_diag_2,
    cells_with_winner_value_o_in_row_1,
    cells_with_winner_value_o_in_row_2,
    cells_with_winner_value_o_in_row_3,
    cells_with_winner_value_o_in_col_1,
    cells_with_winner_value_o_in_col_2,
    cells_with_winner_value_o_in_col_3,
)


@pytest.mark.parametrize(
    "cells, expected_result",
    [
        (cells_with_winner_value_x_in_diag_1(), CellValue.X),
        (cells_with_winner_value_x_in_diag_2(), CellValue.X),
        (cells_with_winner_value_o_in_diag_1(), CellValue.O),
        (cells_with_winner_value_o_in_diag_2(), CellValue.O),
        (cells_with_winner_value_x_in_row_1(), None),
        (cells_with_winner_value_x_in_row_2(), None),
        (cells_with_winner_value_x_in_row_3(), None),
        (cells_with_winner_value_x_in_col_1(), None),
        (cells_with_winner_value_x_in_col_2(), None),
        (cells_with_winner_value_x_in_col_3(), None),
        (cells_with_parity(), None),
    ],
)
def test__get_winner_value_in_diags(
    game: Game, cells: list[list[Cell]], expected_result: CellValue
) -> None:
    assert game._get_winner_value_in_diags(cells) == expected_result


@pytest.mark.parametrize(
    "cells, expected_result",
    [
        (cells_with_winner_value_x_in_diag_1(), None),
        (cells_with_winner_value_x_in_diag_2(), None),
        (cells_with_winner_value_x_in_row_1(), CellValue.X),
        (cells_with_winner_value_x_in_row_2(), CellValue.X),
        (cells_with_winner_value_x_in_row_3(), CellValue.X),
        (cells_with_winner_value_o_in_row_1(), CellValue.O),
        (cells_with_winner_value_o_in_row_2(), CellValue.O),
        (cells_with_winner_value_o_in_row_3(), CellValue.O),
        (cells_with_winner_value_x_in_col_1(), None),
        (cells_with_winner_value_x_in_col_2(), None),
        (cells_with_winner_value_x_in_col_3(), None),
        (cells_with_parity(), None),
    ],
)
def test__get_winner_value_in_rows(
    game: Game, cells: list[list[Cell]], expected_result: CellValue
) -> None:
    assert game._get_winner_value_in_rows(cells) == expected_result


@pytest.mark.parametrize(
    "cells, expected_result",
    [
        (cells_with_winner_value_x_in_diag_1(), None),
        (cells_with_winner_value_x_in_diag_2(), None),
        (cells_with_winner_value_x_in_row_1(), None),
        (cells_with_winner_value_x_in_row_2(), None),
        (cells_with_winner_value_x_in_row_3(), None),
        (cells_with_winner_value_x_in_col_1(), CellValue.X),
        (cells_with_winner_value_x_in_col_2(), CellValue.X),
        (cells_with_winner_value_x_in_col_3(), CellValue.X),
        (cells_with_winner_value_o_in_col_1(), CellValue.O),
        (cells_with_winner_value_o_in_col_2(), CellValue.O),
        (cells_with_winner_value_o_in_col_3(), CellValue.O),
        (cells_with_parity(), None),
    ],
)
def test__get_winner_value_in_cols(
    game: Game, cells: list[list[Cell]], expected_result: CellValue
) -> None:
    assert game._get_winner_value_in_cols(cells) == expected_result
