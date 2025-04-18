# Card Showdown
# Difficulty: ⭐⭐⭐⭐
# given a 5 card hand, play card to showdown against the opponent

# Steps:
# 1. create the suits list from diamond to spade
# 2. create the dictionary to store all the cards where the card with the suit is the key and the value is the power

# 3. go through each number from 2 to 14 for each suit and print out each card

# 4. create a variable to represent power and assign each card to their respective power

# 5. create the deck from all the keys from the dictionary
# 6. NOTE: the dict.keys() function is not a list; need to convert to a list
# 7. shuffle the deck

# 8. create the list for player's hand and computer's hand
# 9. pass out 5 cards to each list

# 10. output the player's hand and ask them which card they would like to use
# 11. remove that card from the player's hand and output it
# 12. NOTE: convert to a function to organize code and return the output

# 13. computer picks a random card from their hand and remove it and output it
# 14. NOTE: convert to a function to organize code and return the output

# 15. lookup the power of each card and save it in a variable
# 16. check to see who wins and output result

# 17. add a loop and repeat for all cards in the hand

# 18. add a scoring system
# 19. output who wins based off of the final scores




import random

suits = ["♦", "♣", "♥", "♠"]

cards = {}
power = 0
for num in range(2,15):
  for s in range(4):
    cardname = str(num)+suits[s]
    if num == 11:
      cardname = "J"+suits[s]
    if num == 12:
      cardname = "Q"+suits[s]
    if num == 13:
      cardname = "K"+suits[s]
    if num == 14:
      cardname = "A"+suits[s]
    cards[cardname] = power
    power += 1


deck = cards.keys()
deck = list(deck)

random.shuffle(deck)

playercards = []
computercards = []
for i in range(5):
  playercards.append(deck.pop(0))
  computercards.append(deck.pop(0))


def pickPlayerCard():
  print(playercards)
  num = input("Which card index do you play?")
  num = int(num)
  return(playercards.pop(num))

def pickComputerCard():
  num = random.randint(0, len(computercards) - 1)
  return(computercards.pop(num))

playerscore = 0
computerscore = 0
for i in range(5):
  pCard = pickPlayerCard()
  cCard = pickComputerCard()
  print(cCard)
  
  pCardPower = cards[pCard]
  cCardPower = cards[cCard]
  
  if pCardPower > cCardPower:
    playerscore += 1
    print("Player beats computer.")
  elif cCardPower > pCardPower:
    computerscore += 1
    print("Computer beats player.")
  else:
    print("Tie")

if playerscore > computerscore:
  print("Player wins!")
elif computerscore > playerscore:
  print("Computer wins!")
else:
  print("Tie")