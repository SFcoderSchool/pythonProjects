# Wordle
# Copy of the popular nytimes game Wordle
# NOTE: will be using colored(text, color) to color the text https://pypi.org/project/termcolor/

# Steps
# 1. start with a word and store it in a variable

# 2. ask the user to guess a 5 letter word

# 3. go through all the letters in the guess and see if it matches with the letters in the answer and output green
# 4. as you go through if they do not match, but exist in the word output yellow
# 5. if letter does not exist in the answer then output white

# 6. instead of outputting the colors, save the colors in a list for each letter
# 7. go through the list of colors and letters of the guessed word
# 8. output the letter with its corresponding color using the colored() function

# 9. add a loop to repeat 6 times
# 10. stop early if the user guesses the word correctly
# 11. output the answer when the loop ends

# Bonus
# 1. add a word bank and select a random word to be the chosen word


from termcolor import colored
import os
import random   
# print(colored("hello","red"))
# print(colored("hello Alen is goofy","cyan"))


print(colored("Please choose a five letter word ","blue"))


words=["money","bread","hello","kwami","babys","dinos","pizza","apple","dance","anvil","print","coder","watch","shoes","books","witch","human","board","sting","drink","solar","power","phone","meter","moody","liter","biter","crumb","plump","first"]
word=words[random.randint(0,len(words)-1)]


nomatch="white"
match="yellow"
correct = "green"
guesses=[]

for turns in range(6):
  colors=[] 
  for i in range(5):
    colors.append(nomatch) 

  guess=input()
  while len(guess) != 5 :
    guess = input("put in a new 5 letter word \n")
  guesses.append(guess)
  
  for i in range(5):
    if word[i]==guess[i]:
      colors[i]=correct
    elif guess[i] in word:
      colors[i]=match

  # print(colors)
  # print(guess)
  # print(word)
  
  for i in range(5):  
    print(colored(guess[i],colors[i]),end="")
  print() 
  if guess==word:
    print("good job")
    break

