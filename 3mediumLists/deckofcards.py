# METHOD 1 BUILD LIST MANUALLY
suits = ["♦","♣","♥","♠"]
characters = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]



## METHOD 2 BUILD LIST WITH FUNCTIONS AND CONVERTING STRINGS
# suits="♦♣♥♠" 
# characters="A23456789JQK"
# suits = list(suits)
# characters = list(characters)
# characters.insert(9,"10")


#BUILD DECK TO PLACE CARDS AFTER COMBINATIONS
deck = []


##METHOD 1 LOOP METHOD WITH RANGE FUNCTION
# for character in range(len(characters)):
#   for suit in range(len(suits)):
#     deck.append(characters[character] + suits[suit])
# print(deck)

#METHOD 2 LOOP METHOD WITHOUT RANGE FUNCTION
for character in characters:
  for suit in suits:
    deck.append(character+suit)
print(deck)


#randomize cards
import random
random.shuffle(deck)
print(deck)
