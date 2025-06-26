# Wheel of Fortune
# given a blanked out phrase, spin the wheel and guess a letter, if u guess it correct you recieve the spun amount

# Steps
# 1. start with a phrase and store it in a variable

# 2. create an empty list and fill it with either underscores or spaces depending on the phrase

# 3. create the list with number values in it to simulate the wheel
# 4. randomly select a number from the wheel and store it in a variable

# 5. ask the user to guess a letter
# 6. go through the phrase and see if the guess matches with any letters in the phrase
# 7. if so then update the underscore to match the guessed letter

# 8. create a wallet to store all your money
# 9. add the value of the randomly selected number from the wheel to the wallet, if there is a letter match

# 10. add a loop and stop when there are no more underscores

# Bonus
# 1. update code to be able to only purchase vowels and guess constanants
# 2. update code to not allow already guessed letters


import random
import os
phrase = "i am hungry today"
wallet = 0

blanks = []
for i in range(len(phrase)):
  if phrase[i] == " ":
    blanks.append(" ")
  else:
    blanks.append("_")

while "_" in blanks:
  print("wallet: ", wallet)
  print(" ".join(blanks))
  
  wheel = [1000, 500, 300, 200, 50, 750, 0]
  
  input("Spin the wheel (ENTER) ")
  spin = wheel[random.randint(0,len(wheel)-1)]

  if spin == 0:
    print("you landed on bankrupt")
    wallet = 0
  else:
    print('you landed on', spin)
  
    guess = input('Guess a letter: ')
    for i in range(len(phrase)):
      if phrase[i] == guess:
        blanks[i] = guess
        wallet = wallet + spin
    os.system("clear")

print("wallet: ", wallet)
print(" ".join(blanks))

