import random

items = {
  "pencil": 5,
  "pen": 10,
  "notebook": 20,
  "ruler": 15,
  "eraser": 3,
  "highlighter": 8,
  "backpack": 100,
  "calculator": 50,
  "glue": 5,
  "scissors": 15
}
#retreiving all the keys from the dictionary into a list
keysList = list(items.keys())
#picking out a random item from the list of keys
randKey = keysList[random.randint(0,len(keysList)-1)]

for tries in range(3):
  #asking the player to guess how much the item cost
  guess = input("How much does "+ randKey +" cost?")
  guess = int(guess)
  #checking what the price is in the dictionary
  if guess == items[randKey]:
    print("You are CORRECT!")
    break
  elif guess > items[randKey]:
    print("You guessed too high")
  elif guess < items[randKey]:
    print("You guessed too low")

difference = abs(items[randKey] - guess)
print("Your guess was this far off", difference)