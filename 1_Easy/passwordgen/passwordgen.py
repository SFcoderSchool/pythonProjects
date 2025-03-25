# Password Generator
# Difficulty: ⭐
# Generate a string 4 character long password

# Steps
# 1. create a String of all the lowercase characters
# 2. generate a random letter from the lowercase characters with random.choice()
# 3. output a random letter from the String
# 4. repeat with uppercase characters, numbers, and symbols
# 5. save all of these into a variable
# 6. randomly select 1 category and output a random character
# 7. ask the user for a number
# 8. repeat from 4 to the number inputted and add a random character from a random category to the password
# 9. output the final password

# Bonus
# 1. shuffle the password with list() and join()
# 2. guarantee that the user will input a number greater or equal to 6

import random

uppercharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercharacters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*(),.?/:;[]{}~|"

password = ""
password = password + random.choice(uppercharacters)
password = password + random.choice(lowercharacters)
password = password + random.choice(numbers)
password = password + random.choice(symbols)

user = input("Password Length: ")
user = int(user)
for i in range(4, user):
  chance = random.randint(1,4)
  if chance == 1:
    password = password + random.choice(uppercharacters)
  if chance == 2:
    password = password + random.choice(lowercharacters)
  if chance == 3:
    password = password + random.choice(numbers)
  if chance == 4:
    password = password + random.choice(symbols)

password = list(password)
random.shuffle(password)
password = "".join(password)

print(password)