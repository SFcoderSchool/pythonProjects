# Dice Guesser
# Difficulty:
# roll a dice and guess the roll

# Steps:
# 1. generate a random number from 1 to 6 to simulate a dice roll
# 2. output the dice roll for now

# 3. ask the user to guess
# 4. check to see if the user guessed correctly
# 5. NOTE: guess needs to be casted to an int

# Bonus:
# 1. repeat the game 10 times and keep track of how many correct guesses

import random
score = 0
for i in range(10):
  dice = random.randint(1,6)
  # print("The dice rolled:", dice)
  guess = input("guess the die: ")
  guess = int(guess)
  if dice == guess:
    print("you guessed right")
    score = score + 1
  else: 
    print("you guessed wrong")

print("you got",score,"gueeses right")