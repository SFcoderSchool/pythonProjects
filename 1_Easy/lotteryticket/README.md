# Lottery Ticket <br> ⭐★★★★★★★★★

## Background

Guess 3 numbers, check to see if you got it right

## Steps

1. Generate a random number between 1 to 10 and print it

```python
import random

num1 = random.randint(1,10)
print(num1)
```

2. Ask the user to guess the number
3. Check to see if the user is correct or incorrect

```python
user1 = input("Guess a random number: ")

if user1 == num1:
  print("correct")
else:
  print("incorrect")
```

4. Change the input data to an int (Test again)

```python
user1 = int(user1)
```

5. Generate 2 more random number between 1 and 10
6. Ask 2 more times with 2 new variables

```python
num2 = random.randint(1,10)
num3 = random.randint(1,10)

print(num2)
print(num3)

user2 = input("Guess a random number: ")
user3 = input("Guess a random number: ")
```

7. cast data and check to see if the user is correct or incorrect

```python
user2 = int(user2)
user3 = int(user3)

if user2 == num2:
  print("correct")
if user3 == num3:
  print("correct")
```

8. create a count and count how many guesses were guessed correctly

```python
count = 0

if user1 == num1:
  print("correct")
  count = count + 1
if user2 == num2:
  print("correct")
  count = count + 1
if user3 == num3:
  print("correct")
  count = count + 1
```

9. player wins alot of money if there are 3 correct
10. player wins a moderate amount of money if there are 2 correct
11. player wins a little bit of money if there is 1 correct
12. player wins nothing if there are no correct

```python
if correct == 1:
  print("You won $10")
elif correct == 2:
  print("You won $100")
elif correct == 3:
  print("You won $1000")
else:
  print("You won nothing :(")
```

# Bonus:

1. make all random numbers unique

```python
rnum2 = random.randint(1,10)
while rnum2 == rnum1:
  rnum2 = random.randint(1,10)

rnum3 = random.randint(1,10)
while rnum3 == rnum1 or rnum3 == rnum2:
  rnum3 = random.randint(1,10)
```
