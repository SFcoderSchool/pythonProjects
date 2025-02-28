#first we will import random which is acquiring the tool that will help us generate random numbers
import random

#now we will generate a random number with the example of a dice
dice = random.randint(1,6)

print(dice)

#run the project several times and see that the dice rolls a random number each time

#now let us combine what we learned from the datatypes lesson
#modify print dice to include a string label in front of the number
print("dice:", dice)

#now that we see the dice roll labeled correctly lets add ALOT more code to this project

#challenges
#1) create a money variable, set it to equal 0
#2) create a name variable, set it to equal your name
#Answers:
money = 0
name = "jason"

#now to roll a dice and add it to money
dice = random.randint(1,6)
print("dice", dice)
money = money + dice
print("money:",money)

#now do this many more times by writing a repeat 10 loop
for i in range(10):
    dice = random.randint(1,6)
    print("dice", dice)
    money = money + dice
    print("money",money)