# Tic Tac Toe w/ functions
# create tic tac toe with the use of functions

# Steps:
# - create the 3 rows of the grid as lists and fill them with 3 underscores
# - print out each row
# - NOTE: will use often therefore convert to functions

# - ask the user to input a row, and input a column
# - update the requested row, col underscore with an "X"
# - NOTE: the code is the same for "O", convert code to function and change "X" with a variable as the parameter

# - start setting up the game
# - printboard, makeMove(O), printboard, makeMove(X)
# - after 1 turn is working, add a while True loop

# - create a function called checkWinner
# - write out all the possible wins there are

# - incorporate the win function into the game and stop the loop

# Bonus
# - add a check to only allow valid numbers as inputs (0-2)

row0 = ["_","_","_"]
row1 = ["_","_","_"]
row2 = ["_","_","_"]

def printBoard():
  print(row0)
  print(row1)
  print(row2)


def makeMove(symbol):
  row = input("Which row (0-2)?")
  row = int(row)
  col = input("Which column (0-2)?")
  col = int(col)
  if row == 0:
    row0[col] = symbol
  if row == 1:
    row1[col] = symbol
  if row == 2:
    row2[col] = symbol

####################################################################

def checkWinner():
  if row0[0]==row0[1]==row0[2] != "_":
    return True
  if row1[0]==row1[1]==row1[2] != "_":
    return True
  if row2[0]==row2[1]==row2[2] != "_":
    return True
  if row0[0]==row1[0]==row2[0] != "_":
    return True
  if row0[1]==row1[1]==row2[1] != "_":
    return True
  if row0[2]==row1[2]==row2[2] != "_":
    return True
  if row0[0]==row1[1]==row2[2] != "_":
    return True
  if row0[2]==row1[1]==row2[0] != "_":
    return True
  return False

####################################################################

while True:
  # X's turn
  printBoard()
  makeMove("X")
  if checkWinner()==True:
    print("Player X has won the game!")
    break

  # O's turn
  printBoard()
  makeMove("O")
  if checkWinner()==True:
    print("Player O has won the game!")
    break