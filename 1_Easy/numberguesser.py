#1 Create variable and store a value (integer)
#2 Allow user to guess using input()
#3 Check to see if variables are equal
#3.5 convert input into integer type to compare int to int

#4 Using a for loop, allow user to set number of tries

#4.5 Using a while loop, allow user to guess until correct

#5 Hints hot or cold (10 numbers away from correct)

#5.5 Hints high or low

#6 Track number of tries

#Bonus: build a string to track low and high for the prompt

import random

tries = 0
number = random.randint(1,100)
for i in range(10):
  string = "guess a number between 1 and 100: "
  guess = int(input(string))
  tries = tries + 1
  if number == guess:
    print("Correct!")
    break
  if number > guess:
    print("guess higher")
    low = guess+1
  if number < guess:
    print("guess lower")
    high = guess - 1
print("you took",tries,"guesses")