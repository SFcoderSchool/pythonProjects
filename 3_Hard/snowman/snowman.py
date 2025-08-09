# Snowman
# given some random word, guess letters until word is guessed

# Steps
# Note: use functions as you make them towards the bottom of the code
# - start with 1 word
# - create the function formatWord with parameter word and return a list of underscores matching the length of the word

# - print out the list of underscores
# - make function formatUnderlines to return the list of underscores as a String

# - make function makeGuess to all the user to guess a letter; go through the word and replace the underscore at the same spot if there is a match

# - make function checkSuccess to return True if the word was guessed correctly; utilize the formatUnderlines function

# - add a loop to play the game
# - keep the game going until they get it correct

# - make list of words
# - make randomWord function to return a random word from the words list
# - update the word variable to contain a random word instead

# Bonus
# - make function containsLetter with paramter letter to return True if the word contains letter at least once
# - add an incorrect counter
# - stop the game when 6 wrong guesses




import random
words = ["cat", "dog", "house", "car", "tree", "book", "phone", "computer", "chair", "table", "apple", "banana", "city", "river", "mountain", "child", "flower", "bird", "sun", "moon"]

def randomWord():
  return words[random.randint(0,len(words)-1)]

def formatWord(word):
  u = []
  for i in range(len(word)):
    u.append("_")
  return u

def formatUnderlines():
  s = ""
  for i in range(len(underlines)):
    s = s + underlines[i]
  return s

def makeGuess():
  letter = input("Guess a letter: ")
  for i in range(len(secretWord)):
    if secretWord[i] == letter:
      underlines[i] = letter

def checkSuccess():
  guess = formatUnderlines()
  if secretWord == guess:
    return True
  else:
    return False
  
def containsLetter(letter):
  for i in range(len(secretWord)):
    if secretWord[i] == letter:
      return True
  return False

secretWord = randomWord()
underlines = formatWord(secretWord)

while True:
  print(formatUnderlines())
  makeGuess()
  if checkSuccess() == True:
    print(secretWord)
    print("You got it correct! ")
    break
  