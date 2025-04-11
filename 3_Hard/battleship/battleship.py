# Battleship
# Difficulty: ⭐⭐⭐⭐
# single player game inspired by the board game battleship

# Steps:
# 1. create the 10 by 10 grid of water
# 2. output the grid neatly
# 3. NOTE: will most likely use this code more later, convert to function

# 4. set the size of a ship to 3
# 5. generate the row and col locations of a ship
# 6. randomly flip a coin to see which direction to ship will grow
# 7. from the original point, travel in the direction chosen for the size of the ship
# 8. NOTE: either travel down or right to avoid index out of bound
# 9. save these locations into a list
# 10. convert this to function when working

# 12. run this function 4 times to generate 4 ships
# 13. save all the coordinated into a list
# 14. print out the list
# 15. NOTE: there will be duplicate coordinates
# 16. update function to run again if there was a duplicate coordinate

# 17. create a list to remember all the coordinates of the ships 
# 18. ask the user for a row
# 19. ask the user for a column
# 20. check to see if the guess was a hit or a miss
# 21. add a while True to repeat
# 22. stop when there are no more ships

import random
import os
grid = []
water = "🌊"
ship = "🚢"
boom = "💥"
miss = "❌"

for i in range(10):
  box = []
  for j in range(10):
    box.append(water)
  grid.append(box)
  
def display():
  print(" ",0,1,2,3,4,5,6,7,8,9)
  for i in range(len(grid)):
    print(i,"".join(grid[i]))  

def make_ship(size):
  match = True
  while match:
    match = False
    ship_location = []

    coin = random.randint(1,2)
    if coin == 1:
      orientation = "vert"
    else:
      orientation = "hori"

    if orientation == "hori":
      row = random.randint(0,len(grid)-size)
      column = random.randint(0,9)
      for i in range(row,row+size):
        ship_location.append([column,i])
    else:
      row = random.randint(0,9)
      column = random.randint(0,len(grid)-size)
      for j in range(column,column+size):
        ship_location.append([j,row])

    for i in range(len(ships)):
      for j in range(size):
        if ships[i] == ship_location[j]:
          match = True
          break

  return ship_location


ships = []
for i in range(1,5):
  ship = make_ship(i)
  for j in range(len(ship)):
    ships.append(ship[j])
print(ships)

display()
while True:
  guess = input("Enter a position between 0 to 9 (row,column)")
  row = int(guess[0])
  col = int(guess[len(guess)-1])

  posi = [row,col]
  if posi in ships:
    grid[row][col] = boom
    ships.remove(posi)
  else:
    grid[row][col] = miss

  os.system("clear")
  display()

  if len(ships) == 0:
    break