import pytest
from gameBoard import GameBoard, TileNotEmptyException


@pytest.fixture
def board():
    return GameBoard()


def test_turn_increase(board):
    """
    Tests whether turn increases on a call to play()
    :param board: GameBoard from fixture "board"
    :return: None
    """
    assert(board.turn == 0)
    board.play(0, 0)
    assert(board.turn == 1)


def test_play(board):
    """
    Tests whether active_player changes on a call to play()
    :param board: GameBoard from fixture "board"
    :return: None
    """
    assert(board.active_player == 'X')
    board.play(0, 0)
    assert(board.active_player == 'O')
    board.play(0, 1)
    assert(board.active_player == 'X')


def test_board_not_full(board):
    """
    Tests whether the game is not over before 9 moves
    :param board: GameBoard from fixture "board"
    :return: None
    """
    # Play 8 moves
    # Literal coordinates to make the test not fail after adding winning condition check
    board.play(0, 0)
    assert not board.game_is_over
    board.play(1, 0)
    assert not board.game_is_over
    board.play(1, 1)
    assert not board.game_is_over
    board.play(2, 2)
    assert not board.game_is_over
    board.play(2, 1)
    assert not board.game_is_over
    board.play(0, 1)
    assert not board.game_is_over
    board.play(0, 2)
    assert not board.game_is_over
    board.play(2, 0)
    assert not board.game_is_over


def test_board_full(board):
    """
    Tests whether the game is over when the board is full
    :param board: GameBoard from fixture "board"
    :return: None
    """
    for col in range(3):
        for row in range(3):
            board.play(row=row, column=col)
    assert board.game_is_over


@pytest.mark.parametrize("row, column", [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)])
def test_tile_not_empty(board, row, column):
    """
    Tests the TileNotEmptyException on play on occupied tile
    :param board: GameBoard from fixture "board"
    :param row: Row of tile to play 0-2
    :param column: Column of tile to play 0-2
    :return: None
    """
    board.play(row=row, column=column)
    try:
        board.play(row=row, column=column)
    except TileNotEmptyException:
        pass
    except Exception:
        assert False
    else:
        assert False
