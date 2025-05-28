# Monkey Search
# Difficulty:
# find the monkey that is different in the grid

# Steps:
# 1. get the monkey emoji and save it in a variable, get the different monkey emoji and save it in a different variable
# 2. create the board and fill it with a 10x10 grid of monkeys
# 3. NOTE: use the box and truck analogy if needed

# 4. pick a random row and a random column
# 5. use the random row and random column and replace that monkey with the different monkey
# 6. go through each row and display each row

# 7. ask the user to pick a row and a column where they think the different monkey is
# 8. check to see if the user guessed correctly

# Bonus:
# 1. add a timer to see how fast the user found the different monkey
# 2. update code to allow the user to type in numbers 1 - 10 instead of 0 - 9

import random
import time #allow timer
find = "🐵"
hide = "🙊"

board = [] 
for i in range(10): 
  temp = [] 
  for j in range(10): 
    temp.append(hide)
  board.append(temp) 

randcolumn = random.randint(0,9)
randrow = random.randint(0,9)

board[randrow][randcolumn] = find

for i in range(10):
  print("".join(board[i]))

start = time.time()

row = int(input("row: "))
column = int(input("column: "))

stop = time.time()

if column == randcolumn+1 and row == randrow+1:
  print("correct!")
  print( round(stop-start,2) )
else: 
  print("wrong")

