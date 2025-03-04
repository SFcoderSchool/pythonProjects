#1 Generate a random number between 1 and 6 to simulate a dice roll

#2 Roll a second dice and sum up their values

#3 Roll until you get a total of 12. Use while True.

#Bonus: track how many attempts to takes to roll 2x 6's

#Bonus: add in a 3rd dice and roll until you get 3x 6's

import random

while True:
  
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  
  print("dice 1:",dice1)
  print("dice 2:",dice2)
  print("total:", dice1+dice2)
  
  if dice1+dice2 == 12:
    break