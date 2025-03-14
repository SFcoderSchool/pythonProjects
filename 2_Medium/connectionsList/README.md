# Connections

## Background

Based on the game from the New York Times, <a href="https://www.nytimes.com/games/connections" target="_blank">Connections</a>.

1. displays a grid of words
2. pick 4 words to attempt to create a connection
3. check to see if the connection is a valid connection

## Steps

1. create 4 list of topics with 4 words per topic
2. create a words list and append all the words from each topic into it

```python
cozy=["hotcocoa","stuffie","naps","fireplace"]
beauty=["comb","spa","makeup","shower"]
body=["hair","eyebrows","lips","foot"]
clothes=["skirt","dress","hat","sock"]

words=[]
for i in range(4):
  words.append(cozy[i])
  words.append(beauty[i])
  words.append(body[i])
  words.append(clothes[i])
```

3. shuffle the words list
4. loop through the words list and display each word

```python
import random

random.shuffle(words)
for i in range(len(words)):
  if i %4==0 and i !=0:
    print(" ")
    print(words[i],end=" |")
print()
```

5. create an empty list called choices
6. ask the user 4 times to enter a word
7. append their entered word into the choices list

```python
choices=[]
for i in range(4):
  answer=input("Enter a word: ")
  choices.append(answer)
```

8. check to see if choices matches any of the topics list
9. if there is then remove the words in choices from the words in the words list

```python
match=False
if choices == cozy:
  match = True
elif choices == beauty:
  match = True
elif choices == body:
  match = True
elif choices == clothes:
  match = True

if match==True:
  print("found match!")
  for i in range(len(choices)):
    words.remove(choices[i])
```

10. will run into issue where the choices don't match any topics list because the order is inconsistent
11. sort each topic list using .sort()
12. sort the choices list using .sort()

```python
cozy=["hotcocoa","stuffie","naps","fireplace"]
beauty=["comb","spa","makeup","shower"]
body=["hair","eyebrows","lips","foot"]
clothes=["skirt","dress","hat","sock"]

cozy.sort()
beauty.sort()
body.sort()
clothes.sort()

...

choices=[]
for i in range(4):
  answer=input("Enter a word: ")
  choices.append(answer)
choices.sort()
```

13. add a while True to repeat steps 4 - 11
14. add a condition to break the loop

```python
while True:
  random.shuffle(words)
  for i in range(len(words)):
    if i %4==0 and i !=0:
      print(" ")
    print(words[i],end=" |")
  print()

  choices=[]
  for i in range(4):
    answer=input("Enter a word: ")
    choices.append(answer)
  choices.sort()

  match=False
  if choices == cozy:
    match = True
  elif choices == beauty:
    match = True
  elif choices == body:
    match = True
  elif choices == clothes:
    match = True

  if match==True:
    print("found match!")
    for i in range(len(choices)):
      words.remove(choices[i])

  if len(words) == 0:
    break
```

15. create a lives variable before the while loop
16. lose a life when the choice does not match any topics
17. add condition to break the loop when no more lives

```python
lives = 4

while True:
  ...

  if match==True:
    print("found match!")
    for i in range(len(choices)):
      words.remove(choices[i])
  else:
    lives = lives - 1

  print("current lives " + str(lives))

  if len(words) == 0 or lives == 0:
    break
```

### Bonus

1. update the while statement to use a condition instead of break

```python
while len(words)>0 and lives>0:
```

2. use replit.clear() or os.system("clear") to clear consoles when game is running
