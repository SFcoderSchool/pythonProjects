# Number Memory Game
# Difficulty:
# Game similar to simon says using numbers instead of colors

# Steps:
# 1. generate a random number and ask the user to guess the number and check to see if correct

# 2. NOTE: need a way to remember previous numbers, store as a String
# 3. create a variable to store all previously generated numbers 
# 4. make sure to convert the random integer to a string
# 5. output the variable

# 6. add a wait for about 1 second
# 7. clear the console
# 8. update the input to ask the user to guess the entire string
# 9. update the check to if the user guessed the entire string correctly

# 10. add a loop to repeat the game forever
# 11. stop the loop when the user guesses incorrectly

# Bonus:
# 1. add a scoring system to keep track how far the user gets
# 2. start the game with already 4 random digits
# 3. update time to pause scaling with the score

import random
import os
import time
score = 0
number = ""
memory = ""


while True:
  addnum = random.randint(0,9)
  addnum = str(addnum)
  number = number + addnum

  print("number:",number)
  time.sleep(1+(score//5))
  os.system("clear")

  memory = input("whats the number? ")
  if number == memory:
    score = score + 1
  os.system("clear")

  if number != memory:
    break

print("game over! score:",score)


