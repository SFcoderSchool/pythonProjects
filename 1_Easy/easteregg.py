import random
eggs = 0
for minutes in range(120):
  print("Minute:", minutes)
  dice = random.randint(1,6)
  if dice == 6:
    eggs = eggs + 1
    print("Found an easter egg!")
  if dice == 1:
    eggs = eggs - 1
    print("Found a rotten egg :(")
  chance = random.randint(1,100)
  if chance == 1:
    eggs = eggs + 100
    print("Found Mr.Beast golden egg!")

print("Times up!")
print("I found",eggs,"eggs!")