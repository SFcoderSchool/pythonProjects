# Use while loops when you would like to repeat for as long as the condition is True

# Structure:
# while [condition]:
#   do stuff
#   the indentation is important


# forever loop
# the condition True never changes to False
# while True:
#   print("hello")

# repeat until something is True and break the loop
import random
dice = random.randint(1,6)
while True:
  if dice <= 3:
    break
  print(dice, "bigger than 3")

# repeat until something is False and break the loop
# import random
dice = random.randint(1,6)
while dice > 3:
  print(dice, "bigger than 3")

