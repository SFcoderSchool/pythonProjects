import random
import os
road = []
level=0
money=100
moneystamp = money
dead =False
prizetype =["money compounds per level", "Additional coins", "Invest in Bitcoin", "Extra Life", "Killer Car"]
prizes=[]
lives = 0
def startlevel():
  global level, road, dead, moneystamp, money, lives
  dead=False
  road = []
  for chicken in range(10):
    road.append("🛣️")
  for x in range(10):
    sprize = random.choice(prizetype)
    prizes.append(sprize)
  level = 0
  road[level]= "🐥"
  print(road)
  moneystamp = money




def makechoice():
  global level, lives, money, moneystamp, dead
  goo = input("Would you like to cross the road?")
  if goo.lower() == "yes":
    road[level] = "🛣️"
    level = level + 1
    money = money + 5
    road[level] = "🐥"
    print("Congragalations! For completing the level, you have earned", prizes[level]+".")
    if prizes[level]== "money compounds per level":
      money = money**(1.1*level)
    elif prizes[level] == "Additional Coins":
      money=money+15
    elif prizes[level]=="Invest in Bitcoin":
      crypto = input("Go in or go Home?")
      if crypto.lower() == "go in":
        cbro =random.randint(0,1)
        if cbro == 0:
          print(" HAAHAHAHHAHAHA YOU LOSE MONEY")
          money = money*0.5
        else:
          print("You're a Genius!!! You win a ton!!!")
          money = money * 2
      else:
        print(" You lost your chance to be cool.")
    elif prizes[level] == "Extra Life":
      lives =lives+1
    elif prizes[level]=="Killer Car":
      if lives > 0:
        lives=lives-1
        print("The car missed you by an inch! Be more careful next time and look both ways.")
      else:
        dead = True
        print("You lost! Try again later!")
        money=moneystamp
  print(road)


startlevel()
while dead == False:
  makechoice()