#1 randomly choose a event from 4 options using if statements and random number

#2 each even will affect fortune in positive or negative way

#3 if player survives first incident, then proceed to next incident

#4 fortune every round

#5 use time library to slow down the display of incidents

#Bonus: Use list and functions to build this program


import random
import time


fortune = 100

#series 1
#each series will do the following
#1 random chance of event
#2 update fortune accordingly
#3 display fortune
#4 wait so user can read before next event

chance = random.randint(1,4)
if chance == 1:
  print("you lost a tone of money")
  fortune = fortune - 30
elif chance == 2:
  print('you get a paper cut, hospital fees cost 10')
  fortune = fortune - 10
elif chance == 3:
  print('you step on dog poo, you need new shoes -5')
  fortune = fortune - 5
else:
  print('you found a 10 dollars on the ground')
  fortune = fortune  + 10

print("fortune:",fortune)
time.sleep(1)

#series 2

if fortune > 0:
  chance = random.randint(1,4)
  if chance == 1:
    print("you get bit by a mosquito -20 fortune")
    fortune = fortune - 20
  elif chance == 2:
    print('you catch the flu -40 hospital fees')
    fortune = fortune - 40
  elif chance == 3:
    print('you bought a toyota -80 fortune')
    fortune = fortune - 80
  else:
    print('find $10 on the ground +10 fortune')
    fortune = fortune + 10
else:
  print('game over')


print("fortune:",fortune)
time.sleep(1)

#series 3
  
if fortune > 0:
  chance = random.randint(1,4)
  if chance == 1:
    print("a basketball hits you in the face -30 fortune")
    fortune = fortune - 30
  elif chance == 2:
    print('you walk into a pole -50 fortune')
    fortune = fortune - 50
  elif chance == 3:
    print('you stub your toe -20 fortune')
    fortune = fortune - 20
  else:
    print('you get free cotton candy +20 fortune')
    fortune = fortune + 20
else:
  print('game over')


print("fortune:",fortune)
time.sleep(1)

#series 4

if fortune > 0:
  chance = random.randint(1,4)
  if chance == 1:
    print("you failed college -20 fortune")
    fortune = fortune - 20
  elif chance == 2:
    print('you fall into a sinkhole -100 fortune')
    fortune = fortune - 100
  elif chance == 3:
    print('you get stabbed by a spork -30 fortune')
    fortune = fortune - 30
  else:
    print('get free warriors tickets +100 fortune')
    fortune = fortune + 100
else:
  print('game over')


print("fortune:",fortune)
time.sleep(1)

#check if alive at the end
if fortune>0: 
  print("YOU SURVIVE!")
else:
  print("you're in debt!")





  
# Example for list version
# s1 = ["a basketball hits you in the face -30 fortune",'you walk into a pole -50 fortune','you stub your toe -20 fortune','you get free cotton candy +20fortune']
# s1fortune = [-30, -10, -5, 10]


# chance = random.randint(0,3)
# print(s1[chance])
# fortune = fortune + s1fortune[chance]
# print("health: ",fortune)


# Example as function

# def incident(series, fortune_list, fortune):
#   chance = random.randint(0,3)
#   print(series[chance])
#   fortune = fortune + fortune_list[chance]
#   if fortune >100:
#     fortune = 100
#   print("health: ",fortune)
#   return fortune
  
# fortune = 100
# print( incident(s1,s1fortune,fortune) )
  