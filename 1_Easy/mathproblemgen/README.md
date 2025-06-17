# Math Problem Generator <br> ⭐★★★★★★★★★

## Background

Generate math equations and ask the user to solve the equation

## Steps

1. Create 2 variables and save a number in each variable
2. output a string equation using the variables as the numbers

```python
number1 = 0
number2 = 10

question = str(number1) + "+" + str(number2) + "="
```

3. ask the user to solve the equation
4. check to see if the user is correct
5. NOTE: make sure to cast the data to match properly

```python
answer = input(question)
answer = int(answer)

if answer == number1 + number2:
  print("correct")
else:
  print("incorrect! Answer was", number1 + number2)
```

6. replace the numbers with random numbers

```python
import random

number1 = random.randint(1, 100)
number2 = random.randint(1, 100)
```

7. repeat with subtraction, multiplication

```python
number1 = random.randint(1, 100)
number2 = random.randint(1, 100)
question = str(number1) + "-" + str(number2) + "="

answer = input(question)
answer = int(answer)

if answer == number1 - number2:
  print("correct")
else:
  print("incorrect! Answer was", number1 - number2)

number1 = random.randint(1, 100)
number2 = random.randint(1, 100)
question = str(number1) + "*" + str(number2) + "="

answer = input(question)
answer = int(answer)

if answer == number1 * number2:
  print("correct")
else:
  print("incorrect! Answer was", number1 * number2)
```

Bonus:

1. add a loop to repeat 10 times
2. set random number to select the type of equation seperately
3. include division, NOTE: data needs to be converted to a float and rounded
