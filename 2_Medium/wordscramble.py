import random

words = ["potato","sandwich","apple","sick","plant","battle","bottle"]

for i in range(3):
  #save word
  word = random.choice(words)
  # word = "potato"
  
  #covert word into a list to use shuffle function
  scramble = list(word)
  random.shuffle(scramble)
  
  #convert list back to string to display (can be skipped as long as you check list vs string instead of string vs string)
  scramble = "".join(scramble)
                 
  print(scramble)
  
  #guess until correct
  guess = input("guess the word: ")
  score = 1
  while guess!=word:
    scramble = list(word)
    random.shuffle(scramble)
    scramble = "".join(scramble)
    
    print(scramble)
    guess = input("guess `the word: ")
    score = score + 1
  
  print("score:", score)
  words.remove(word)


#