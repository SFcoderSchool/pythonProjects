import random 
from pprint import pprint
import os
import readchar

Steve = "🧍"
player_row = 0
player_col = 0
lava = "🌋"

def generateGrid(length, width):
  brown_emoji = "🟫"
  grid = []
  
  for i in range(length):
    row = []
    for i in range(width):
      row.append(brown_emoji)
    grid.append(row)

  amount = int(length/6 * width/6)
  for i in range(amount):
    skbidi_rizz = random.randint(0, width -1)
    fantum_tax = random.randint(0, length -1)
    grid[fantum_tax][skbidi_rizz] = "💎" 
    grid[fantum_tax -1][skbidi_rizz] = "💎"
    grid[fantum_tax][skbidi_rizz-1] = "💎" 
    grid[fantum_tax-1][skbidi_rizz-1] = "💎" 
  #put 5 lava at random places
  for i in range(5):
    one = random.randint(0,width -1)
    two = random.randint(0, length -1)
    grid[two][one] = lava
    grid[two][one-1] = lava
    grid[two][one+1] = lava
    
  grid[0][0] = Steve
  return grid

wall= generateGrid(20,10)
inventory = 0
#write a function called mineDiamond 
#the function will ask you to input a row and column number asking you where to mine
#the place you mine on the grid will be replaced with "  "

def mineDiamond():
  global inventory
  row = int(input("Give me a integer between 0, 19: "))
  col = int(input("Give me a integer between 0, 9: "))
  if wall[row][col] == "💎":
    print("U found the diamond. ")
    inventory = inventory+1
  wall[row][col] = "  "

def move_player():
  global player_row, player_col
  k = readchar.readkey()
  wall[player_row][player_col] = "  "
  if k == "d":
    player_col = player_col + 1
  if k == "a":
    player_col = player_col - 1
  if k == "s":
    player_row = player_row + 1
  if wall[player_row][player_col] == lava:
    exit()
  wall[player_row][player_col] = Steve



while True:
  os.system('clear')
  pprint(wall)
  move_player()
  