import random

score = 0

while True:
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  dice3 = random.randint(1,6)
  print("Your dices:", dice1, dice2, dice3)
  playertotal = dice1 + dice2 + dice3
  
  cdice1 = random.randint(1,6)
  cdice2 = random.randint(1,6)
  cdice3 = random.randint(1,6)
  computertotal = cdice1 + cdice2 + cdice3
  
  #decide who wins
  choice = input("who wins, higher or lower?")
  print("Computer dices:", cdice1, cdice2, cdice3)
  
  #the person with the higher total wins
  if choice == "higher":
    if playertotal > computertotal:
      print("you win")
      score = score + 1
    else:
      print("you lose")
      score = score - 1
  
  #the person with the lower total wins
  if choice == "lower":
    if playertotal < computertotal:
      print("you win")
      score = score + 1
    else:
      print("you lose")
      score = score - 1

  print("Score:",score)
  
  