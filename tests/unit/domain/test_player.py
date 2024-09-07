def test_get_name(player_one, name1) -> None:
    assert player_one.get_name() == name1


def test_get_cell_value(player_one, cell_value_one) -> None:
    assert player_one.get_cell_value() == cell_value_one


def test_move(
    player_with_determined_randomizer,
    cells_for_board,
    empty_cells_positions,
    determined_randomizer,
) -> None:
    assert (
        player_with_determined_randomizer.move(empty_cells_positions, cells_for_board)
        is None
    )
    cell_pos = determined_randomizer.choice(*empty_cells_positions)
    assert (
        cells_for_board[cell_pos.row_idx][cell_pos.col_idx].value
        == player_with_determined_randomizer.get_cell_value()
    )
