# Number Guesser
# Difficulty: ⭐
# Generate a random number and guess it correctly

# Steps
# 1. Create a variable number and store an integer
# 2. Allow user to guess using input() and save it in a variable guess
# 3. Check to see if variables are equal

# 4. convert input into integer type to compare int to int

# 5. Using a for loop, allow user to try 10 times
# 6. Stop when the user guesses correctly
# 7. Using a while loop, allow user to guess until correct

# 8. Hints hot or cold (10 numbers away from correct)
# 9. Hints high or low

# 10. Track number of tries

# Bonus: build a string to track low and high for the prompt

import random

tries = 0
number = random.randint(1,100)
low = "1"
high = "100"

for i in range(10):
  question = "guess a number between " + low + "and " + high + ": "
  guess = input(question)
  guess = int(guess)
  tries = tries + 1

  if number == guess:
    print("Correct!")
    break
  elif number > guess:
    print("guess higher")
    low = guess+1
    low = str(low)
  elif number < guess:
    print("guess lower")
    high = guess - 1
    high = str(high)

  if number - 10 < guess and number + 10 > guess:
    print("Hot")
  elif number != guess:
    print("cold")

tries = str(tries)
print("you took " + tries + " guesses")