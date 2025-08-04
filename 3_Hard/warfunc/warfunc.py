# War w/ functions
# card game war

# Steps
# - build a list of suits 
# - build a different list of characters 
# - start with an empty list for deck

# - make buildDeck function
# - fill it with all combinations of characters and suits
# - shuffle and print the list

# - simulate a card draw for the player and remove the top of the list
# - do the same for the computer

# - attempt to compare the 2 cards to see which is bigger
# - NOTE: need to process the data before comparing

# - create a function cardValue with 1 parameter (String) to check the incoming string and return the value of the card

# - use the cardValue function to check the 2 cards then check to see who has the bigger card
# - if the cards are the same then initiate war

# - War function
#   - burn 3 cards and redraw for player/cpu
#   - create T/F variable to while loop war and start False
#   - while war switch to True
#   - duplicate play code under else war
#   - if either player wins, switch war to False to stop while loop

# Bonus:
# - add a loop to keep the game going
# - reload the deck when there are no more cards
# - keep track of won cards for player and computer


import random

deck = []
def buildDeck():
  suits = ["♦","♣","♥","♠"]
  characters = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
  for character in characters:
    for suit in suits:
      deck.append(character+suit)
  random.shuffle(deck)

def cardValue(card):
  if card[0] == "K":
    value = 13
  elif card[0] == "Q":
    value = 12
  elif card[0] == "J":
    value = 11
  elif card[0] == "A":
    value = 14
  elif card[0] == "1":
    value = 10
  else:
    value = int(card[0])
  return value

def war():
  for i in range(0,3,1):
    deck.pop(0)
  player = deck.pop(0)
  cpu = deck.pop(0)

  print("player:", player)
  print("cpu:", cpu)

  playerValue = cardValue(player)
  cpuValue = cardValue(cpu)
  if cpuValue > playerValue:
    print("cpu wins")
    return False
  elif cpuValue < playerValue:
    print("player wins")
    return False
  else:
    print("war")
    return True
  

buildDeck()

player = deck.pop(0)
cpu = deck.pop(0)

print("player:", player)
print("cpu:", cpu)

playerValue = cardValue(player)
cpuValue = cardValue(cpu)
if cpuValue > playerValue:
  print("cpu wins")
elif cpuValue < playerValue:
  print("player wins")
else:
  print("war")
  warStart = True
  while warStart == True:
    warStart = war()

