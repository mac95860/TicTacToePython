# board
# play game
    # handle turn
# display board
# change players
# check win
    # check rows
    # check columns
    # check diagonals
    # check draw

board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

# displays initial game board
def display_board() :
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def handle_turn():
    position = input("Choose a position from 1-9: ")
    position = int(position) - 1
    board[position] = "X"
    display_board()

def play_game():
    display_board()
    handle_turn()

play_game()
