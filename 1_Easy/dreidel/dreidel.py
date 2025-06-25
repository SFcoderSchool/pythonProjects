# Dreidel
# Difficulty: ⭐
# Pay a coin and spin the top and 
# depending on what the top lands on,
# do the action depending on the rules
# Lose all your coins and its game over

# Rules
# Nun - receive nothing
# Gimel - receive all coins from the table
# Hay - receive half the coins from the table
# Shin - put a coin to the table

# Steps
# 1. give player and computer 10 coins and table should have 0 coins

# 2. both player and computer will pay the coin and put it in the table
# 3. use input() to pause the script 

# 4. randomly select a number from 1 to 4 for the dreidel
# 5. output a word from the rules for each possible random number

# 6. depending on the rules, do the action for each word

# 7. use input() to pause the script
# 8. repeat the dreidel spin for the computer

# 9. output the current amount of coins of player, computer, and table

# 10. add a while True to repeat the game (steps 4 to 9)
# 11. stop the game when someone has reached 0 or less coins

import random
#both players start with 10 coins
player = 10
computer = 10
table = 0

while True:
  #both players put a coin on the table
  player = player - 1
  computer = computer - 1
  table = table + 2

  #player spins the dreidel
  input("Press enter to spin the dreidel!")
  dreidel = random.randint(1,4)
  if dreidel == 1:
    print("nun, you get nothing")
  elif dreidel == 2:
    print("gimel, you get all coins on table")
    player = player + table
    table = 0
  elif dreidel == 3:
    print("hay, you get half the coins on the table")
    reward = table/2
    reward = int(reward)
    player = player + reward
    table = table - reward
  elif dreidel == 4:
    print("shin, you lose 1 coin")
    player = player - 1
    table = table + 1

  #computer spins the dreidel
  input("Computer's turn to spin the dreidel!")
  dreidel = random.randint(1,4)
  if dreidel == 1:
    print("nun, computer get nothing")
  elif dreidel == 2:
    print("gimel, computer get all coins on table")
    computer = computer + table
    table = 0
  elif dreidel == 3:
    print("hay, computer get half the coins on the table")
    reward = int(table/2)
    computer = computer + reward
    table = table - reward
  elif dreidel == 4:
    print("shin, computer lose 1 coin")
    computer = computer - 1
    table = table + 1
    
  print("your coins", player)
  print("computer coins", computer)
  if player <= 0:
    break
  elif computer <= 0:
    break