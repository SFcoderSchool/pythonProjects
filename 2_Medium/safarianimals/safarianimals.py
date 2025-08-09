# Safari Animals
# Have a safari and fill it with animals!

# Steps
# - Make a list called safari.
# - Write a forever loop asking "What animals would you like to add to the safari?"
# - Take the input and append it to the list.

# - Stop when user types in "stop"
# - print out the size of your list

# - Write a for loop to iterate through each animal in the list and print them out.
# - Randomly pick out 1 animal from the list to be VERY HAPPY in the safari.

import random

safari = []
while True:
  animal = input("What animals would you like to add to the safari?")
  if animal == "stop":
    break
  safari.append(animal)

size = len(safari)
print("Your safari has", size, "animals!")
for i in range(size):
  print(safari[i])

print(safari[random.randint(0,size-1)], "is very happy in the safari!")