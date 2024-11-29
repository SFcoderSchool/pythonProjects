import readchar
import os
import random

thing = "_"
player = "♙"
enemy = "♞"
goal = "♚"


board = []
gsize = 8
for x in range (gsize):
	li = []
	for i in range (gsize):
		li.append(thing)
	board.append(li)
	
y = 0
x = 0
board[y][x] = player

enemyY = []
enemyX = []

for r in range (3):
	enemyY.append(random.randint(2, len(board) - 1))
	enemyX.append(random.randint(2, len(board) - 1))

for i in range (len(enemyY)):
	board[enemyY[i]][enemyX[i]] = enemy

def loadBoard():
	for b in range (gsize):
		print ("".join(board[b]))
loadBoard()


def enemyMovement(enemyY, enemyX):
	rmove = random.randint(1, 4)
	board[enemyY][enemyX] = thing
	if rmove == 1:
		enemyY += 1
	elif rmove == 2:
		enemyX += 1
	elif rmove == 3:
		enemyY -= 1
	elif rmove == 4:
		enemyX -= 1
	if enemyY < 0:
		enemyY = len(board) - 1
	elif enemyY > len(board) - 1:
		enemyY = 0
	elif enemyX < 0:
		enemyX = len(board) - 1
	elif enemyX > len(board) - 1:
		enemyX = 0
	return(enemyY, enemyX)

while True:
	k = readchar.readkey()
	board[y][x] = thing
	if k == "w" and y != 0:
		y -= 1
	if k == "a" and x != 0:
		x -= 1
	if k ==	"s" and y != len(board) - 1:
		y += 1
	if k == "d" and x != len(board) - 1:
		x += 1
	board[y][x] = player
	
	for i in range (len(enemyY)):
		enemyY[i], enemyX[i] = enemyMovement(enemyY[i], enemyX[i])
		board[enemyY[i]][enemyX[i]] = enemy
		os.system("cls")
		loadBoard()

	for i in range(len(enemyY)):
		if enemyY[i]==y and enemyX[i] == x:
			quit()

	if y == len(board) - 1 and x == len(board) - 1:
		board[y][x] = thing
		y = 0
		x = 0
		board[y][x] = player
		enemyY.append(random.randint(2, len(board) - 1))
		enemyX.append(random.randint(2,len(board) - 1))
		
		os.system("cls")
		loadBoard()