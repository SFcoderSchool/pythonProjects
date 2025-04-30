# Minefield
# Difficulty:⭐⭐⭐⭐★★★★★★
# Traverse through the field, advance every round by either going left, right, or straight

# Steps
# 1. generate the 10x5 grid filled with bombs
# 2. print out the grid of bombs neatly
# 3. NOTE: will most likely use this set of instructions later on, turn into function
# 4. starting at the last list, in the middle, clear a path to the first list for the user
# 5. NOTE: don't go out of bounds
# 6. create a separate grid filled with covers
# 7. print out the grid of covers to cover the bombs with dirt
# 8. NOTE: instructions will look the same as printing out the bombs, update function to accept a parameter
# 9. make the player emoji
# 10. keep track of the position fo the player
# 11. use readchar to accept key inputs a, w, d
# 12. advance the player depending on the input
# 13. replace the current spot back to blank
# 14. put the new player into the new spot it advanced into
# 15. check to see if player ran into a bomb, if they did reset the player
# 16. add a while True loop to repeat the game
# 17. stop the game when user reaches the end


import random
import readchar
import os


minegrid = []

for i in range(10):
  row = []
  for j in range(5):
      row.append("💣")
  minegrid.append(row)

def printGrid(grid):
  for i in range(len(grid)):
    print(" ".join(grid[i]))

printGrid(minegrid)

column = 2 
for i in range(10):
  minegrid[9-i][column] = "⬜" 
  column += random.randint(-1,1)
  if column < 0:
    column = 0
  if column > 4:
    column = 4
  
printGrid(minegrid)


dirtgrid = []
for i in range(10):
  row = []
  for j in range(5):
      row.append("🟨")
  dirtgrid.append(row)



player = "🧍"
col = 2
row = 9

dirtgrid[row][col] = player
printGrid(dirtgrid)

while True:
  k = readchar.readkey()
  if k == "a":
    dirtgrid[row][col] = "⬜"
    col -= 1
    row -= 1
    dirtgrid[row][col] = player
  if k == "d":
    dirtgrid[row][col] = "⬜"
    col += 1
    row -= 1
    dirtgrid[row][col] = player
  if k == "w":
    dirtgrid[row][col] = "⬜"
    row -= 1
    dirtgrid[row][col] = player
  if minegrid[row][col] == "💣":
    dirtgrid[row][col] = "💣"
    col=2
    row=9
    dirtgrid[row][col] = player
  os.system("clear || cls")
  printGrid(dirtgrid)
  if row == 0:
    print("YOU WIN!")
    break