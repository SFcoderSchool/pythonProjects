# Monkey Search
# Difficulty:
# find the monkey that is different in the grid

# Steps:
# 1. get the monkey emoji and save it in a variable, get the different monkey emoji and save it in a different variable
# 2. create the board and fill it with a 10x10 grid of monkeys


#1 get the emojis and store in a easy to use variable. (easier than copy and paste)
#2 setup board
#example explained: grab a empty box > fill with items > move box to cargo truck
#3 switch a monkey out randomly
#4 display board
#5 allow user to type in the position and check if correct
#reminder: first index is going down and second index is going right
#6 what if we want to count 1-10 instead of 0-9? add 1 to randcolumn and randrow in the if statement
#7 set timer

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
column = int(input("column: "))
row = int(input("row: "))
stop = time.time()

if column == randcolumn+1 and row == randrow+1:
  print("correct!")
  print( round(stop-start,2) )
else: 
  print("wrong")

