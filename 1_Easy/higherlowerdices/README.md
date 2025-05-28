# Higher or Lower Dices <br> ⭐★★★★★★★★★

## Background

roll 3 dices for the player and computer, guess if you have the higher total or lower total

## Steps

1. generate 3 random numbers from 1 to 6 to simulate 3 dice rolls for the player
2. output the 3 dices
3. add up all 3 dices and save the total into a variable

```python
import random

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
dice3 = random.randint(1,6)
print("Your dices:", dice1, dice2, dice3)
playertotal = dice1 + dice2 + dice3
```

4. generate 3 more random numbers from 1 to 6 to sumulate 3 dice rolls for the computer
5. output the 3 dices
6. add up all 3 dices and tabe the total into a variable

```python
cdice1 = random.randint(1,6)
cdice2 = random.randint(1,6)
cdice3 = random.randint(1,6)
computertotal = cdice1 + cdice2 + cdice3
```

7. ask the user to guess if their total is higher than the computer's total
8. check to see if their guess was correct or not

```python
choice = input("who wins, higher or lower?")
print("Computer dices:", cdice1, cdice2, cdice3)

if choice == "higher":
  if playertotal > computertotal:
    print("you win")
  else:
    print("you lose")

if choice == "lower":
  if playertotal < computertotal:
    print("you win")
  else:
    print("you lose")
```

9. turn off the cheats and add a loop to the game
10. add a score variable into the game
11. output the score inside the loop
12. increment / decrement the score where you win or lose

```python
score = 0

while True:
  ...

  if choice == "higher":
    if playertotal > computertotal:
      print("you win")
      score = score + 1
    else:
      print("you lose")
      score = score - 1

  if choice == "lower":
    if playertotal < computertotal:
      print("you win")
      score = score + 1
    else:
      print("you lose")
      score = score - 1

  print("Score:",score)
```
