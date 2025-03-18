#1 Build board

board = [] #main board
temp = [] #list of 3 numbers to insert into board
for i in range(1,10): #generate numbers 1-9
  temp.append(i) #adds number into temp list
  if i%3 == 0: #if 3 6 or 9
    board.append(temp) #take completed list of 3 values and move into board
    temp = [] #clear temp list for 3 new numbers

####################################################################

#2 Build function to display board, because data are integers, you cannot use "".join()
#good idea to keep as integer to get better understanding on data relations
def printBoard():
  for row in range(3): 
    for col in range(3):
      print(board[row][col] , end = " ")
    print()
printBoard()

####################################################################

#3 Allow user to pick a number. Reminder: numbers on board are integers
# choice = int(input("choose a position: "))

####################################################################

#4 build a function to switch chosen position into "X"
# def updateBoard():
#   for row in range(3): 
#     for col in range(3):
#      if board[row][col] == choice:
#        board[row][col] = "X"
#   printBoard()

####################################################################

#5 setup loop for up to 9 turns
# for turn in range(9):
#   choice = int(input("choose a position: "))
#   updateBoard()
  #Why do i only have "X"??

####################################################################

#6 update updateBoard function to take in turn parameter to decide if change should be X or O
# def updateBoard(turn):
#   for row in range(3): 
#     for col in range(3):
#       if board[row][col] == choice:
#         if turn%2 == 0: #odd vs even turn
#           board[row][col] = "X"
#         else:
#           board[row][col] = "O"
#   printBoard()

# for turn in range(9):
#   choice = int(input("choose a position: "))
#   updateBoard(turn)

####################################################################

#7 build functions to check for winner
#VERTICAL 147 259 369


def updateBoard(turn):
  for row in range(3): 
    for col in range(3):
      if board[row][col] == choice:
        if turn%2 == 0: #odd vs even turn
          board[row][col] = "X"
        else:
          board[row][col] = "O"
  printBoard()

def winChecker():
  #VERTICAL
  for i in range(3):
    if board[0][i] == board[1][i] == board[2][i]:
      return board[0][i] #returns winner
  #HORIZONTAL
  for i in range(3):
    if board[i][0] == board[i][1] == board[i][2]:
      return board[i][0] #returns winner
  #DIAGONAL L TO R
  if board[0][0] == board[1][1] == board[2][2]:
    return board[0][0]
  #DIAGONAL R TO L
  if board[0][2] == board[1][1] == board[2][0]:
    return board[0][2]



for turn in range(9):
  choice = int(input("choose a position: "))
  updateBoard(turn)
  result = winChecker()
  if result:
    print(result, "wins")
    break