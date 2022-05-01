from gameBoard import GameBoard, TileNotEmptyException


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


def draw_board():
    """
    Prints the game board from the GameBoard model
    :return: None
    """
    global board
    print(' {} | {} | {} '.format(board.columns[0][0], board.columns[1][0], board.columns[2][0]))
    line()
    print(' {} | {} | {} '.format(board.columns[0][1], board.columns[1][1], board.columns[2][1]))
    line()
    print(' {} | {} | {} '.format(board.columns[0][2], board.columns[1][2], board.columns[2][2]))


board = GameBoard()
running = True
while running:
    cls()
    draw_board()
    print(f"Turn no. {board.turn+1}")
    print(f"{board.active_player}'s turn")
    input_invalid = True
    while input_invalid:
        column = input("column: ")
        row = input("row: ")
        try:
            c = int(column)
            r = int(row)
            board.play(row=r, column=c)
        except TileNotEmptyException:
            print("This tile is not empty")
        except Exception as e:
            print(e)
        else:
            input_invalid = False
    running = not board.game_is_over

cls()
draw_board()
print(board.result)
