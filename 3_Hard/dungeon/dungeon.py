# Dungeon
# Difficulty: ⭐⭐⭐⭐
# Enter a dungeon as the player and retrieve the goal while avoiding the enemies

# Steps:

# Generate board
# 1. create an empty board list
# 2. add 10 rows list into the board
# 3. add 10 "_" into each row

# 4. print out the each row in the board
# 5. NOTE: convert this process into a function 

# 6. create a variable for the player and save an emoji in it
# 7. randomly pick a random row for the player
# 8. randomly pick a random col for the player
# 9. place the player into its randomly chosen place and printBoard to test

# 10. repeat for the goal

# 11. create a count for the amount of enemies to spawn
# 12. create an empty list for enemies rows
# 13. create an empty list for enemies columns
# 14. add random numbers into the list for however many enemies there are
# 15. for all enemies put them onto the board

# Player movement
# 16. use readchar.readkey() and check the user input
# 17. depending on their input, move the piece accordingly

# 18. NOTE: piece may go out of bounds
# 19. add checks to make sure piece does not go out of bounds

# Enemy movement
# 20. for all enemies
# 21. generate a random number from 1 to 4
# 22. depending on the number, reset the current position back to blank, move the piece accordingly

# 23. NOTE: piece may go out of bounds
# 24. add checks to make sure piece does not go out of bounds

# Check for game over states 
# 25. check to see if the player coordinates are on the goal coordinates
# 26. check to see if the player coordinates are on any of the enemy coordinates

# Simplify
# 27. NOTE: adding a while True: to the game would be very long and confusing; should make functions
# 28. convert the generate game board / pieces into a function
# 29. convert the player movement into a function
# 30. convert the enemy movement into a function
# 31. convert the update characters into a function
# 32. convert the logic for loss into a function
# 33. convert the logic for win into a function

# Final Game Logic
# 34. start a while True and repeat the steps for the game
# 35. playermovement, enemymovement, drawcharacters
# 36. if win then generate a new board with new positions
# 37. if loss then break the loop and say you lose
# 38. clear and print wherever needed

# Bonus
# 1. update code where a new enemy spawns after each level
# 2. update code to allow use to enter how big they would like the board

import readchar
import os
import random

space = "⬜"
player = "🙂"
enemy = "👿"
goal = "🍔"

board = []
bsize = 10

pcol = 0
prow = 0
esize = 10
ecol = []
erow = []
gcol = 0
grow = 0

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

def printBoard():
	for i in range(bsize):
		print(" ".join(board[i]))

def enemyMovement():
	global erow, ecol

	for i in range(esize):
		board[erow[i]][ecol[i]] = space

		rmove = random.randint(1,4)
		if rmove==1 and ecol[i] != len(board) - 1 and ecol[i] + 1 != gcol:
			ecol[i] += 1
		elif rmove==2 and ecol[i] != 0 and ecol[i] - 1 != gcol:
			ecol[i] -= 1
		elif rmove==3 and erow[i] != len(board) - 1 and erow[i] + 1 != grow:
			erow[i] += 1
		elif rmove==4 and erow[i] != 0 and erow[i] - 1 != grow:
			erow[i] -= 1

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
	for i in range(len(ecol)):
		board[erow[i]][ecol[i]] = enemy
	board[grow][gcol] = goal
	board[prow][pcol] = player

def checkWin():
	if pcol == gcol and prow == grow:
		return True
	return False

def checkLoss():
	for i in range(len(ecol)):
		if ecol[i] == pcol and erow[i] == prow:
			return True
	return False



generateBoard()
drawCharacters()
os.system("clear || cls")

while True:
	printBoard()
	playerMovement()
	enemyMovement()

	drawCharacters()

	if checkWin():
		generateBoard()
		drawCharacters()

	os.system("clear || cls")
	if checkLoss():
		print("You lose")
		break	