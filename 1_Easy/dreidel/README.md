# Dreidel <br> ⭐★★★★★★★★★

## Background

Pay a coin and spin the top.<br>
Depending on what the top lands on,
do the action depending on the rules.<br>
Lose all your coins and its game over

> **Rules**
>
> - Nun - receive nothing
> - Gimel - receive all coins from the table
> - Hay - receive half the coins from the table
> - Shin - put a coin to the table

## Steps

1. give player and computer 10 coins and table should have 0 coins

```python
player = 10
computer = 10
table = 0
```

2. both player and computer will pay the coin and put it in the table
3. use input() to pause the script

```python
player = player - 1
table = table + 1

computer = computer - 1
table = table + 1

input("Press Enter to play")
```

4. randomly select a number from 1 to 4 for the dreidel
5. output a word from the rules for each possible random number

```python
import random

...

dreidel = random.randint(1,4)
if dreidel == 1:
  print("Nun")
if dreidel == 2:
  print("Gimel")
if dreidel == 3:
  print("Hay")
if dreidel == 4:
  print("Shin")
```

6. depending on the rules, do the action for each word<br>
   **NOTE:** print out the half from hay and note the data type to the student

```python
if dreidel == 1:
  print("Nun")
  print("Do nothing")
if dreidel == 2:
  print("Gimel")
  print("Receive all coins from the table")
  player = player + table
  table = 0
if dreidel == 3:
  print("Hay")
  print("Receive half of the coins from the table")
  reward = table / 2
  # print(reward)
  reward = int(reward)
  player = player + reward
  table = table - reward
if dreidel == 4:
  print("Shin")
  print("Lose a coin, and put in to table")
  player = player - 1
  table = table + 1
```

7. use input() to pause the script
8. repeat the dreidel spin and rules for the computer

```python
input("Computer's turn to spin the dreidel!")

dreidel = random.randint(1,4)
  if dreidel == 1:
    print("nun, computer get nothing")
  if dreidel == 2:
    print("gimel, computer get all coins on table")
    computer = computer + table
    table = 0
  if dreidel == 3:
    print("hay, computer get half the coins on the table")
    reward = table/2
    # print(reward)
    reward = int(reward)
    computer = computer + reward
    table = table - reward
  if dreidel == 4:
    print("shin, computer lose 1 coin")
    computer = computer - 1
    table = table + 1
```

9. output the current amount of coins of player, computer, and table

```python
print("your coins", player)
print("computer coins", computer)
```

10. add a while True to repeat the game (steps 4 to 9)
11. stop the game when someone has reached 0 or less coins

```python
while True:

  ...

  if player <= 0:
    break
  if computer <= 0:
    break
```
