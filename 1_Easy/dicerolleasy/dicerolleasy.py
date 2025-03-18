# Dice Roll (Easy)
# Difficulty: ⭐
# Roll a dice and win on certain numbers

# Steps
# 1. generate a random number between 1 and 6 and save it in a variable dice
# 2. print out the dice

# 3. check to see if the dice is a win (greater than 3) or a loss (3 or below)
# 4. print out the win and the loss

# Bonus
# 1. add a loop to repeat the code 10 times
# 2. create variables to keep track of total wins and total losses
# 3. output if they won more or loss more or tie

import random

wins = 0
loss = 0

for i in range(6):
  dice = random.randint(1,6)
  print(dice)
  if dice > 3:
    wins = wins + 1
    print("win!")
  if dice <= 3:
    loss = loss + 1
    print("loss :(")

print("WINS ", wins)
print("LOSS ", loss)

if wins > loss:
  print("You won more!")
if wins < loss:
  print("You loss more!")
if wins == loss:
  print("tie")