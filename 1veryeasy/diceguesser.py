#1 ROLL THE DIE

# import random
# dice = random.randint(1,6)


#2 GUESS THE ROLL

# import random
# dice = random.randint(1,6)
# guess = int(input("guess the die: ")) #make sure to cover inputs are string types
# if dice == guess:
#   print("you guessed right")
# else: #if you need more if statement practice use dice != guess
#   print("you guessed wrong")


#3 10 GUESSES AND TRACK THE CORRECT GUESSES

import random
score = 0
for i in range(10):
  dice = random.randint(1,6)
  guess = int(input("guess the die: "))
  if dice == guess:
    print("you guessed right")
    score = score + 1
  else: 
    print("you guessed wrong")

print("you got",score,"gueeses right")