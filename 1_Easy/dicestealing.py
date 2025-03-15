import random

#both players start with 6 coins
#they will then roll dices to see how much to steal from the opponent
playercoins = 6
computercoins = 6
print(playercoins)
print(computercoins)

while True:
  input("Press enter to roll the dice!")
  #player rolls the dice
  dice = random.randint(1,6)
  print("Player Dice roll:", dice)
  #add that amount to the player, subtract it from the computer
  playercoins = playercoins + dice
  computercoins = computercoins - dice
  print(playercoins)
  print(computercoins)
  #computer's turn to roll the dice
  dice = random.randint(1,6)
  print("Player Dice roll:", dice)
  computercoins = computercoins + dice
  playercoins = playercoins - dice
  print(playercoins)
  print(computercoins)
  #game ends when either player or computer runs out of coins
  if playercoins <= 0:
    print("Player ran out of coins, you lose!")
    break
  if computercoins <= 0:
    print("Computer ran out of coins, you win!")
    break
  