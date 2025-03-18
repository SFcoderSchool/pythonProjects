# Lottery Ticket 
# Difficulty: ⭐
# Guess 3 numbers, check to see if you got it right

# Steps
# 1. Generate a random number between 1 to 10 and print it

# 2. Ask the user to guess the number
# 3. Check to see if the user is correct or incorrect

# 4. Change the input data to an int (Test again)

# 5. Generate 2 more random number between 1 and 10
# 6. Ask 2 more times with 2 new variables

# 7. check to see if the user is correct or incorrect

# 8. create a count and count how many guesses were guessed correctly

# 9. player wins alot of money if there are 3 correct
# 10. player wins a moderate amount of money if there are 2 correct
# 11. player wins a little bit of money if there is 1 correct
# 12. player wins nothing if there are no correct

# Bonus
# 1. make all random number unique

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