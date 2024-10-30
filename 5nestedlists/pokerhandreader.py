import random
suits = "♦,♣,♥,♠"
suits = suits.split(",")
chars = "2,3,4,5,6,7,8,9,10,J,Q,K,A"
chars = chars.split(",")
deck = {}
value = 1
s = 1

for char in chars:
  for suit in suits: 
    deck.update({char+suit:[value,char,suit,s]})
    value = value+1
  s = s+1

cards = list(deck.keys())
player_hand = []
dealer_hand = []
random.shuffle(cards)
for i in range(5):
  player_hand.append(cards[0])
  cards.pop(0)
  dealer_hand.append(cards[0])
  cards.pop(0)
bet = int(input("How much do you want to bet?"))
wallet = 0

def match(hand):
  pairs = []
  for i in range(len(hand)):
    pairs.append(deck.get(hand[i])[1])
  pairs.sort()
  dupes = []
  count = 1
  for i in range(len(pairs)-1):
    if pairs[i]==pairs[i+1]:
      count = count+1
    else:
      if count > 1:
        dupes.append(count) 
      count = 1
  if count > 1:
    dupes.append(count)
  return dupes

def flush(hand):
  count = True
  for i in range(len(hand)-1):
    if deck.get(hand[i])[2] != deck.get(hand[i+1])[2]:
      count = False
      break
  return count


def straight(hand):
  same = True
  straight_value = []
  for i in range(len(hand)):
    straight_value.append(deck.get(hand[i])[3])
  straight_value.sort()
  if straight_value == [1,2,3,4,13]:
    return True
  for i in range(len(straight_value)-1):
    if straight_value[i]+1 != straight_value[i+1]:
      same = False
      break
  return same

def result(hand):
  if straight(hand) and flush(hand):
    return ("straight and flush!",1)
  elif 4 in match(hand):
    return ("4 of a kind (HOW???)",2)
  elif 3 in match(hand) and 2 in match(hand):
    return ("FULL HOUSE",3)
  elif flush(hand):
    return ("Flush",4)
  elif straight(hand):
    return ("Ya got a straight.",5)
  elif 3 in match(hand):
    return ("3 of a kind!",6)
  elif match(hand) == [2,2]:
    return ("2 pairs!",7)
  elif match(hand) == [2]:
    return ("1 pair!",8)
  else:
    return ("High card (Nothing)",9)


player = result(player_hand)
dealer = result(dealer_hand)
print("This is player's hand:",player_hand) 
print(result(player_hand)[0])
print("This is dealer's hand:",dealer_hand)
print(result(dealer_hand)[0])

if player[1] < dealer[1]:
  wallet = wallet + bet
  print("Player wins.$",bet,"gained.")
  print("Your bank account:$",wallet)
elif player[1] > dealer[1]:
  print("Dealer wins.$",bet,"stolen")
  wallet = wallet - bet
  print("Your bank account:$",wallet)
else:
  print("Tie")








