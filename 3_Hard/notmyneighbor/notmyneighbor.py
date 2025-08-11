# Not my neighbor
# Find if the text is from an imposter

# Steps
# - create a list of 5 greetings
# - create a list of 5 conversations
# - create a list of 5 followUps
# - create a list of 5 goodbye

# - create function pickRandom with 1 parameter (list), pick a random index and return a random string from the list
# - store a random greeting using the pickRandom function
# - store a random conversation using the pickRandom function
# - store a random followUp using the pickRandom function
# - store a random goodbye using the pickRandom function

# - create the printText function, print one of the variables, sleep for 2 seconds, clear the console

# - create the imposterfy function with 3 parameters (text, oldLetter, newLetter), return a new string without the oldLetter and replace it with the newLetter

# - before you use printText, determine whether or not there is an imposter with a coin flip
# - if there is then, imposterfy each text and change the u to i, then store the result back into the variable

# - ask the user is there an imposter
# - determine if the user guessed correctly

# - add a loop, stop the loop if the user guesses incorrectly

# Bonus
# - randomly decide what letters to replace not just the u and the v ( a to o, i to l, o to c, u to v )
# - add a score variable
# mathematically make time.sleep lower the more score you get
# example time.sleep(2-score/10)

import random
import time
import os

greeting = [
  "Hey there!",
  "Hi!",
  "Hello!",
  "What's up?",
  "Howdy!",
  "Yo!",
  "Hiya!",
  "Hey!",
  "Hi there!",
  "Hey, how's it going?",
  "Hey, what's going on?",
  "How's it hanging?",
  "Hey, how are you?",
  "Long time no see!",
  "Good to see you!",
  "Hey, good to see you!",
  "Hi, good to see you!",
  "Hey, how have you been?",
  "Hi, how have you been?",
]

conversation = [
  "Have you had any interesting travel experiences lately?",
  "What are some of your favorite books or movies?",
  "What hobbies or interests are you currently into?",
  "Have you heard about any recent events or news that caught your attention?",
  "Do you enjoy cooking or trying out new foods?",
  "Are you interested in the latest technology and gadgets?",
  "Have you been to any good music concerts lately?",
  "Are you into sports or fitness activities?",
  "Do you enjoy expressing yourself through art or creativity?",
  "What are some of your personal goals and aspirations?",
  "Do you have any funny anecdotes or stories to share?",
  "Do you have any exciting plans or trips coming up?",
  "How's work or your career going?",
  "Are you currently learning anything new or interesting?",
  "Do you have any pets? Tell me about them!",
  "How do you prioritize health and wellness in your life?",
  "Are you into fashion and style? What's your go-to look?",
  "What are your thoughts on relationships and dating?",
  "Have you been thinking about any environmental issues lately?",
  "What's your philosophy or perspective on life?",
]

followUp = [
  "That sounds fascinating. I'd love to hear more about it.",
  "I'm intrigued by that. Share some more details.",
  "Interesting! I didn't know that about you.",
  "Nice! It's always great to learn something new.",
  "I see! It's cool to see what you're passionate about.",
  "Wow, that's impressive. You must be really dedicated.",
  "That's awesome! It's cool to see your interests.",
  "Very cool. I can see why you enjoy it.",
  "Impressive! You've accomplished a lot.",
  "That's really interesting. I'm curious to know more.",
  "Neat! It's cool to hear about your experiences.",
  "That's intriguing. It's great to have a hobby like that.",
  "Wow, that's a lot. You must be busy!",
  "That's fascinating. It's interesting to see your perspective.",
  "That's impressive. It's clear you're passionate about it.",
  "That's cool. It's great that you're pursuing your interests.",
  "That's really interesting. It's cool to hear about your passion.",
  "That's intriguing. It's interesting to hear about your experiences.",
  "That's fascinating. It's great to hear about your passion.",
  "That's impressive. It's clear you've put a lot of effort into it.",
]

goodbye = [
  "See you later!",
  "Catch you later!",
  "Take care!",
  "Until next time!",
  "Bye for now!",
  "Later!",
  "Talk to you soon!",
  "Have a good one!",
  "Peace out!",
  "See you around!",
  "Goodbye!",
  "Bye!",
  "Take it easy!",
  "Stay safe!",
  "Adios!",
  "Ciao!",
  "Cheers!",
  "Farewell!",
  "Keep in touch!",
  "So long!",
]

def imposterfy(text, oldLetter, newLetter):
  s = ""
  for i in range(len(text)):
    if text[i] == oldLetter:
      s = s + newLetter
    else:
      s = s + text[i]
  return s

def pickRandom(textList):
  randomIndex = random.randint(0, len(textList) - 1)
  return textList[randomIndex]

def printText():
  print(randomGreeting)
  time.sleep(2)
  os.system("clear")

  print(randomConversation)
  time.sleep(2)
  os.system("clear")

  print(randomFollowUp)
  time.sleep(2)
  os.system("clear")

  print(randomGoodbye)
  time.sleep(2)
  os.system("clear")

while True:
  randomGreeting = pickRandom(greeting)
  randomConversation = pickRandom(conversation)
  randomFollowUp = pickRandom(followUp)
  randomGoodbye = pickRandom(goodbye)

  imposter = random.randint(1,2)
  if imposter == 1:
    randomGreeting = imposterfy(randomGreeting, "u", "v")
    randomConversation = imposterfy(randomConversation, "u", "v")
    randomFollowUp = imposterfy(randomFollowUp, "u", "v")
    randomGoodbye = imposterfy(randomGoodbye, "u", "v")
    
  printText()

  answer = input("Is this person an imposter?")
  if answer == "yes" and imposter == 1:
    print("You're right. They are suspicious.")
  elif answer == "no" and imposter == 2:
    print("You're right. They are fine.")
  else:
    print("IMPOSTER GOT YOU!")
    break

  time.sleep(2)
  os.system("clear")
