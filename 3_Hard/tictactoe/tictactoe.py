# tic tac toe
# Difficulty:
# general game of tic tac toe

# Steps:
# 1. start with an empty list to represent the board
# 2. GOAL: add numbers 1 through 9 with every 3 numbers in seperate lists
# 3. create a temporary list
# 4. start a for loop to count from 1 to 9
# 5. add the number into the temp list

# 6. NOTE: every 3 numbers added, the number is divisible by 3
# 7. check to see if the number is divisible by 3
# 8. if it is then append the temp list into the board list
# 9. reset the temp list by assigning it to an empty list

# 10. output the board by going through the entire nested list
# 11. update the end value to " " so that a new line only generates after each 3 number
# 12. NOTE: will have to use this later, so TEST and then convert to a function

# 13. ask the user to pick out a spot with an inputted number
# 14. find that spot that matches the number and replace it with an "X"

# 15. create a turn variable 
# 16. update code to replace the chosen spot with "X" or "O" depending on the turn variable

# 17. NOTE: will use this later, convert to a function
# 18. set the turn as a parameter

# 19. start the game with a for loop that repeats 9 times
# 20. utilize the functions created before and play the game

# 21. start with checking for a win horizontally, check all rows to see if there is a match
# 22. when there is a win stop the outer loop
# 23. NOTE: can only break out of the loop that checks each row
# 24. convert this to a function and utilize return

# 25. add vertical checks and the diagonal checks



board = [] 
temp = [] 
for i in range(1,10): 
  temp.append(i) 
  if i%3 == 0: 
    board.append(temp) 
    temp = [] 

def printBoard():
  for row in range(3): 
    for col in range(3):
      print(board[row][col] , end = " ")
    print()
printBoard()


def updateBoard(turn):
  for row in range(3): 
    for col in range(3):
      if board[row][col] == choice:
        if turn%2 == 0: 
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