# Number Guesser <br> ⭐★★★★★★★★★

## Background

Generate a random number and guess it correctly

## Steps

1. Create a variable number and store an integer
2. Allow user to guess using input() and save it in a variable guess
3. Check to see if variables are equal

```python
number = random.randint(1,100)

question = "guess a number between 1 and 100"
guess = input(question)

if number == guess:
  print("Correct!")
else:
  print("Incorrect")
```

4. convert input into integer type to compare int to int

```python
guess = int(guess)
```

5. Using a while loop, allow user to guess until correct
6. Stop when the user guesses correctly

```python
while True:
  question = "guess a number between 1 and 100"
  guess = input(question)

  if number == guess:
    print("Correct!")
    break
  else:
    print("Incorrect")
```

7. Hints high or low

```python
if number == guess:
  print("Correct!")
  break
if number > guess:
  print("guess higher")
if number < guess:
  print("guess lower")
```

8. Track number of tries

```python
tries = 0

while True:
  tries = tries + 1

  ...

tries = str(tries)
print("you took " + tries + " guesses")
```

## Bonus

1. build a string to track low and high for the prompt

```python
low = "1"
high = "100"

while True:
  question = "guess a number between " + low + "and " + high + ": "

  ...

  if number == guess:
    print("Correct!")
    break
  if number > guess:
    print("guess higher")
    low = guess+1
    low = str(low)
  if number < guess:
    print("guess lower")
    high = guess - 1
    high = str(high)
```

2. Additional hints: hot or cold (10 numbers away from correct)

```python
if number - 10 < guess and number + 10 > guess:
  print("Hot")
elif number != guess:
  print("cold")
```
