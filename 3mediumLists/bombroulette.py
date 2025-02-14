import random

#Based on the hit game "buckshot roulette" a 2 player russian roulette game!
#1: generate a list of bombs either a dud or a real bomb
#2: player decides if they will bomb themselves (russian roulette) or bomb the opponent
#3: you want to throw a bomb at yourself because the duds will heal you
#4: becareful when throwing a bomb at the computer because duds will heal them
#(HINT: there's 3 duds and 3 real bombs in the list, count how many are left before reloading)
#5: computer's turn they make a random choice to bomb themselves or you

#generating an inventory of bombs there are 3 duds and 3 real
bombs = []
for i in range(3):
  bombs.append("dud")
  bombs.append("bomb")
random.shuffle(bombs)
# print(bombs)

playerlives = 4
computerlives = 4



while playerlives>0 and computerlives>0:
  print("Your lives:", playerlives)
  print("Computer lives:", computerlives)
  #player's turn first
  #taking a bomb out of the inventory
  hand = bombs.pop(0)
  choice = input("who will you throw bomb at?")
  #choose to throw at yourself or the computer
  if choice == "self": 
    #checking if it was a real bomb or not
    if hand == "dud":
      print("No damage, you healed yourself!")
      playerlives = playerlives + 1
    else:
      print("You bombed yourself!")
      playerlives = playerlives - 1
  #if you choose to throw it at the computer
  if choice == "computer":
    #checking if it was a real bomb or not
    if hand == "dud":
      print("you threw a dud at the computer, they got healed!")
      computerlives = computerlives + 1
    else:
      print("You bombed the computer!")
      computerlives = computerlives - 1


  #now its the computer's turn
  #taking a bomb out of the inventory
  hand = bombs.pop(0)
  choice = random.randint(1,2)
  #computer randomly decides to throw at you or themselves
  if choice == 1:
    #checking if it was a real bomb or not
    if hand == "dud":
      print("computer threw a dud at themselves, they healed!")
      computerlives = computerlives + 1
    else:
      print("computer bombed themselves lol")
      computerlives = computerlives - 1
  if choice == 2:
    #checking if it was a real bomb or not
    if hand == "bomb":
      print("computer threw a bomb at you!")
      playerlives = playerlives - 1
    else:
      print("computer threw a dud at you! you healed!")
      playerlives = playerlives + 1
    

  #reload when run out of bombs
  if len(bombs) <= 0:
    for i in range(3):
      bombs.append("dud")
      bombs.append("bomb")
    random.shuffle(bombs)
  