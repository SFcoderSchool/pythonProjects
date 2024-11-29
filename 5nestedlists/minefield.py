import random
from pprint import pprint
import readchar
import os

#this is a game where the player has a starting position in the grid
#the player then moves up traversing the 2d list and tries to avoid the mines
#there is only 1 path out
#stepping on a land mine will return the player to the beginning
#💣🌫️

#creating a grid of mines
#BONUS: if your student is more advance feel free to automate this processing by using for loops and append
minegrid = []

for i in range(10):
    row = []
    for j in range(5):
        row.append("💣")
    minegrid.append(row)
# pprint(minegrid)

#now we will open a path allowing the player to run through the mines
column = 2 
#we will start at the middle column index and start clearing the mine field here
for i in range(10):
  minegrid[9-i][column] = "__" #getting rid of the bomb at this index
  #shifting the column index left or right
  column += random.randint(-1,1)
  #preventing the column from going out of bounds
  if column < 0:
    column = 0
  if column > 4:
    column = 4
  

pprint(minegrid)

#now to hide all the bombs by generating a second grid
dirtgrid = []

for i in range(10):
    row = []
    for j in range(5):
        row.append("🟨")
    dirtgrid.append(row)



player = "🧍"
x = 2
y = 9

dirtgrid[y][x] = player
pprint(dirtgrid)

while True:
  movement = k = readchar.readkey()
  #player will always move up one row, the option of left or right is for diagonally up
  if movement == "a":
    #erease the player from curent location, change the yx row&column
    #place the player down in the new yx row&column
    dirtgrid[y][x] = "__"
    x -= 1
    y -= 1
    dirtgrid[y][x] = player
  if movement == "d":
    #erease the player from curent location, change the yx row&column
    #place the player down in the new yx row&column
    dirtgrid[y][x] = "__"
    x += 1
    y -= 1
    dirtgrid[y][x] = player
  if movement == "w":
    #erease the player from curent location, change the yx row&column
    #place the player down in the new yx row&column
    dirtgrid[y][x] = "__"
    y -= 1
    dirtgrid[y][x] = player
  #checking if the player yx row&column is on top of a bomb
  if minegrid[y][x] == "💣":
    #if it is then reveal the bomb in the dirt, reset the player yx postion back to the beginning
    dirtgrid[y][x] = "💣"
    x=2
    y=9
    dirtgrid[y][x] = player
  os.system("cls")
  pprint(dirtgrid)
  #if the y(row) index is at the final row then player wins
  if y == 0:
    print("YOU WIN!")
    break