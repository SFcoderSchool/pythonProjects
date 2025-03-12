import random

#a player starts with 2 cards in the game of blackjack
#the value of the card can be 1(A) up to 10(face cards)
card1 = random.randint(1,10)
card2 = random.randint(1,10)
#the player's usually do mental math to calculate the total but we will rely on the computer to calcualte total
total = card1 + card2

print(card1, card2)
print("Total:", total)

#continuously ask if they want an additional card
while True:
  choice = input("do you want a card? ")
  #if input is yes then generate a random number to represent a random card and add it to the total
  if choice == "yes":
    card3 = random.randint(1,10)
    total = total + card3
    print(card3)
    print("Total:",total)
  #if input is no then stop the loop to stop asking
  if choice == "no":
    break

#after the player is done receiving cards its time for the computer
card4 = random.randint(1,10)
card5 = random.randint(1,10)
computerTotal = card4 + card5
print(card4, card5)

#since the computer grabs card automatically lets implement the rule where the computer will grab cards as long as their total is below 16 (this is true for the dealer in real life as well)

while computerTotal < 16:
  card6 = random.randint(1,10)
  print(card6)
  computerTotal = computerTotal + card6

print("Computer's total:", computerTotal)

#now both the player and the computer are done receiving cards its time to check the winner
#the rule for winning blackjack is who ever is closest to 21 without going over
if total>computerTotal and total <= 21:
  print("Player wins")
elif computerTotal > total and computerTotal <= 21:
  print("Computer wins")
elif computerTotal>21 and total > 21:
  print("Both lose")
elif computerTotal>21:
  print("computer loses")
elif total > 21:
  print("you lose")
else:
  print("tie")