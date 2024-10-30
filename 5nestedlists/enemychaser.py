from pprint import pprint
import random
import os
import readchar

grid = []
row = []

for i in range(8):
  row.append(" ")
#generated one row of strings

for j in range(8):
  #appending the SAME row to the grid 8 times
  #you HAVE to recreate the row each time before you append it
  #beacuse when you recreate the row, the data in computer memory will reference it as a DIFFERENT row
  row = []
  for i in range(8):
    row.append("  ")
  grid.append(row)






player = "🥶"
enemy = "👺"
goal = "🥅"

prow = random.randint(0,7)
pcol = random.randint(0,7)

erow = random.randint(0,7)
ecol = random.randint(0,7)

grow = random.randint(0,7)
gcol = random.randint(0,7)

grid[prow][pcol] = player

grid[erow][ecol] = enemy

grid[grow][gcol] = goal

def enemymove():
  global erow, prow, ecol, pcol
  #come up with an algorithm that will move the enemy to a new row and col
  #Rule: the enemy will try to get closer to the player's position
  #enemy's row and col number
  grid[erow][ecol] = "  "
  if prow < erow:
    erow -= 1
  elif pcol < ecol:
    ecol -= 1
  elif prow > erow:
    erow += 1
  elif pcol > ecol:
    ecol += 1
  grid[erow][ecol] = enemy
  
score = 0
      
pprint(grid)

while True:
  k = readchar.readkey()
  grid[prow][pcol] = "  "
  if k == "w":
    prow -= 1
  if k == "s":
    prow += 1
  if k == "a":
    pcol -= 1
  if k == "d":
    pcol += 1
  if grid[prow][pcol] == goal:
    prow = random.randint(0,7)
    pcol = random.randint(0,7)
    grid[erow][ecol] = "  "
    erow = random.randint(0,7)
    ecol = random.randint(0,7)
    grid[grow][gcol] = "  "
    grow = random.randint(0,7)
    gcol = random.randint(0,7)
    
    grid[prow][pcol] = player
  
    grid[erow][ecol] = enemy
  
    grid[grow][gcol] = goal
    score += 1
  grid[prow][pcol] = player
  enemymove()
  if grid[prow][pcol] == enemy:
    break
  os.system("clear")
  pprint(grid)
  print(score)
