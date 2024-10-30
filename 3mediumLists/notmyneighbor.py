import random
import time
import os

#A game about finding the imposter!
#You get a list of dialogue and you gotta figure out which person is the imposter!


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

while True:
  randomGreeting = greeting[random.randint(0,len(greeting)-1)]
  randomConversation = conversation[random.randint(0,len(conversation)-1)]
  randomFollowUp = followUp[random.randint(0,len(followUp)-1)]
  randomGoodbye = goodbye[random.randint(0,len(goodbye)-1)]
  imposter = random.randint(1,2)
  if imposter == 1:
    randomGreeting = randomGreeting.replace("u","v")
    randomConversation = randomConversation.replace("u","v")
    randomFollowUp = randomFollowUp.replace("u","v")
    randomGoodbye = randomGoodbye.replace("u","v")
    #BONUS is to randomly decide what letters to replace not just the u and the v
    # dice = random.randint(1,4)
    # if dice == 1:
    #   randomGreeting = randomGreeting.replace("a","o")
    #   randomConversation = randomConversation.replace("a","o")
    #   randomFollowUp = randomFollowUp.replace("a","o")
    #   randomGoodbye = randomGoodbye.replace("a","o")
    # if dice == 2:
    #   randomGreeting = randomGreeting.replace("i","l")
    #   randomConversation = randomConversation.replace("i","l")
    #   randomFollowUp = randomFollowUp.replace("i","l")
    #   randomGoodbye = randomGoodbye.replace("i","l")
    # if dice == 3:
    #   randomGreeting = randomGreeting.replace("u","v")
    #   randomConversation = randomConversation.replace("u","v")
    #   randomFollowUp = randomFollowUp.replace("u","v")
    #   randomGoodbye = randomGoodbye.replace("u","v")
    # if dice == 4:
    #   randomGreeting = randomGreeting.replace("o","c")
    #   randomConversation = randomConversation.replace("o","c")
    #   randomFollowUp = randomFollowUp.replace("o","c")
    #   randomGoodbye = randomGoodbye.replace("o","c")

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

#BONUS: add a score variable
#mathematically make time.sleep lower the more score you get
#example time.sleep(2-score/10)