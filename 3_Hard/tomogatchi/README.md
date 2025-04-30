# Tomogatchi <br> ⭐⭐⭐⭐⭐★★★★★

## Background

Based off of the tomogatchi toy, keep the pet alive, by interacting with it everyday

# Steps:

1. create the pet with a dictionary to store the characteristics of your pet
2. output the pets information in a neat and concise manner
3. NOTE: will use this later, test and convert to a function

```python
pet = {
  "name": "Pikachu",
  "health": 20,
  "belly": 20,
  "rest": 20,
  "happiness": 20,
  "age": 1
}

def printPet():
  print("Name " + pet["name"])
  print("Health " + str(pet["health"]))
  print("Belly " + str(pet["belly"]))
  print("Rest " + str(pet["rest"]))
  print("Happiness " + str(pet["happiness"]))
  print("Age " + str(pet["age"]))
```

4. feed the pet by increasing the belly by a random number
5. NOTE: will use this later, test and convert to a function

```python
import random

...

def feed():
  print("You feed " + pet["name"])
  pet["belly"] += random.randint(5,10)
```

6. play with the pet by increasing the happiness by a random number
7. then lower the rest and belly by a random number
8. NOTE: will use this later, test and convert to a function

```python
def play():
  print("You played with " + pet["name"])
  pet["happiness"] += random.randint(5,10)
  pet["rest"] -= random.randint(5,10)
  pet["belly"] -= random.randint(5,10)
```

9. make your pet sleep by increasing the rest by a random number
10. NOTE: will use this later, test and convert to a function

```python
def sleep():
  print(pet["name"] + " went to sleep")
  pet["rest"] += random.randint(5,10)
```

11. advance to the next day by increasing the age by 1
12. then decrease the belly and rest by a random number
13. NOTE: will use this later, test and convert into a function

```python
def nextDay():
  pet["belly"] -= random.randint(5,10)
  pet["rest"] -= random.randint(5,10)
  pet["age"] += 1
  print("The day is over, everyone went to sleep, see you tomorrow.")
```

14. as the days progress, a random misfortune may fall upon the pet
15. roll a dice from 1 to 6
16. if the dice rolled a 1 then the pet had a bad night
17. if the dice rolled a 2 then the pet got sick
18. if the dice rolled a 3 then the pet got mad
19. if the dice rolled a 4 then the pet got more hungry
20. NOTE: will use this later, test and convert into a function

```python
def randomMisfortune():
  dice = random.randint(1,6)
  if dice == 1:
    print(pet["name"] + " had a bad night.")
    pet["rest"] -= random.randint(5,10)
  if dice == 2:
    print(pet["name"] + " got sick :(")
    pet["health"] -= random.randint(5,10)
  if dice == 3:
    print(pet["name"] + " woke up on the wrong side of the bed and is now angry at you.")
    pet["happiness"] -= random.randint(10,20)
  if dice == 4:
    print(pet["name"] + " is extra hungry today.")
    pet["belly"] -= random.randint(5,10)
```

21. request the user to do 3 activities with the pet
22. ask the user which activity they would like to do
23. depending on their choice call either the feed, play, sleep functions
24. repeat 3 times
25. NOTE: will use this later, test and convert to a function

```python
def threeActivities():
  for i in range(3):
    print("What would you like to do?")
    choice = input("1)Feed 2)Play 3)Sleep ")
    if choice == "1":
      feed()
    if choice == "2":
      play()
    if choice == "3":
      sleep()
```

26. check for gameover
27. it is game over when 1 of the characteristics of the pet reaches 0 or below

```python
if pet["health"] <= 0:
  print("Your pet has died.")
if pet["belly"] <= 0:
  print("Your pet has starved.")
if pet["rest"] <= 0:
  print("Your pet is exhausted.")
if pet["happiness"] <= 0:
  print("Your pet has ran away.")
```

28. NOTE: will use this later, test and convert to a function
29. return True if the pet has died, False otherwise

```python
def checkGameOver():
  if pet["health"] <= 0:
    print("Your pet has died.")
    return True
  if pet["belly"] <= 0:
    print("Your pet has starved.")
    return True
  if pet["rest"] <= 0:
    print("Your pet is exhausted.")
    return True
  if pet["happiness"] <= 0:
    print("Your pet has ran away.")
    return True
  return False
```

30. output the pet information
31. do 3 activities with the pet
32. goto the next day
33. check for a random misfortune

```python
printPet()
threeActivities()
nextDay()
randomMisfortune()
```

34. add a while True loop and repeat forever
35. stop the loop when the pet has died and output the age at which the pet lived up until

```python
while True:
  printPet()
  threeActivities()
  nextDay()
  randomMisfortune()
  if checkGameOver():
    print(pet["name"] + " has disappeared at the age of " + str(pet["age"]))
    break
```
