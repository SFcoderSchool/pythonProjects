import readchar
import os
import random
from pprint import pprint

space = "_"
player = "♙"
enemy = "♞"
goal = "♚"
board = []
px = 0
py = 0
ex = 0
ey = 0
gx = 0
gy = 0

#generates the game 8x8 board

def generateBoard():
	global px, py, ex, ey, gx, gy, board
	board = []
	bsize = 8
	for x in range (bsize):
		row = []
		for i in range (bsize):
			row.append(space)
		board.append(row)
		
	#placing the player on the map	
	py = random.randint(0,7)
	px = random.randint(0,7)
	board[py][px] = player

	#placing the enemy on the map
	ey = random.randint(0,7)
	ex = random.randint(0,7)
	board[ey][ex] = enemy

	gy = random.randint(0,7)
	gx = random.randint(0,7)
	board[gy][gx] = goal

#enemey will follow the player
#when the player is on the right side of the enemy, enemy moves right
#etc.
def enemyMovement():
	global ey, ex, py, px
	rmove = random.randint(1, 4)
	board[ey][ex] = space
	if px > ex:
		ex += 1
	elif px < ex:
		ex -= 1
	elif py > ey:
		ey += 1
	elif py < ey:
		ey -= 1
	board[ey][ex] = enemy

def playerMovement():
	global px, py
	k = readchar.readkey()
	board[py][px] = space
	if k == "w" and py != 0:
		py -= 1
	if k == "a" and px != 0:
		px -= 1
	if k ==	"s" and py != len(board) - 1:
		py += 1
	if k == "d" and px != len(board) - 1:
		px += 1
	board[py][px] = player	

def checkWin():
	if px == gx and py == gy:
		return True
	return False

def checkLoss():
	if ex == px and ey == py:
		return True
	return False

generateBoard()

while True:
	pprint(board)
	playerMovement()
	
	enemyMovement()

	if checkWin():
		generateBoard()

	os.system("cls")
	if checkLoss():
		print("You lose")
		break	