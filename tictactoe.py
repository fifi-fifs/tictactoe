def ttt_layout(table):
  """
  Sets out the table on the screen 
  and 
  changes in the state accordingly
  """
  
  for row in table:
    print("|", end="")
    for cell in row:
      print(cell, end="|")
    print()

def check_winner(table):
  """Checks if a player has won the game."""
  # Check rows
  for row in table:
    if row[0] == row[1] == row[2] and row[0] != " ":
      return row[0]
  # Check columns
  for col in range(3):
    if table[0][col] == table[1][col] == table[2][col] and table[0][col] != " ":
      return table[0][col]
  # Check diagonals
  if table[0][0] == table[1][1] == table[2][2] and table[0][0] != " ":
    return table[0][0]
  if table[0][2] == table[1][1] == table[2][0] and table[0][2] != " ":
    return table[0][2]
  # No winner
  return None

def play_tic_tac_toe():  

  """Plays a game of Tic Tac Toe."""
  table = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
  current_player = "X"
  while True:
    ttt_layout(table)
    row = int(input(f"Player {current_player}, enter the row number (1-3): ")) - 1
    col = int(input(f"Player {current_player}, enter the column number (1-3):  ")) - 1
    if table[row][col] != " ":
      print("That space is already taken!")
      continue
    table[row][col] = current_player
    winner = check_winner(table)
    if winner:
      ttt_layout(table)
      print(f"Player {winner} has won!")
      break
    if all(all(cell != " " for cell in row) for row in table):
      ttt_layout(table)
      print("It's a tie!")
      break
    current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
  play_tic_tac_toe()   