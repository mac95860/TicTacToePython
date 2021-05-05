board = ['-','-','-','-','-','-','-','-','-']

def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])

#If game is still going
game_is_still_going = True

#Who won? Or tie?
winner = None

#Who's turn is it?
current_player = "X"

def play_game():
  # display initial game board
  display_board()

  while game_is_still_going:
    handle_turn(current_player)
    check_if_game_over()
    flip_player()
  # The game has ended
  if winner == "X" or winner == "0":
    print(winner + " won.")
  elif winner == "None":
    print("tie")

# handle turn of arbitary player
def handle_turn(player):
  position = input("Choose a position from 1-9: ")
  position = int(position) - 1
  board[position] = "X"
  display_board()

def check_if_game_over():
  check_if_win()
  check_if_tie()

def check_if_win():
  global winner
  #check rows
  row_winner = check_rows()
  #check columns
  column_winner = check_columns()
  #Check diagonals
  diagonal_winner = check_diagonals()
  if row_winner:
    #there was a winne
    winner = row_winner()
  elif diagonal_winner:
    #there was a winner
    winner = diagonal_winner()
  elif column_winner:
    #there was a winner
    winner = column_winner()
  else:
    #there was no winners
    winner = "None"
    return

def check_rows():
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  return

def check_columns():
  return

def check_diagonals():
  return

def check_if_tie():
  return

def flip_player():
  return

play_game()