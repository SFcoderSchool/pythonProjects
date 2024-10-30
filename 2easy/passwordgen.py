import random

#get all characters caps/lower, numbers, and symbols
uppercharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercharacters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*(),.?/:;[]{}~|"

#a password MUST contain one of each and cannot be lower than 6 characters
#lets start by making sure that the password is one of each
password = ""
password = password + random.choice(uppercharacters)
#show the student how to pick out one random character and then ask them to do the rest themselves
password = password + random.choice(lowercharacters)
password = password + random.choice(numbers)
password = password + random.choice(symbols)
#this will guarantee that the password will contain a uppercase, lowercase, number, and symbol

#now lets ask the user to decide the password length themselves for added variety
length = int(input("Password Length: "))
#repeat length amount of times minus 4 since we are already guaranteed to have 4 characters in the password
for i in range(length-4):
  #ask the student to roll a dice and randomly pick what type of character should be added to the password
  dice = random.randint(1,4)
  if dice == 1:
    password = password + random.choice(uppercharacters)
  if dice == 2:
    password = password + random.choice(lowercharacters)
  if dice == 3:
    password = password + random.choice(numbers)
  if dice == 4:
    password = password + random.choice(symbols)


#BONUS: shuffle the characters for added security so the order is different each time
password = list(password)
random.shuffle(password)
password = "".join(password)

print(password)

#SECOND BONUS: make sure the length input is greater than or eqal to 6
#this is done with a while loop right after the input
#while the input is < 6
# ask to type input again