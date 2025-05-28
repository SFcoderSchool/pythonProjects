# Coin Flip <br> ⭐★★★★★★★★★

## Background

Flip a virtual coin and guess the outcome.

## Steps

1. create a coin variable and set it to 1
2. check to see if that variable is a 1 and print out "Heads"

```python
coin = 1

if coin == 1:
  print("heads")
```

3. replace the 1 with a 2
4. add check to see if the variable is a 2 and print out "Tails"

```python
coin = 2

if coin == 1:
  print("heads")
if coin == 2:
  print("tails")
```

5. add randomization to pick between 1 and 2

```python
import random

coin = random.randint(1,2)

if coin == 1:
  print("heads")
if coin == 2:
  print("tails")
```

## Bonus:

1. add a for loop to flip 5 coins
2. create variables to track how many heads and tails that got shown
