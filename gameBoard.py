"""
Tic-Tac-Toe Game Board model
"""

from itertools import permutations


class TileNotEmptyException(Exception):
    pass


class GameOverException(Exception):
    pass


class GameBoard:
    def __init__(self):
        self._turn = 0
        self.WIN_TEXT = '{} wins'
        self.DRAW_TEXT = 'Draw'
        self.PLAYERS = ['X', 'O']
        # The magic square is used to determine if a player has won:
        # If any 3 of the player's magic values add up to 15, that player has won
        self.MAGIC_SQUARE = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
        self.MAGIC_SUM = 15
        self.players_magic_values = {'X': [], 'O': []}
        self._active_player = 'X'
        empty_row = [" ", " ", " "]
        self.columns = [empty_row.copy(), empty_row.copy(), empty_row.copy()]

    def play(self, row: int, column: int):
        """
        One game turn. Set active player's sign (X or O) into the tile (row, column)
        Columns and rows count from zero
        :return: None
        """
        # ToDo: input validation
        if self.game_is_over:
            raise GameOverException('Game is over. No more moves allowed')
        # Check if tile is empty
        if self.columns[column][row] in ('X', 'O'):
            raise TileNotEmptyException('Tile not empty')
        self.columns[column][row] = self._active_player
        self.players_magic_values[self._active_player].append(self.MAGIC_SQUARE[column][row])
        self._turn += 1
        self._active_player = self.PLAYERS[self.turn % 2]

    def player_has_won(self, player: str):
        """
        Determines if the player has win (3 tiles in a row, column, or main diagonale)
        :param player: str 'X' or 'O'
        :return: bool. If the player has already won
        """
        # The magic square is used: Complete rows, columns or main diagonals always add up to 15,
        # no other combination of 3 tiles adds up to 15.
        magic_moves = self.players_magic_values[player]
        if len(magic_moves) < 2:
            return False
        # check all 3-item permutations of the players moves:
        for perm in permutations(magic_moves, 3):
            if sum(perm) == self.MAGIC_SUM:
                return True
        return False

    @property
    def active_player(self):
        """
        :return: str. The player whose turn it is. "X" or "O"
        """
        return self._active_player

    @property
    def turn(self):
        """
        :return: int. Current turn number. Counts from zero.
        """
        return self._turn

    @property
    def game_is_over(self):
        """
        :return: bool. Either the board is full, or one player has won
        """
        if self._turn >= 9:
            return True
        if self.player_has_won('X') | self.player_has_won('O'):
            return True
        return False

    @property
    def result(self):
        """
        The result of a finshed games
        :return: str. Either "Draw" or "X wins" or "O wins"
        """
        if not self.game_is_over:
            return ""
        if self.player_has_won('X'):
            return self.WIN_TEXT.format('X')
        if self.player_has_won('O'):
            return self.WIN_TEXT.format('O')
        return self.DRAW_TEXT
