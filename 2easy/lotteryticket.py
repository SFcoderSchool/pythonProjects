#1. Allow user to create 3 variables to hold 3 inputs of numbers
#1.5 convert data into integers
#2 Generate 3 random numbers
#3 Check if you got any matches using if statements
#4 count matches
#5 using the count output how much you win



import random

print("Enter the numbers for your lottery ticket!")
num1 = input("Enter a number: ")
num2 = input("Enter a number: ")
num3 = input("Enter a number: ")

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

rnum1 = random.randint(1,10)

rnum2 = random.randint(1,10)
while rnum2 == rnum1: 
  rnum2 = random.randint(1,10)
  
rnum3 = random.randint(1,10)
while rnum3 == rnum1 or rnum3 == rnum2:
  rnum3 = random.randint(1,10)
print(rnum1,rnum2,rnum3)
correct = 0

if num1 == rnum1 or num1 == rnum2 or num1 == rnum3:
  correct = correct + 1

if num2 == rnum1 or num2 == rnum2 or num2 == rnum3:
  correct = correct + 1

if num3 == rnum1 or num3 == rnum2 or num3 == rnum3:
  correct = correct + 1

print(rnum1)
print(rnum2)
print(rnum3)
print("You got", correct, "correct")

if correct == 1:
  print("You won $10")
elif correct == 2:
  print("You won $100")
elif correct == 3:
  print("You won $1000")
else:
  print("You won nothing :(")