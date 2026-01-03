# Ladder and Snakes
import random
from pprint import pprint
import os
import time

player_y = 19
player_x = 0
player = "🐥"
ladder = "🪜 "
snake = "🐍"
grid = []
grid2 = []
tile = "🟫"
enemy = "💀"
enemy_y= 19
enemy_x = 0

def copyGrid(grid):
  new_grid = []
  for i in range(len(grid)):
    new_grid.append([])
    for j in range(len(grid[i])):
      new_grid[i].append(grid[i][j])
  return new_grid

def generateGrid(length, width):
  global grid, grid2
  grid = []
  for i in range(20):
    row = []
    for j in range(width):
      row.append(tile)
    grid.append(row)

  for i in range(18):
    row = random.randint(0,19)
    column = random.randint(0,19)
    
    grid[row][column] = ladder
    
  for i in range(15):
    snakerow = random.randint(0,18)
    snakecolumn = random.randint(0,19)

    grid[snakerow][snakecolumn] = snake
  grid2 = copyGrid(grid)
  grid[player_y][player_x] = player
          
generateGrid(20,20)

def printGrid():
  os.system("clear")
  for z in range(20):
    print("".join(grid[z]))

printGrid()

def player_move():
  global player_y, player_x
  dice = random.randint(1,6)
  for i in range(dice):
    grid[player_y][player_x] = grid2[player_y][player_x]
    if player_y % 2 == 0: 
      player_x = player_x - 1
    if player_y % 2 == 1:
      player_x = player_x +1
    
    if player_x > 19:
      player_x = 19
      player_y = player_y - 1
      
    if player_x < 0:
      player_x = 0
      player_y = player_y - 1
    grid[player_y][player_x] = player
    time.sleep(0.000000001)
    printGrid()

    if player_y == 0 and player_x == 0:
      print("Player1 won! ")
      quit()
      
  if grid2[player_y][player_x] == ladder:
    grid[player_y][player_x] = grid2[player_y][player_x]
    player_y = player_y - 1
    grid[player_y][player_x] = player
    
  if grid2[player_y][player_x] == snake:
    grid[player_y][player_x] = grid2[player_y][player_x]
    player_y = player_y + 1
    grid[player_y][player_x] = player
     

def enemymove():
  global enemy_y, enemy_x
  dice = random.randint(1, 6)
  for i in range(dice):
    grid[enemy_y][enemy_x] = grid2[enemy_y][enemy_x]
    if enemy_y % 2 == 0:
      enemy_x = enemy_x - 1
      
    if enemy_y % 2 == 1:
      enemy_x = enemy_x + 1
      
    if enemy_x > 19:
      enemy_x = 19
      enemy_y = enemy_y - 1

    if enemy_x < 0:
      enemy_x = 0
      enemy_y = enemy_y - 1
    grid[enemy_y][enemy_x] = enemy
    time.sleep(0.00000001)
    printGrid()
    
    if enemy_y == 0 and enemy_x == 0:
      print("Player2 won! ")
      quit()
      
  if grid2[enemy_y][enemy_x] == ladder:
    grid[enemy_y][enemy_x] = grid2[enemy_y][enemy_x]
    enemy_y = enemy_y -1
    grid[enemy_y][enemy_x] = enemy

  if grid2[enemy_y][enemy_x] == snake:
    grid[enemy_y][enemy_x] = grid2[enemy_y][enemy_x]
    enemy_y = enemy_y + 1
    grid[enemy_y][enemy_x] = enemy
    
while True:
  input("Player1: Press enter to roll your dice ")
  player_move()
  printGrid()
  input("Player2: Press enter to roll your dice ")
  enemymove()
  printGrid()