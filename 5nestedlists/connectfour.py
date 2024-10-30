import os
from termcolor import colored
board = [
  [0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0]
]
win = False
def printBoard():
  for row in range(6):
    for column in range(7):
      #optional coloring; can just print(board[row][column]) instead
      #***********************************************
      if board[row][column] == 'x':
        print(colored(board[row][column],'magenta', attrs=['bold']), end=" ")
      elif board[row][column] == 'o':
        print(colored(board[row][column],'blue', attrs=['bold']), end=" ")
      else:
        print(colored(board[row][column],"red"), end=" ")
      #***********************************************
    print()
  #print col number
  for i in range(1,8):
    print(colored(i,'red'), end=" ")
  print("\n")
def turn(player, playerTurn):
  #-1 b/c needs to be in bounds of list (list indexs from 0-6 not 1-7)
  playerTurn = playerTurn -1
  #assume column is full
  columnFull = True
  for row in range(5,-1,-1):
    #if we find a 0 in the column, then we say the column is not full and place the x/o
    if board[row][playerTurn] == 0:
      board[row][playerTurn] = player
      columnFull = False
      break
#optional
#*******************************************
  if columnFull == True:
    playerTurn = int(input('this column is already full, try another number from 1-7 \n'))
    while playerTurn < 1 or playerTurn > 7:
      playerTurn = int(input('give me a number between the range 1-7 \n'))
    turn(player,playerTurn)
  #*******************************************
      
def winChecker():
  #horizontal check
  for row in range(6):
    for column in range(4):
      if board[row][column] == board[row][column+1] == board[row][column+2] == board[row][column+3] and board[row][column] != 0:
        return board[row][column]
  #vertical check
  for row in range(3):
    for column in range(7):
      if board[row][column] == board[row+1][column] == board[row+2][column] == board[row+3][column] and board[row][column] != 0:
        return board[row][column]
  #diagonal check for \, restricting ranges to check when diagonals are in bounds
  for row in range(2,-1,-1):
    for column in range(3,-1,-1):
      if board[row][column] == board[row+1][column+1] == board[row+2][column+2] == board[row+3][column+3] and board[row][column] !=0:
        return board[row][column]
  #diagonal check for /, restricting ranges to check when diagonals are in bounds
  for row in range(5,2,-1):
    for column in range(4):
      if board[row][column] == board[row-1][column+1] == board[row-2][column+2] == board[row-3][column+3] and board[row][column] !=0:
        return board[row][column]

#only 42 possible turns        
for i in range(42):
  printBoard()
  player = ""
  if i%2==0:
    player = 'x'
  else:
    player='o'
  playerTurn=int(input("It's " + player + "'s turn! Input a number between 1-7 \n"))
  #optional
  #***********************************************
  while playerTurn < 1 or playerTurn > 7:
    print("number between 1 to 7 please")
    playerTurn=int(input("It's " + player + "'s turn! Input a number between 1-7 \n"))
  #***********************************************
  turn(player, playerTurn) 
  win = winChecker()
  if win != None:
    os.system('clear')
    printBoard()
    print(str(win) + " wins!")
    break
  os.system('clear')
else:
  printBoard()
  print("It's a draw!")