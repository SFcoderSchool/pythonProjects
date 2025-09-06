import random
import time
import os

emojis = ["💰","💎","👌","❤️ ","😎","💀","👻","👽","💩","🦄"]
blank = "⬜"
board = []
answerkey = []

def generateBoard():
    global board, answerkey
    board = []
    for i in range(4):
        row = []
        for j in range(5):
            row.append(blank)
        board.append(row)
    answerkey = []
    e = []
    for i in range(10):
        e.append(emojis[i])
        e.append(emojis[i])
    random.shuffle(e)
    for i in range(4):
        row = []
        for j in range(5):
            row.append(e.pop(0))
        answerkey.append(row)

def printBoard():
    os.system("clear || cls")
    for i in range(4):
        print(" ".join(board[i]))

def makemove():
    global board, answerkey
    row = int(input("Row: "))
    col = int(input("Col: "))
    if board[row][col] != blank:
        print("That space is already filled")
        time.sleep(1)
        return
    board[row][col] = answerkey[row][col]
    printBoard()
    time.sleep(1)
    row2 = int(input("Row: "))
    col2 = int(input("Col: "))
    if board[row2][col2] != blank:
        print("That space is already filled")
        board[row][col] = blank
        time.sleep(1)
        return
    board[row2][col2] = answerkey[row2][col2]
    printBoard()
    time.sleep(1)
    if board[row][col] != board[row2][col2]:
        board[row][col] = blank
        board[row2][col2] = blank
        printBoard()


generateBoard()
while True:
    printBoard()
    makemove()
