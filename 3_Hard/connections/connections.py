# Connections w/ dictionaries
# Difficulty: ⭐⭐⭐⭐
# Based on the game from the New York Times, Connections.

# Steps:
# 1. create the dictionary of 16 words as the key with the category for each word as the value
# 2. get all the keys from the dictionary
# 3. NOTE: this is not a list; need to convert to a list
# 4. shuffle the list of words

# 5. output the list of words in a 4x4 format
# 6. create an index counter to keep track of where you are in the list
# 7. NOTE: will use this later, turn into a function

# 8. ask the user to pick out a word 4 times
# 9. save the user inputs in a list
# 10. check if all the words are of matching categories
# 11. if it is then output the categgory they picked, and removed the selected words
# 12. NOTE: will use this later, turn into a function

# 13. one round of the game consists of outputting the words in a grid, and asking the user to pick 4 words
# 14. NOTE: use the functions from before to accomplish this
# 15. add a while True to repeat and stop when there are no more words in the words list

# Bonus:
# 1. can cheat if choosing the same words over and over, add checks to stop that from happening

import random

connections = {
  "strawberries": "red",
  "fire truck": "red",
  "roses": "red",
  "apple": "red",
  "saphire":"blue",
  "blueberry":"blue",
  "sky":"blue",
  "ocean":"blue",
  "orange":"orange",
  "carrot":"orange",
  "pumpkin":"orange",
  "tiger":"orange",
  "grass":"green",
  "avocado":"green",
  "frog":"green",
  "leaves":"green"
}

words = connections.keys()
words = list(words)
random.shuffle(words)

def printWords():
  index = 0
  rows = int(len(words)/4)
  for i in range(rows):
    line = ""
    for j in range(4):
      line += str(index) + ")" + words[index] + " \t"
      index += 1
    print(line)

def select4words():
  selection = []
  for i in range(4):
    num = int(input("Select a word #: "))
    selection.append(words[num])

  if connections[selection[0]] == connections[selection[1]] == connections[selection[2]] == connections[selection[3]]:
    print("The category was: " + connections[selection[0]])
    for i in range(4):
      words.remove(selection[i])
  

while True:
  printWords()
  select4words()

  if len(words) == 0:
    print("Congratz you grouped all words!")
    break