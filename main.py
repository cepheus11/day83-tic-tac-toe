def cls():
    """
    Clear the screen
    :return: None
    """
    print("\033[H\033[2J", end="")


def line():
    """
    Print one horizontal line of the game board
    :return: None
    """
    print('-----------')


def grid_lines():
    """
    Print one empty grid line of the game board (3x1 tiles)
    :return: None
    """
    print('   |   |   ')


def draw_board():
    """
    Prints the game board (3x3 tiles)
    :return: None
    """
    grid_lines()
    line()
    grid_lines()
    line()
    grid_lines()


PLAYERS = ['X', 'O']
active_player = PLAYERS[0]
turn = 0
running = True
while running:
    cls()
    draw_board()
    print(f"{active_player}'s turn")
    row_col = input("row (1-3), column (1-3): ")
    coords = tuple(int(x) for x in row_col.split(','))
    turn += 1
    print(turn)
    active_player = PLAYERS[turn % 2]
