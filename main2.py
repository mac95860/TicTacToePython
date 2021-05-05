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
  global game_is_still_going
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  if row_1 or row_2 or row_3:
    game_is_still_going = False
  
  #return the winner (X or O)
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]

def check_columns():
  global game_is_still_going
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[9] != "-"
  if column_1 or column_2 or column_3:
    game_is_still_going = False
  
  #return the winner (X or O)
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]

def check_diagonals():
  global game_is_still_going
  diagonal_1 = board[0] == board[4] == board[9] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"

  if diagonal_1 or diagonal_2:
    game_is_still_going = False
  
  #return the winner (X or O)
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[1]
  

def check_if_tie():
  return

def flip_player():
  return

play_game()