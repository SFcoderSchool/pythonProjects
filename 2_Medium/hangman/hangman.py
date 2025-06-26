# Hangman
# guess a letter until you guess the word or fail too many times

# Steps
# 1. create the word and store it in a variable

# 2. create an empty blanks list and fill it with underscores
# 3. output the blanks list

# 4. ask the user to guess a letter
# 5. go through the word and check to see if the letter guessed matches any letters in the word
# 6. if it does then set the "_" to the letter in that position

# 7. create a mistakes counter and a variable change to remember if the code entered the correct if statement
# 8. if there was no change to the change variable then the user got it wrong
# 9. otherwise the user was correct

# 10. add a while True loop to repeat the game
# 11. add condition to stop the game
# 12. stop the game when mistakes reaches 6 or when the blanks joined together equals the word

# Bonus
# 1. add hangman ascii art from google
# 2. add a word bank and randomly select a word

import random
import os


mistakes = 0
word = "bottle"

blank = []
for i in range(len(word)):
  blank.append("_")


print(" ".join(blank))


while mistakes<6 and word != "".join(blank):

  guess = input() 
  change = False

  for i in range(len(word)):
    if word[i] == guess:
      blank[i] = guess
      change = True
      
  if change == False:
    mistakes = mistakes + 1
  os.system("clear")

  print(" ".join(blank))
  