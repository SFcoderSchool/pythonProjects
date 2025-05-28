# Dice Guesser <br> ⭐★★★★★★★★★

## Background

Guess the outcome of a dice roll and see if you're right.

## Steps

1. generate a random number from 1 to 6 to simulate a dice roll
2. output the dice roll for now

```python
import random

dice = random.randint(1,6)
print("The dice rolled:", dice)
```

3. ask the user to guess
4. check to see if the user guessed correctly
5. NOTE: guess needs to be casted to an int

```python
guess = input("guess the die: ")
guess = int(guess)

if guess == dice:
    print("Correct!")
else:
    print("Incorrect.")
```

## Bonus:

1. add a loop to run this multiple times
2. keep track of the score of how many guessed correctly
