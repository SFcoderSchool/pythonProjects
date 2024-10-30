import random
import time
#this project simulates a person trick-or-treating and going through a hundred houses asking for candy
#some houses give candy, some houses dont
#1 create variable for candy
#2 write a for loop that loops 100 times
#3 roll a dice with 1/4 chance that the house will give you candy
#4 add a random amount of candy to your total
#5 randomly there is a 1/10th chance a ghost will come and steal your candy
#BONUS: create a grandprize
#there is a 1/100 chance you pick up a grand prize from Mr. Beast
#at the end you can choose to trade in your grandprize for more candy

candy = 0
grandprize = 0 
for houses in range(100):
  #roll a dice with 1/4 chance that the house will give you candy
  dice = random.randint(1,4)
  if dice == 1:
    candy = candy + random.randint(1,4)
    print("you got candy")
  else:
    print("this house has no candy")
  #randomly there is a 1/10th chance a ghost will come and steal your candy
  dice2 = random.randint(1,10)
  if dice2 == 1:
    candy=candy-1
    print("a ghost stole my candy")
  #there is a 1/100 chance you pick up a grand prize from Mr. Beast
  dice3 = random.randint(1,100)
  if dice3==1:
    grandprize = grandprize + 1
    print ("you get an ultra rare charizard from Mr.Beast")
  time.sleep(0.4)
#at the end you can choose to trade in your grandprize for more candy    
print(grandprize)
if grandprize > 0:
  choice = input("Do you want to trade grandprize for candy?")
  if choice == "yes":
    candy = candy + 50
    print("You traded for candy")

#FINAL BONUS: write a for loop that will loop based on how much candy you have
print("You have " +str(candy) + " amount of candy")
for eat in range(candy):
  print("eatting.......")

print("I ate all the candy....")