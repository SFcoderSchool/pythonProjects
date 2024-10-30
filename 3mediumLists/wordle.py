
from termcolor import colored
import os
import random   
# print(colored("hello","red"))
# print(colored("hello Alen is goofy","cyan")


print(colored("Please choose a five letter word ","blue"))


words=["money","bread","hello","kwami","babys","dinos","pizza","apple","dance","anvil","print","coder","watch","shoes","books","witch","human","board","sting","drink","solar","power","phone","meter","moody","liter","biter","crumb","plump","first"]
word=words[random.randint(0,len(words))]





#build word bank for guesses
#read those guesses each turn and read colors each turn

#replaced in line 30 after or to test: ''.join(guesses).find(guess) != -1)

nomatch="white"
match="yellow"
correct = "green"
guesses=[]

#loop for each turn the player guesses
for turns in range(6):
  
  #make list of colors for letters all white
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
    elif word.find(guess[i])>=0:
      colors[i]=match
  
  for i in range(5):  
    print(colored(guess[i],colors[i]),end="") #print out the word with colored letters
  print() 
  if guess==word:
    print("good job")
    break

