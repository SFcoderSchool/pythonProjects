# Password Generator
# Difficulty: ⭐⭐
# Generate a string 4 character long password

# Steps
# 1. create a String of all the lowercase characters
# 2. generate a random number from 0 to len(alphabet)-1
# 3. output a random letter from the String
# 4. repeat with uppercase characters, numbers, and symbols
# 5. save all of these into a variable
# 6. randomly select 1 category and output a random character
# 7. ask the user for a number
# 8. repeat from 4 to the number inputted
# 9. output the final password

# Bonus
# 1. shuffle the password with list() and join()
# 2. guarantee that the user will input a number greater or equal to 6

import random

lowercharacters = "abcdefghijklmnopqrstuvwxyz"
uppercharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*(),.?/:;[]{}~|"

password = ""

rnum1 = random.randint(0,len(lowercharacters) - 1)
password = password + lowercharacters[rnum1]

rnum2 = random.randint(0,len(uppercharacters) - 1)
password = password + uppercharacters[rnum2]

rnum3 = random.randint(0,len(numbers) - 1)
password = password + numbers[rnum3]

rnum4 = random.randint(0,len(symbols) - 1)
password = password + symbols[rnum4]

user = input("Password Length: ")
user = int(user)

for i in range(4, user):
  chance = random.randint(1,4)
  if chance == 1:
    rnum1 = random.randint(0,len(lowercharacters) - 1)
    password = password + lowercharacters[rnum1]    
  if chance == 2:
    rnum2 = random.randint(0,len(uppercharacters) - 1)
    password = password + uppercharacters[rnum2]
  if chance == 3:
    rnum3 = random.randint(0,len(numbers) - 1)
    password = password + numbers[rnum3]
  if chance == 4:
    rnum4 = random.randint(0,len(symbols) - 1)
    password = password + symbols[rnum4]

print(password)