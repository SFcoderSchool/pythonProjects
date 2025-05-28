# Coinflip
# Difficulty:
# simulate flipping a coin

# Steps:
# 1. create a coin variable and set it to 1
# 2. check to see if that variable is a 1 and print out "Heads"

# 3. replace the 1 with a 2
# 4. add check to see if the variable is a 2 and print out "Tails"

# 5. add randomization to pick between 1 and 2

# Bonus:
# 1. add a for loop to flip 5 coins
# 2. create variables to track how many heads and tails that got shown

import random

heads = 0
tails = 0

for i in range(5):
  coin = random.randint(1,2)
  if coin == 1:
    print('heads')
    heads = heads + 1
  if coin == 2:
    print("tails")
    tails = tails + 1
  if heads == 3 or tails == 3:
    break

print("heads",heads)
print("tails",tails)