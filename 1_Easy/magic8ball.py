import random

input("Ask me a questions: ")
#input does not need to be saved since responses are randomized

chance = random.randint(1,5)

if chance == 1:
  print('Yes')
elif chance == 2:
  print("No")
elif chance == 3:
  print("Maybe")
elif chance == 4:
  print("Hm... ask me again tomorrow")
else:
  print("That's a weird question to ask.")