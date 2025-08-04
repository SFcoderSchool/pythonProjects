# Blackjack w/ functions
# game of blackjack

# Steps
# - build a list of suits 
# - build a different list of characters 
# - start with an empty list for deck

# - make buildDeck function
# - fill it with all combinations of characters and suits
# - shuffle and print the list

# - create list to save the player cards
# - pass out 2 cards to the player

# - need to know the value of the cards
# - create a function cardValue with 1 parameter (String) to check the incoming string and return the value of the card

# - calculate the score of the player
# - NOTE: will use this code for later, turn into a function

# - repeatedly ask the user if they want to hit or stand
# - if they want to hit then give them a card and continue the loop
# - if the stand then say "they stand" and break

# - create list to save the dealer cards
# - pass out a card to the dealer when player gets a card

# - update calcScore to take a hand as a parameter

# - dealer's turn happens when player has not busted
# - dealer must hit for as long as their total is 16 or less

# - check who wins

# Bonus
# - implement Aces as 11 when calculating the score



import random

deck = []
playerhand = []
computerhand = []

def buildDeck():
  suits = ["♦","♣","♥","♠"]
  characters = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
  for character in characters:
    for suit in suits:
      deck.append(character+suit)
  random.shuffle(deck)

def cardValue(card):
  if card[0] == "K":
    value = 10
  elif card[0] == "Q":
    value = 10
  elif card[0] == "J":
    value = 10
  elif card[0] == "A":
    value = 1
  elif card[0] == "1":
    value = 10
  else:
    value = int(card[0])
  return value

def calcScore(hand):
  total = 0
  for i in range(0, len(hand), 1):
    total = total + cardValue(hand[i])
  return total

def playerTurn():
  while True:
    print(computerhand[0] + "##")
    print(playerhand)

    choice = input("Would you like another card?")
    if choice == "yes":
      c = deck.pop(0)
      playerhand.append(c)

      playerTotal = calcScore(playerhand)
      if playerTotal > 21:
        break
    else:
      break

def computerTurn():
  total = calcScore(computerhand)
  while total < 16:
    c = deck.pop(0)
    computerhand.append(c)
    total = calcScore(computerhand)

def checkWinner(player, computer):
  if player > 21:
    print("Player bust!")
  elif computer > 21:
    print("Computer bust!")
  elif player > computer:
    print("Player wins!")
  elif computer > player:
    print("Computer wins!")
  else:
    print("Tie")



buildDeck()

for i in range(2):
  c = deck.pop(0)
  playerhand.append(c)
  c = deck.pop(0)
  computerhand.append(c)

playerTurn()
playerTotal = calcScore(playerhand)

if playerTotal <= 21:
  computerTurn()

computerTotal = calcScore(computerhand)

print("Player cards",playerhand)
print("Computer cards",computerhand)
checkWinner(playerTotal, computerTotal)