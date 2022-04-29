"""
Tic-Tac-Toe Game Board model
"""


class TileNotEmptyException(Exception):
    pass


class GameBoard:
    def __init__(self):
        self._turn = 0
        self.PLAYERS = ['X', 'O']
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
        # Check if tile is empty
        if self.columns[column][row] in ('X', 'O'):
            raise TileNotEmptyException('Tile not empty')
        self.columns[column][row] = self._active_player
        self._turn += 1
        self._active_player = self.PLAYERS[self.turn % 2]

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
        # ToDo: check if someone has won
        return False
