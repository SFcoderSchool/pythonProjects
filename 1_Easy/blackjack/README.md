# BlackJack <br> ⭐★★★★★★★★★

## Background

Basic recreation of the game BlackJack

## Steps

1. create 2 card variables and assign them random numbers from 1 to 10
2. output the 2 cards and the total of the 2 cards

```python
import random

card1 = random.randint(1,10)
card2 = random.randint(1,10)

print(card1, card2)
print(card1 + card2)
```

3. ask the user if they would like an extra card and save their answer in a variable
4. if they say yes then generate a new random number from 1 to 10
5. output the running total of the player, need a variable to save the total of the first 2 cards

```python
total = card1 + card2

choice = input("do you want a card? ")
if choice == "yes":
  card3 = random.randint(1,10)
  total = total + card3
  print(card3)
  print("Total:",total)
```

6. start a while True loop to repeat steps 3 - 5
7. stop the loop when the user enters no or total is greater equal to 21

```python
while True:
  choice = input("do you want a card? ")
  if choice == "yes":
    card3 = random.randint(1,10)
    total = total + card3
    print(card3)
    print("Total:",total)
  if choice == "no":
    break
  if total >= 21:
    break
```

8. dealers turn: create 2 card variables and assign them random numbers from 1 to 10
9. the dealer will always hit on 16 and below and player is not busted

```python
card4 = random.randint(1,10)
card5 = random.randint(1,10)
dealertotal = card4 + card5
print(card4, card5)

while True:
  if total > 21:
    break
  elif dealertotal > 16:
    break
  else:
    card6 = random.randint(1,10)
    print(card6)
    dealertotal = dealertotal + card6

print("Dealer total:", dealertotal)
```

10. check for who wins

```python
if total > 21:
  print("player bust")
elif dealertotal > 21:
  print("dealer bust")
elif dealertotal > total:
  print("dealer wins")
elif total > dealertotal:
  print("player wins")
else:
  print("tie")
```
