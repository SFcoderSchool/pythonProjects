# Dice Roll (Easy) <br> ⭐★★★★★★★★★

## Background

Roll a dice and win on certain numbers

## Steps

1. generate a random number between 1 and 6 and save it in a variable dice
2. print out the dice

```python
import random

dice = random.randint(1,6)
print(dice)
```

3. check to see if the dice is a win (greater than 3) or a loss (3 or below)
4. print out the win and the loss

```python
if dice > 3:
  print("win!")
if dice <= 3:
  print("loss :(")
```

## Bonus

1. add a loop to repeat the dice roll 10 times

```python
for i in range(0,10,1):
  dice = random.randint(1,6)
  print(dice)
  if dice > 3:
    print("win!")
  if dice <= 3:
    print("loss :(")
```

2. create variables to keep track of total wins and total losses

```python
wins = 0
loss = 0

for i in range(0,10,1):
  dice = random.randint(1,6)
  print(dice)
  if dice > 3:
    wins = win + 1
    print("win!")
  if dice <= 3:
    loss = loss + 1
    print("loss :(")

print("wins", wins)
print("losses", loss)
```

3. output if they won more or loss more or tie

```python
if wins > loss:
  print("You won more!")
if wins < loss:
  print("You loss more!")
if wins == loss:
  print("tie")
```
