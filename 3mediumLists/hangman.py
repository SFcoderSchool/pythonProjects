import random
import os



mistakes = 0
# create variable and store a string > make a list and randomly choose a word
word = "bottle"

#create empty list to hold "_" based on how many letters you have
blank = []
for i in range(len(word)):
  blank.append("_")

1#access hangman ascii art (google hangman ascii)
print(" ".join(blank))




# play as long as mistakes less than 6 or solved
while mistakes<6 and word != "".join(blank):

  guess = input() # user guess a letter
  change = False
  #check if any of the words letter is same as guess. If match, then switch blank's index position to guessed letter.
  for i in range(len(word)):
    if word[i] == guess:
      blank[i] = guess
      change = True
      
  #separate condition to check if any changes were made. If no changes were made, increase mistakes count by 1.
  if change == False:
    mistakes = mistakes + 1
  os.system("clear")

  print(" ".join(blank))
  