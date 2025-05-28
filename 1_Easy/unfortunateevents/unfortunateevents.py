# A series of unfortunate events
# Difficulty:
# start with some health and experience a series of unfortunate events and see if you survive

# Steps:
# 1. output 4 events

# 2. generate a random number from 1 to 4
# 3. update code to output an event per each number

# 4. create a hp variable to keep track of hp
# 5. for each event, change the amount of hp they would lose

# 6. display the health after this series of events has finished and move on to the next series

# 7. check to see if the user has died, if they have not then run the next series otherwise game over
# 8. rinse and repeat 1 more time with new events

# 9. finally check to see if the user survived till the end


# Bonus: 
# 1. add more events
# 2. Use list and functions to build this program
# 3. add time to pause after each event series


import random
import time

hp = 100

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
  