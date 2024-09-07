from onion.domain.entities.board import Board


def test_get_cells(board_with_cells, cells_for_board) -> None:
    assert board_with_cells.get_cells() == cells_for_board


def test_get_cells_hr_representation(board_with_cells, cells_for_board) -> None:
    assert board_with_cells.get_cells_hr_representation() == "\n".join(
        [" | ".join([str(cell.value) for cell in row]) for row in cells_for_board]
    )


def test_get_empty_cells_positions(board_with_cells, empty_cells_positions) -> None:
    assert board_with_cells.get_empty_cells_positions() == empty_cells_positions


def test_create(dimension, empty_cells_for_board) -> None:
    assert Board.create(dimension=dimension).get_cells() == empty_cells_for_board
