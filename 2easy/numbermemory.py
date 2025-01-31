# **import clear function first since it takes a few minutes**

# 1 Create a variable and store a empty string 

#2 import random library and using randint to generate a single digit 0-9

#3 add random digit into the empty string. convert random digit into string type

#4 print number

#5 import time library and using the sleep function, wait 1 second

#6 clear the screen using the clear() before the user guesses

#7 allow user to guess. 

#8 Write a while loop to allow user to continue playing as long as the number and your memory matches


#9 Score

#bonus: Allow user to increase sleep time by 1 second for every 5 digits. use //

#bonus: start game with 4 random values in string 

#bonus: add numbers to string 2 at a time
# 24
# 2468
# 246827



import random
import os
import time
score = 0
number = ""
memory = ""


while number == memory:
  addnum = random.randint(0,9)
  number = number + str(addnum)
  print("number:",number)
  time.sleep(1+(score//5))
  os.system("cls")
  memory = input("whats the number? ")
  if memory == number:
    score = score + 1
  os.system("cls")
print("game over! score:",score)


