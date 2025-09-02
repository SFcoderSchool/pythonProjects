# Word Scramble
# Scramble the letters of a word, attempt to guess the word

# Steps:
# - create a variable and save a word in it, then print it out

# - create an empty list to store all the letters of the word
# - index through the word and append each letter to the list
# - using the random library, shuffle the list

# - create an empty string
# - go through all the letters of the shuffled list and add them to the empty string

# - ask the user, what the scrambled word is
# - check to see if they got it right or wrong

# - add a loop to keep the guess going until they get it correct

# Bonus:
# - reshuffle the word when they guess it wrong; count how many attempts it took them to get it correct
# - add a list of words, set the word to be a random word from the words list
# - repeat the game 3 times, after each run, remove the chosen word from the words list


import random

words = ["potato","sandwich","apple","sick","plant","battle","bottle"]

for i in range(3):
  #save word
  randomIndex = random.randint(0, len(words)-1)
  word = words[randomIndex]
  # word = "potato"
  
  scrambleLetters = []
  for i in range(len(word)):
    scrambleLetters.append(word[i])
  random.shuffle(scrambleLetters)

  scramble = ""
  for i in range(len(scrambleLetters)):
    scramble = scramble + scrambleLetters[i]
  print(scramble)
  
  #guess until correct
  guess = input("guess the word: ")
  score = 1
  while guess!=word:
    scrambleLetters = []
    for i in range(len(word)):
      scrambleLetters.append(word[i])
    random.shuffle(scrambleLetters)

    scramble = ""
    for i in range(len(scrambleLetters)):
      scramble = scramble + scrambleLetters[i]
    print(scramble)
     
    guess = input("guess `the word: ")
    score = score + 1
  
  print("score:", score)
  words.remove(word)

