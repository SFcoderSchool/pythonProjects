# USA State Capitals Quiz <br> ⭐⭐⭐⭐★★★★★★

## Background

A quiz of random States and Capitals

## Steps:

1. create a dictionary of 5 States and Capitals; State being the key and Capital being the value

```python
answers = {
  "California" : "Sacramento",
  "Montana" : "Helena",
  "Idaho" : "Boise",
  "Georgia" : "Atlanta",
  "Washington" : "Olympia"
}
```

2. get all the keys from the dictionary, which are all the states
3. convert the keys into a list and then shuffle

```python
import random

...

states = answers.keys()
states = list(states)
random.shuffle(states)
```

4. start with the first state and print it out
5. ask the user to guess the capital
6. check to see if the user got it correct by grabbing the value from the dictionary
7. output a correct reply if correct
8. output a incorrect reply if incorrect

```python
state=states[s]
print("What is the capital of",state+"?")
guess = input()
capital = answers[state]
if guess == capital:
  print("Correct")
else:
  print("Wrong the actual capital is",capital)
```

9. add a repeat to go through all of the states

```python
for s in range(0,len(states),1):
  state=states[s]
  print("What is the capital of",state+"?")
  guess = input()
  capital = answers[state]
  if guess == capital:
    print("Correct")
  else:
    print("Wrong the actual capital is",capital)
```

Bonus:

1. add more states and capitals

```python
answers = {
  "California" : "Sacramento",
  "Montana" : "Helena",
  "Idaho" : "Boise",
  "Georgia" : "Atlanta",
  "Washington" : "Olympia",
  "Maine" : "Agusta",
  "Rhode Island" : "Providence",
  "Texas" : "Austin",
  "Colorado" : "Denver",
  "Oklahoma" : "Oklahoma City",
  "New Jersey" : "Trenton",
  "New York" : "Albany",
  "Arkansas" : "Little Rock",
  "New Mexico" : "Santa Fe",
  "Wisconsin" : "Madison",
  "Ohio" : "Columbus",
  "Missouri" : "Jefferson City"
}
```

2. add a list of correct replies and pick a random reply to say

```python
if guess == capital:
  correct_replies = ["Correct,Good Job!", "Correct,Nice memory","Correct, You know your capitals!"]
  r = random.randint(0,len(correct_replies)-1)
  print(correct_replies[r])
```
