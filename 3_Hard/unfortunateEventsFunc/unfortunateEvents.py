# School
# bad grade, caught the flu, tripped and fell

# Work
# yelled at by boss, run into door, tripped and broke ankle

# Restaraunt
# food poisoning, 200% tip, waiter dropped food

# Home
# clogged the toilet, broke the window, milk got spoiled

# Store
# shelves fell on you, slipped on wet floor, double charged on items

import random

locations = ["school", "work", "restaraunt", "home", "store"]
currentPlace = "home"

def home():
  global currentPlace

  event = random.randint(1,3)
  if event == 1:
    print("clogged the toilet")
  elif event == 2:
    print("broke the window")
  elif event == 3:
    print("milk got spoiled")
  
  user = input("where go next ")
  while checkLocation(user) == False:
    user = input("where go next ")
  currentPlace == user

def work():
  global currentPlace

  event = random.randint(1,3)
  if event == 1:
    print("you got yelled at by boss")
  elif event == 2:
    print("ran into door")
  elif event == 3:
    print("tripped and broke ankle")
  
  user = input("where go next ")
  while checkLocation(user) == False:
    user = input("where go next ")
  currentPlace == user

def restaraunt():
  global currentPlace

  event = random.randint(1,3)
  if event == 1:
    print("food poisoning")
  elif event == 2:
    print("200% tip")
  elif event == 3:
    print("waiter dropped food")
  
  user = input("where go next ")
  while checkLocation(user) == False:
    user = input("where go next ")
  currentPlace == user

def school():
  global currentPlace

  event = random.randint(1,3)
  if event == 1:
    print("got a bad grade")
  elif event == 2:
    print("caught flu")
  elif event == 3:
    print("tripped and fell")
  
  user = input("where go next ")
  while checkLocation(user) == False:
    user = input("where go next ")
  currentPlace == user

def store():
  global currentPlace

  event = random.randint(1,3)
  if event == 1:
    print("shelves fell on top of you")
  elif event == 2:
    print("slipped on wet floor")
  elif event == 3:
    print("double charged for items")
  
  user = input("where go next ")
  while checkLocation(user) == False:
    user = input("where go next ")
  currentPlace == user

def generateTime():
  hour = random.randint(0,23)
  minute = random.randint(0,59)
  print("Currently it is", str(hour) + ":" + str(minute), end=" : ")

def checkLocation(location):
  if location not in locations:
    return False
  return True


while True:
  generateTime()

  if currentPlace == "home":
    home()
  if currentPlace == "work":
    work()
  if currentPlace == "restaraunt":
    restaraunt()
  if currentPlace == "school":
    school()
  if currentPlace == "store":
    store()