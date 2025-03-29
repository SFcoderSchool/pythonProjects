# Choose your own adventure <br> ⭐★★★★★★★★★

## Background

A text-based choice story. Try to survive till the end.

## Steps

1. output a statement for the background of the story
2. output the first choices the user can pick and allow the to pick
3. check to see what they inputted and output the message depending out their choice

```python
print("Your plane crash lands on a deserted island. \n")

level1 = input("1. Search for food\n2. Search for water\n3. Search for shelter\n")

if level1 == "1":
  print("You find some fruits and berries. \n")
elif level1 == "2":
  print("You find a lake with pirahnas and get eaten. Game Over!\n") #GAMEOVER
elif level1 == "3":
  print("You find a cave \n")
```

4. choose a choice and output the second choices to the user
5. check to see what they inputted and output the message depending out their choice
6. mark certain lines as gameover!

```python
if level1 == "1":
  print("You find some fruits and berries. \n")
  level2 = input("1. Eat the berry\n2. Feed fruits and berries to a nearby squirrel\n3. Look for other options for food\n")
  if level2 == "1":
    print("You ate the poisonous berries and died. Game Over") #GAMEOVER
  elif level2 == "2":
    print("the squirrel dies from the poisonous berries! Phew! Close one!")
  elif level2 =="3":
    print("You find a coconut tree and eat the coconut. \n")
```

7. continue adding more levels

```python
elif level1 == "3":
  print("You find a cave \n")
  level2 = input("1. Enter the cave\n2. Look for other options\n")
  if level2 == "1":
    print("You enter the cave and find a treasure chest. \n")
  elif level2 == "2":
    print("You find an abandon cabin")
```
