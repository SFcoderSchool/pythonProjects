# Halloween Candy <br> ⭐★★★★★★★★★

## Background

This project simulates a person trick-or-treating and going through a hundred
<br>houses asking for candy some houses give candy, some houses dont

## Steps

1. create a variable for total candy

```python
candy = 0
```

2. create a 1/4 chance that the house will give you candy
3. add 10 candy to total candy and output total candy

```python
import random

candy = 0

chance = random.randint(1,4)
if chance == 1:
  print("This house gave out candy")
  candy = candy + 10
else:
  print("This house did not give out any candy")

print("Total candy " + str(candy))
```

4. update code such that a random amount of candy will be added

```python
candy = candy + random.randint(1,10)
```

5. create a 1/10 chance for a ghost to steal a candy and output the total candy

```python
chance2 = random.randint(1,10)
if chance2 == 1:
  print("ghost stole a piece of candy")
  candy = candy - 1

print("Total candy " + str(candy))
```

6. start a loop to visit 100 houses loop steps 2 to 5

```python
for houses in range(0,100,1):
  chance = random.randint(1,4)
  if chance == 1:
    print("This house gave out candy")
    candy = candy + 10
  else:
    print("This house did not give out any candy")

  chance2 = random.randint(1,10)
  if chance2 == 1:
    print("ghost stole a piece of candy")
    candy = candy - 1

  print("Total candy " + str(candy))
```

## Bonus

1. create a GRAND PRIZE for 1/100 chance to gain a bonus prized (insert item here)

```python
chance3 = random.randint(1,100)
if chance3 == 1:
  print("You got the grand prize (insert item here)")
```

2. give the user a chance to trade in the prized (insert item here) for more candy

```python
chance3 = random.randint(1,100)
if chance3 == 1:
  print("You got the grand prize (insert item here)")
  user = input("would you like to trade in the item for some candy? (yes/no) ")
  if user == "yes":
    print("you get an extra 100 pieces of candy")
    candy = candy + 100
```

3. create a loop to output "eating..." for as many candies you have obtained

```python
print("You have " +str(candy) + " amount of candy")
for i in range(candy):
  print("eating.......")

print("I ate all the candy....")
```
