import random

#Based on the hit game "buckshot roulette" a 2 player russian roulette game!
#1: generate a list of bombs either a dud or a real bomb
#2: player decides if they will bomb themselves (russian roulette) or bomb the opponent
#3: turn does not pass when choosing to bomb yourself
#  -turn goes to the opponent when you choose to bomb them regardless if it is a dud or real bomb
#4: change turn to the opponent when choosing to bomb them
#5: computer's turn they make a random choice to bomb themselves or you

#generating an inventory of bombs there are 8 duds and 8 real
bombs = []
for i in range(3):
  bombs.append("dud")
  bombs.append("bomb")
random.shuffle(bombs)
# print(bombs)

playerlives = 4
computerlives = 4

#whos turn it is, player goes first
turn = "player"

while playerlives>0 and computerlives>0:
  print("Your lives:", playerlives)
  print("Computer lives:", computerlives)
  #if your turn
  if turn == "player":
    #taking a bomb out of the inventory
    bomb = bombs.pop(0)
    choice = input("who will you throw bomb at?")
    #choose to throw at yourself or the computer
    if choice == "self": 
      #checking if it was a real bomb or not
      if bomb == "dud":
        print("No damage, you are fine")
      else:
        print("You bombed yourself!")
        playerlives = playerlives - 1
    #if you choose to throw it at the computer
    if choice == "computer":
      #checking if it was a real bomb or not
      if bomb == "dud":
        print("you threw a dud at the computer")
      else:
        print("You bombed the computer!")
        computerlives = computerlives - 1
      turn = "computer"
      #change turns ONLY when throwing it at the opponent

  #when the computer's turn
  if turn == "computer":
    #taking a bomb out of the inventory
    bomb = bombs.pop(0)
    choice = random.randint(1,2)
    #computer randomly decides to throw at you or themselves
    if choice == 1:
      #checking if it was a real bomb or not
      if bomb == "dud":
        print("computer threw a dud at themselves")
      else:
        print("computer bombed themselves lol")
        computerlives = computerlives - 1
    if choice == 2:
      #checking if it was a real bomb or not
      if bomb == "dud":
        print("computer threw a dud at you!")
      if bomb == "bomb":
        print("computer threw a bomb at you!")
        playerlives = playerlives - 1
      turn = "player"
      #change turns ONLY when throwing it at the opponent
  #reload when run out of bombs
  if len(bombs) < 2:
    for i in range(3):
      bombs.append("dud")
      bombs.append("bomb")
    random.shuffle(bombs)
  