# Halloween Candy 
# Difficulty: ⭐

# This project simulates a person trick-or-treating and going through a hundred houses asking for candy
# some houses give candy, some houses dont

# 1. create a variable for total candy 
# 2. create a 1/4 chance that the house will give you candy 
# 3. add 10 candy to total candy and output total candy

# 4. update code such that a random amount of candy will be added

# 5. create a 1/10 chance for a ghost to steal a candy and output the total candy

# 6. start a loop to visit 100 houses loop steps 2 to 5

# Bonus
# 1. create a GRAND PRIZE for 1/100 chance to gain a bonus prized (insert item here)
# 2. give the user a chance to trade in the prized (insert item here) for more candy
# 3. create a loop to output "eating..." for as many candies you have obtained

#1 create variable for candy
#2 write a for loop that loops 100 times
#3 roll a dice with 1/4 chance that the house will give you candy
#4 add a random amount of candy to your total
#5 randomly there is a 1/10th chance a ghost will come and steal your candy
#BONUS: create a grandprize
#there is a 1/100 chance you pick up a grand prize from Mr. Beast
#at the end you can choose to trade in your grandprize for more candy

import random
import time

candy = 0
grandprize = 0 
for houses in range(100):
  chance = random.randint(1,4)
  if chance == 1:
    candy = candy + random.randint(1,4)
    print("you got candy")
  else:
    print("this house has no candy")

  chance2 = random.randint(1,10)
  if chance2 == 1:
    candy=candy-1
    print("a ghost stole my candy")

  time.sleep(0.4)

chance3 = random.randint(1,100)
if chance3==1:
  print ("you get an ultra rare charizard from Mr.Beast")
  user = input("Do you want to trade grandprize for candy?")
  if user == "yes":
    candy = candy + 100
    print("you get an extra 100 pieces of candy")

print("You have " +str(candy) + " amount of candy")
for eat in range(candy):
  print("eating.......")

print("I ate all the candy....")