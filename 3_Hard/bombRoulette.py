import random

#Please Make Bomb Roulett first before this game!
#This project adds to the original project and modifies it


#generating an inventory of bombs there are 8 duds and 8 real
bombs = []
playerlives = 4
computerlives = 4



def printStats():
  print("Player lives:",playerlives)
  print("Computer lives:",computerlives)
  print("Bombs left:",len(bombs))

def reload():
  print("Reloading....")
  for i in range(3):
    bombs.append("dud")
    bombs.append("bomb")
  random.shuffle(bombs)
  # print(bombs)

def playerMove():
  global playerlives, computerlives, turn
  #taking a bomb out of the inventory
  hand = bombs.pop(0)
  choice = input("who will you throw bomb at?")
  #choose to throw at yourself or the computer
  if choice == "self": 
    #checking if it was a real bomb or not
    if hand == "dud":
      print("It's a dud, you healed")
      playerlives = playerlives + 1
    else:
      print("You bombed yourself!")
      playerlives = playerlives - 1
  #if you choose to throw it at the computer
  if choice == "computer":
    #checking if it was a real bomb or not
    if hand == "dud":
      print("you threw a dud at the computer, they healed")
      computerlives = computerlives + 1
    else:
      print("You bombed the computer!")
      computerlives = computerlives - 1
    turn = "computer"
    #change turns ONLY when throwing it at the opponent

def computerMove():
  global playerlives, computerlives, turn
  #taking a bomb out of the inventory
  hand = bombs.pop(0)
  choice = random.randint(1,2)
  #computer randomly decides to throw at you or themselves
  if choice == 1:
    #checking if it was a real bomb or not
    if hand == "bomb":
      print("computer bombed themselves lol")
      computerlives = computerlives - 1
    else:
      print("computer threw a dud at themselves, they healed")
      computerlives = computerlives + 1
  if choice == 2:
    #checking if it was a real bomb or not
    if hand == "bomb":
      print("computer threw a bomb at you!")
      playerlives = playerlives - 1
    else:
      print("computer threw a dud at you!, you healed!")
      playerlives = playerlives + 1
    turn = "player"
    #change turns ONLY when throwing it at the opponent



while playerlives>0 and computerlives>0:
  if len(bombs) <= 0:
    reload()
  printStats()
  playerMove()
  printStats()
  computerMove()
