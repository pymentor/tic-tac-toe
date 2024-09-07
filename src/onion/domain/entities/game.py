from onion.domain.dataclasses_.cell import Cell
from onion.domain.dataclasses_.cell_position import CellPosition
from onion.domain.dataclasses_.game_result import GameResult
from onion.domain.enums_.cell_value import CellValue
from onion.domain.interfaces.domain.board import IBoard
from onion.domain.interfaces.domain.player import IPlayer
from onion.domain.interfaces.infrastructure.logger import ILogger
from onion.domain.interfaces.infrastructure.randomizer import IRandomizer


class Game:
    """
    Class that represents a game.
    """

    def __init__(
        self,
        player_one: IPlayer,
        player_two: IPlayer,
        board: IBoard,
        randomizer: IRandomizer,
        logger: ILogger,
    ) -> None:
        self._board = board
        self._logger = logger
        self._randomizer = randomizer
        self._player_one = player_one
        self._player_two = player_two

    def start(self) -> GameResult:
        """
        Starts the game.

        :return: the result of the game
        """
        self._logger.info(
            f"Game has started. Players: {self._player_one.get_name()} and {self._player_two.get_name()}."
        )

        # choose who goes first
        all_players: list[IPlayer] = [self._player_one, self._player_two]
        first_player: IPlayer = self._randomizer.choice(*all_players)

        # choose who goes second
        all_players.remove(first_player)
        second_player: IPlayer = all_players.pop()

        self._logger.info(
            f"{first_player.get_name()} moves first with value {first_player.get_cell_value()}. "
            f"{second_player.get_name()} moves second with value {second_player.get_cell_value()}."
        )

        # get all cells on the board in the initial state (all cells are empty)
        cells: list[list[Cell]] = self._board.get_cells()

        self._logger.debug(
            f"Initial board:\n{self._board.get_cells_hr_representation()}"
        )

        # run main game loop
        while True:
            # iterate over players. the first player goes first, the second player goes second
            # on every iteration of the main loop
            for player in (first_player, second_player):
                # get empty cells positions for the current moment
                empty_cells_pos: list[CellPosition] = (
                    self._board.get_empty_cells_positions()
                )

                # player moves
                player.move(empty_cells_pos, cells)

                # check if game is over
                game_result: GameResult | None = self._is_game_over(cells)

                self._logger.debug(
                    f"Board after {player.get_name()} move:\n"
                    f"{self._board.get_cells_hr_representation()}"
                )

                # if game is over (there is a winner or parity), return the result
                if game_result is not None:
                    self._logger.info("Game has finished.")
                    return game_result

    def _get_winner_value_in_rows(self, cells: list[list[Cell]]) -> CellValue | None:
        """
        Get the winner value in rows.

        Example:

        [[E, E, E],
         [X, X, X], <- winner value X in 2-nd row
         [E, E, E]]

        :param cells: list of all cells on the board
        :return: winner value if there is a winner, None otherwise
        """
        self._logger.debug("Getting winner value in rows for cells")

        dim: int = len(cells)

        for row_idx in range(dim):  # rows
            cells_filled_with_o: int = 0
            cells_filled_with_x: int = 0

            for col_idx in range(dim):  # columns
                if cells[row_idx][col_idx].value == CellValue.X:
                    cells_filled_with_x += 1

                elif cells[row_idx][col_idx].value == CellValue.O:
                    cells_filled_with_o += 1

            if cells_filled_with_x == dim:
                self._logger.debug(f"Winner value X in {row_idx + 1}-st row")
                return CellValue.X

            if cells_filled_with_o == dim:
                self._logger.debug(f"Winner value O in {row_idx + 1}-st row")
                return CellValue.O

        self._logger.debug("No winner value in rows")
        return None

    def _get_winner_value_in_cols(self, cells: list[list[Cell]]) -> CellValue | None:
        """
        Get the winner value in columns.

        Example:

        [[O, X, E],
         [O, X, O],
         [E, X, E]]
             ^
             |
             winner value X in 2-nd column

        :param cells: list of all cells on the board
        :return: winner value if there is a winner, None otherwise
        """
        self._logger.debug("Getting winner value in columns for cells")

        dim: int = len(cells)

        for col_idx in range(dim):  # columns
            cells_filled_with_o: int = 0
            cells_filled_with_x: int = 0

            for row_idx in range(dim):  # rows
                if cells[row_idx][col_idx].value == CellValue.X:
                    cells_filled_with_x += 1

                elif cells[row_idx][col_idx].value == CellValue.O:
                    cells_filled_with_o += 1

            if cells_filled_with_x == dim:
                self._logger.debug(f"Winner value X in {col_idx + 1}-st column")
                return CellValue.X

            if cells_filled_with_o == dim:
                self._logger.debug(f"Winner value O in {col_idx + 1}-st column")
                return CellValue.O

        self._logger.debug("No winner value in columns")
        return None

    def _get_winner_value_in_diags(self, cells: list[list[Cell]]) -> CellValue | None:
        """
        Get the winner value in diagonals.

        Examples:

        [[X, O, O],
         [E, X, E],
         [E, E, X]]
                ^
                |
                winner value X in left-top -> right-bottom diag

        [[O, E, X],
         [O, X, E],
         [X, E, E]]
          ^
          |
          winner value X in right-top -> left-bottom diag

        :param cells: list of all cells on the board
        :return: winner value if there is a winner, None otherwise
        """
        self._logger.debug("Getting winner value in diagonals for cells")

        dim: int = len(cells)

        for col_idx_start_value in (0, dim - 1):
            # 0 is for `left-top -> right-bottom` diag
            # (dim - 1) is for `right-top -> left-bottom` diag
            row_idx: int = 0
            col_idx: int = col_idx_start_value

            cells_filled_with_x: int = 0
            cells_filled_with_o: int = 0

            while row_idx < dim:
                if cells[row_idx][col_idx].value == CellValue.X:
                    cells_filled_with_x += 1

                elif cells[row_idx][col_idx].value == CellValue.O:
                    cells_filled_with_o += 1

                row_idx += 1

                if col_idx_start_value == 0:
                    # `left-top -> right-bottom` diag
                    col_idx += 1
                else:
                    # `right-top -> left-bottom` diag
                    col_idx -= 1

            if cells_filled_with_x == dim:
                self._logger.debug(
                    f"Winner value X in {'left-top -> right-bottom' if col_idx_start_value == 0 else 'right-top -> left-bottom'} diag"
                )
                return CellValue.X

            if cells_filled_with_o == dim:
                self._logger.debug(
                    f"Winner value O in {'left-top -> right-bottom' if col_idx_start_value == 0 else 'right-top -> left-bottom'} diag"
                )
                return CellValue.O

        self._logger.debug("No winner value in diagonals")
        return None

    def _is_game_over(self, cells: list[list[Cell]]) -> GameResult | None:
        """
        Method to determine if the game is over (there is a winner or a parity).

        :param cells: list of all cells on the board
        :return: the result of the game if it is over, None otherwise
        """
        # get winner values in rows, columns, and diagonals and
        # iterate over all the results and try to determine a winner
        self._logger.debug("Checking if game is over")

        for winner_value in (
            self._get_winner_value_in_rows(cells),
            self._get_winner_value_in_cols(cells),
            self._get_winner_value_in_diags(cells),
        ):
            if winner_value is not None:
                # determine winner player
                winner_player: IPlayer = self._determine_winner(winner_value)
                self._logger.debug(f"Determined a winner: {winner_player.get_name()}.")
                return GameResult(winner=winner_player, board=self._board)

        # try to determine if game is over but with a parity - no winner and
        # players can't move anymore since no empty cells left
        if not self._board.get_empty_cells_positions():
            self._logger.debug("Determined a parity.")
            return GameResult(winner=None, board=self._board)

        self._logger.debug("Game is not over yet.")
        return None

    def _determine_winner(self, winner_value: CellValue) -> IPlayer:
        """
        Determine the winner player by the winner value.

        :param winner_value: winner value
        :return: the winner player
        """
        for player in (self._player_one, self._player_two):
            if player.get_cell_value() == winner_value:
                return player

        raise AssertionError(
            f"Failed to determine winner player for cell value {winner_value}"
        )
