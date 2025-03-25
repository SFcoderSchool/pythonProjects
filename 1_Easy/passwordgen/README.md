# Password Generator <br> ⭐★★★★★★★★★

## Background

Generate a string 4 character long password

## Steps

1. create a String of all the lowercase characters
2. generate a random letter from the lowercase characters with random.choice()
3. output a random letter from the String

```python
import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
print(random.choice(lowercase))
```

4. repeat with uppercase characters, numbers, and symbols
5. save all of these into a variable

```python
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*(),.?/:;[]{}~|"

password = ""

password = password + random.choice(lowercase)
password = password + random.choice(uppercase)
password = password + random.choice(numbers)
password = password + random.choice(symbols)
```

6. randomly select 1 category and output a random character

```python
chance = random.randint(1,4)

if chance == 1:
  password = password + random.choice(lowercase)
elif chance == 2:
  password = password + random.choice(uppercase)
elif chance == 3:
  password = password + random.choice(numbers)
else:
  password = password + random.choice(symbols)
```

7. ask the user for a number
8. repeat from 4 to the number inputted and add a random character from a random category to the password
9. output the final password

```python
user = input("Enter a number: ")
user = int(user)

for i in range(4, user):
  chance = random.randint(1,4)

  if chance == 1:
    password = password + random.choice(lowercase)
  elif chance == 2:
    password = password + random.choice(uppercase)
  elif chance == 3:
    password = password + random.choice(numbers)
  else:
    password = password + random.choice(symbols)

print(password)
```

## Bonus

1. shuffle the password with list() and join()

```python
password = list(password)
random.shuffle(password)
password = "".join(password)
```

2. guarantee that the user will input a number greater or equal to 6

```python
user = input("Enter a number: ")
user = int(user)

while user < 6:
  user = input("Enter a number: ")
  user = int(user)
```
