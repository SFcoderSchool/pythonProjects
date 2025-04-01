# Dungeon <br> ⭐⭐⭐⭐★★★★★★

## Background

Enter a dungeon as the player and retrieve the goal while avoiding the enemies

## Steps

### Generate Board

1. create an empty board list
2. add 10 rows list into the board
3. add 10 "\_" into each row

```python
board = []
bsize = 10
space = "⬜"

for i in range(bsize):
  row = []
  for j in range(bsize):
    row.append(space)
  board.append(row)
```

4. print out the each row in the board
5. NOTE: convert this process into a function

```python
def printBoard():
	for i in range(bsize):
		print(board[i])
```

6. create a variable for the player and save an emoji in it
7. randomly pick a random row for the player
8. randomly pick a random col for the player
9. place the player into its randomly chosen place and printBoard to test

```python
import random

player = "🙂"

prow = random.randint(0,bsize-1)
pcol = random.randint(0,bsize-1)

board[prow][pcol] = player

printBoard()
```

10. repeat for the goal

```python
goal = "🍔"

grow = random.randint(0,bsize-1)
gcol = random.randint(0,bsize-1)

board[grow][gcol] = goal

printBoard()
```

11. create a count for the amount of enemies to spawn
12. create an empty list for enemies rows
13. create an empty list for enemies columns
14. add random numbers into the list for however many enemies there are
15. for all enemies put them onto the board

```python
enemy = "👿"

erow = []
ecol = []
esize = 10

for i in range(esize):
  erow.append(random.randint(0,bsize-1))
  ecol.append(random.randint(0,bsize-1))

for i in range(len(ecol)):
  board[erow[i]][ecol[i]] = enemy

printBoard()
```

### PlayerMovement

16. use readchar.readkey() and check the user input
17. depending on their input, reset the current position back to blank, move the piece accordingly

```python
import readchar

k = readchar.readkey()
board[prow][pcol] = space
if k == "w":
  prow -= 1
if k == "a":
  pcol -= 1
if k ==	"s":
  prow += 1
if k == "d":
  pcol += 1
```

18. NOTE: piece may go out of bounds
19. add checks to make sure piece does not go out of bounds

```python
k = readchar.readkey()
board[prow][pcol] = space
if k == "w" and prow != 0:
  prow -= 1
if k == "a" and pcol != 0:
  pcol -= 1
if k ==	"s" and prow != len(board) - 1:
  prow += 1
if k == "d" and pcol != len(board) - 1:
  pcol += 1
```

### Enemy movement

20. generate a random number from 1 to 4
21. depending on the number, reset the current position back to blank, move the piece accordingly

```python
board[erow][ecol] = space

rmove = random.randint(1,4)
if rmove==1:
  ecol += 1
elif rmove==2:
  ecol -= 1
elif rmove==3:
  erow += 1
elif rmove==4:
  erow -= 1
```

22. NOTE: piece may go out of bounds
23. add checks to make sure piece does not go out of bounds

```python
board[erow][ecol] = space

rmove = random.randint(1,4)
if rmove==1 and ecol != len(board) - 1:
  ecol += 1
elif rmove==2 and ecol != 0:
  ecol -= 1
elif rmove==3 and erow != len(board) - 1:
  erow += 1
elif rmove==4 and erow != 0:
  erow -= 1
```

### Check for game over states

24. check to see if the player coordinates are on the goal coordinates
25. check to see if the player coordinates are on the enemy coordinates

```python
if pcol == gcol and prow == grow:
  print("reached goal!")

if pcol == ecol and prow == erow:
  print("gameover")
```

### Simplify

26. NOTE: adding a while True: to the game would be very long and confusing; should make functions
27. convert the generate game board / pieces into a function
28. convert the player movement into a function
29. convert the enemy movement into a function
30. convert the update characters into a function
31. convert the logic for loss into a function
32. convert the logic for win into a function

```python
def generateBoard():
  global pcol, prow, ecol, erow, gcol, grow, board, esize
  board = []
  erow = []
  ecol = []
  esize = 10

  for x in range (bsize):
    row = []
    for i in range (bsize):
      row.append(space)
    board.append(row)

  prow = random.randint(0,bsize-1)
  pcol = random.randint(0,bsize-1)

  for i in range(esize):
    erow.append(random.randint(0,bsize-1))
    ecol.append(random.randint(0,bsize-1))

  grow = random.randint(0,bsize-1)
  gcol = random.randint(0,bsize-1)


def enemyMovement():
	global erow, ecol

  board[erow][ecol] = space

  rmove = random.randint(1,4)
  if rmove==1 and ecol != len(board) - 1:
    ecol += 1
  elif rmove==2 and ecol != 0:
    ecol -= 1
  elif rmove==3 and erow != len(board) - 1:
    erow += 1
  elif rmove==4 and erow != 0:
    erow -= 1

def playerMovement():
	global pcol, prow
	k = readchar.readkey()
	board[prow][pcol] = space
	if k == "w" and prow != 0:
		prow -= 1
	if k == "a" and pcol != 0:
		pcol -= 1
	if k ==	"s" and prow != len(board) - 1:
		prow += 1
	if k == "d" and pcol != len(board) - 1:
		pcol += 1

def drawCharacters():
	board[erow][ecol] = enemy
	board[grow][gcol] = goal
	board[prow][pcol] = player

def checkWin():
	if pcol == gcol and prow == grow:
		return True
	return False

def checkLoss():
  if ecol == pcol and erow == prow:
    return True
	return False
```

### Final Gane Logic

33. start a while True and repeat the steps for the game
34. playermovement, enemymovement, drawcharacters

```python
generateBoard()
drawCharacters()

while True:
  printBoard()
  playerMovement()
  enemyMovement()
  drawCharacters()
```

35. if win then generate a new board with new positions
36. if loss then break the loop and say you lose
37. clear and print wherever needed

```python
while True:

  ...

  if checkWin():
    generateBoard()
    drawCharacters()

  os.system("clear")
  if checkLoss():
    print("You Lose")
    break
```

## Bonus

1. update code where a new enemy spawns after each level

2. update code to allow use to enter how big they would like the board
