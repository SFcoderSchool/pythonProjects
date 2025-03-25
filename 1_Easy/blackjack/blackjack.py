# Blackjack
# Difficulty:⭐
# Basic recreation of the game BlackJack

# Steps
# 1. create 2 card variables and assign them random numbers from 1 to 10
# 2. output the 2 cards and the total of the 2 cards

# 3. ask the user if they would like an extra card and save their answer in a variable
# 4. if they say yes then generate a new random number from 1 to 10
# 5. output the running total of the player, need a variable to save the total of the first 2 cards

# 6. start a while True loop to repeat steps 3 - 5
# 8. stop the loop when the user enters no or total is greater equal to 21

# 9. dealers turn: create 2 card variables and assign them random numbers from 1 to 10
# 10. the dealer will always hit on 16 and below and player is not busted

# 11. check for who wins

import random

card1 = random.randint(1,10)
card2 = random.randint(1,10)
total = card1 + card2

print(card1, card2)
print("Total:", total)

while True:
  choice = input("do you want a card? ")
  if choice == "yes":
    card3 = random.randint(1,10)
    total = total + card3
    print(card3)
    print("Total:",total)
  if choice == "no":
    break
  if total >= 21:
    break

card4 = random.randint(1,10)
card5 = random.randint(1,10)
dealertotal = card4 + card5
print(card4, card5)

while dealertotal < 16:
  card6 = random.randint(1,10)
  print(card6)
  dealertotal = dealertotal + card6

print("dealer's total:", dealertotal)

if total > 21:
  print("player bust")
elif dealertotal > 21:
  print("dealer bust")
elif dealertotal > total:
  print("dealer wins")
elif total > dealertotal:
  print("player wins")
else:
  print("tie")