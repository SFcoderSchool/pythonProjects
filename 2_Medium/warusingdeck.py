#1 build a list of suits 
#2 build a list of characters 
#3 assemble and store in a list 
#4 shuffle cards
#5 draw card for player and cpu>= then remove card from deck after draw
#6 read only first character of card 
#7 assign numerical value to first substring so we can compare
#8 special cases first: J Q K A 10(2 character instead of 1)
#9 check if win lose or war
#10 war: burn 3 cards and redraw for player/cpu
  #create T/F variable to while loop war and start False
  #if war switch to True
  #duplicate play code under else war
  #if either player wins, switch war to False to stop while loop


import random

suits = ["♦","♣","♥","♠"]
characters = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

deck = []

for character in characters:
  for suit in suits:
    deck.append(character+suit)

random.shuffle(deck)

war = False
player = deck[0]
deck.pop(0)

cpu = deck[0]
deck.pop(0)

print("player:", player)
print("cpu:", cpu)

if player[0] == "K":
  playerValue = 13
elif player[0] == "Q":
  playerValue = 12
elif player[0] == "J":
  playerValue = 11
elif player[0] == "A":
  playerValue = 14
elif player[0] == "1":
  playerValue = 10
else:
  playerValue = int(player[0])

if cpu[0] == "K":
  cpuValue = 13
elif cpu[0] == "Q":
  cpuValue = 12
elif cpu[0] == "J":
  cpuValue = 11
elif cpu[0] == "A":
  cpuValue = 14
elif cpu[0] == "1":
  cpuValue = 10
else:
  cpuValue = int(cpu[0])


if cpuValue > playerValue:
  print("cpu wins")
elif cpuValue < playerValue:
  print("cpu wins")
else:
  print("war")
  war = True
  while war:
    player = deck[0]
    deck.pop(0)

    cpu = deck[0]
    deck.pop(0)

    print("player:", player)
    print("cpu:", cpu)

    if player[0] == "K":
      playerValue = 13
    elif player[0] == "Q":
      playerValue = 12
    elif player[0] == "J":
      playerValue = 11
    elif player[0] == "A":
      playerValue = 14
    elif player[0] == "1":
      playerValue = 10
    else:
      playerValue = int(player[0])

    if cpu[0] == "K":
      cpuValue = 13
    elif cpu[0] == "Q":
      cpuValue = 12
    elif cpu[0] == "J":
      cpuValue = 11
    elif cpu[0] == "A":
      cpuValue = 14
    elif cpu[0] == "1":
      cpuValue = 10
    else:
      cpuValue = int(cpu[0])


    if cpuValue > playerValue:
      print("cpu wins")
      war = False
    elif cpuValue < playerValue:
      print("cpu wins")
      war = False
    else:
      print("war")
    