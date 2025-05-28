# Unforunate Events <br> ⭐★★★★★★★★★

## Background

start with some health and experience a series of unfortunate events and see if you survive

## Steps

1. output 4 events

```python
print("you get hit by a  baseball -30 hp")

print('you get a paper cut -10 hp')

print('you step on dog poo -5 hp')

print('you found a pork bun +10 hp')
```

2. generate a random number from 1 to 4
3. update code to output an event per each number

```python
import random

chance = random.randint(1,4)
if chance == 1:
  print("you get hit by a  baseball -30 hp")
elif chance == 2:
  print('you get a paper cut -10 hp')
elif chance == 3:
  print('you step on dog poo -5 hp')
else:
  print('you found a pork bun +10 hp')
```

4. create a hp variable to keep track of hp
5. for each event, change the amount of hp they would lose

```python
hp = 100

chance = random.randint(1,4)
if chance == 1:
  print("you get hit by a  baseball -30 hp")
  hp = hp - 30
elif chance == 2:
  print('you get a paper cut -10 hp')
  hp = hp - 10
elif chance == 3:
  print('you step on dog poo -5 hp')
  hp = hp - 5
else:
  print('you found a pork bun +10 hp')
  hp = hp + 10
```

6. display the health after this series of events has finished and move on to the next series

```python
print("health:",hp)
```

7. check to see if the user has died, if they have not then run the next series otherwise game over
8. rinse and repeat 1 more time with new events

```python
if hp > 0:
  chance = random.randint(1,4)
  if chance == 1:
    print("you get bit by a mosquito -20 hp")
    hp = hp - 20
  elif chance == 2:
    print('you catch the flu -40 hp')
    hp = hp - 40
  elif chance == 3:
    print('you get hit by a toyota -80 hp')
    hp = hp - 80
  else:
    print('find $10 on the ground +10 hp')
    hp = hp + 10
else:
  print('game over')
```

9. finally check to see if the user survived till the end

```python
if hp>0:
  print("YOU SURVIVE!")
```

## Bonus:

1. add more events
2. Use list and functions to build this program
3. add time to pause after each event series
