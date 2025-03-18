# Magic 8 Ball 
# Difficulty: ⭐
# Ask the program a question, program will respond with a random response

# Steps
# 1. Ask the user for a question

# 2. Generate a random number between 1 and 5
# 3. Output the number

# 4. Check to see if the number is 1 and output a message for 1
# 5. Check to see if the number is 2 and output a different message for 2
# 6. Continue until all numbers accounted for

# Bonus
# 1. add more numbers and messages

import random

input("Ask me a questions: ")
#input does not need to be saved since responses are randomized

chance = random.randint(1,5)

if chance == 1:
  print("Yes")
elif chance == 2:
  print("No")
elif chance == 3:
  print("Maybe")
elif chance == 4:
  print("Hm... ask me again tomorrow")
else:
  print("That's a weird question to ask.")