#1 randomly choose a event from 4 options using if statements and random number

#2 each even will affect health in positive or negative way

#3 if player survives first incident, then proceed to next incident

#4 display health for every round. Health should not exceed 100.

#5 use time library to slow down the display of incidents

#Bonus: Use list and functions to build this program


import random
import time


hp = 100


#series 1
#each series will do the following
#1 random chance of event
#2 update health accordingly
#3 do not let health exceed 100
#4 display health
#5 wait so user can read before next event

chance = random.randint(1,4)
if chance == 1:
  print("you get hit by a  baseball -30 hp")
  hp = hp - 30
elif chance == 2:
  print('you get a paper cut -10 hp')
  hp = hp - 10
elif chance == 3:
  print('you step on dog poo -5 hp')
  hp = hp - 5
else:
  print('you found a pork bun +10 hp')
  hp = hp + 10

if hp>100:
  hp = 100
print("health:",hp)
time.sleep(1)

#series 2

if hp > 0:
  chance = random.randint(1,4)
  if chance == 1:
    print("you get bit by a mosquito -20 hp")
    hp = hp - 20
  elif chance == 2:
    print('you catch the flu -40 hp')
    hp = hp - 40
  elif chance == 3:
    print('you get hit by a toyota -80 hp')
    hp = hp - 80
  else:
    print('find $10 on the ground +10 hp')
    hp = hp + 10
else:
  print('game over')

if hp>100:
  hp = 100
print("health:",hp)
time.sleep(1)

#series 3
  
if hp > 0:
  chance = random.randint(1,4)
  if chance == 1:
    print("a basketball hits you in the face -30 hp")
    hp = hp - 30
  elif chance == 2:
    print('you walk into a pole -50 hp')
    hp = hp - 50
  elif chance == 3:
    print('you stub your toe -20 hp')
    hp = hp - 20
  else:
    print('you get free cotton candy +20hp')
    hp = hp + 20
else:
  print('game over')

if hp>100:
  hp = 100
print("health:",hp)
time.sleep(1)

#series 4

if hp > 0:
  chance = random.randint(1,4)
  if chance == 1:
    print("you forgot to do your homework -20 hp")
    hp = hp - 20
  elif chance == 2:
    print('you fall into a sinkhole -100 hp')
    hp = hp - 100
  elif chance == 3:
    print('you get stabbed by a spork -30 hp')
    hp = hp - 30
  else:
    print('get free warriors tickets +100 hp')
    hp = hp + 100
else:
  print('game over')

if hp>100:
  hp = 100
print("health:",hp)
time.sleep(1)

#check if alive at the end
if hp>0: 
  print("YOU SURVIVE!")





  
# Example for list version
# s1 = ["a basketball hits you in the face -30 hp",'you walk into a pole -50 hp','you stub your toe -20 hp','you get free cotton candy +20hp']
# s1hp = [-30, -10, -5, 10]


# chance = random.randint(0,3)
# print(s1[chance])
# hp = hp + s1hp[chance]
# print("health: ",hp)


# Example as function

# def incident(series, hp_list, hp):
#   chance = random.randint(0,3)
#   print(series[chance])
#   hp = hp + hp_list[chance]
#   if hp >100:
#     hp = 100
#   print("health: ",hp)
#   return hp
  
# hp = 100
# print( incident(s1,s1hp,hp) )
  