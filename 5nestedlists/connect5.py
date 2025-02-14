import random
import os


def generateBoard():
    b = []
    for i in range(10):
        row = []
        for j in range(10):
            row.append("🔲")
        b.append(row)
    return b

def printBoard(b):
    os.system("clear")
    nums = []
    for i in range(len(b)):
        row = "".join(b[i])
        print(row,i)
        nums.append(str(i))
    print(" " + " ".join(nums))
    
    

def makeMove(piece, b):
    row = int(input("What row do you select? "))
    col = int(input("What col do you select? "))
    while b[row][col] != "🔲":
        row = int(input("Spot already taken, pick a new row: "))
        col = int(input("Spot already taken, pick a new col: "))
    b[row][col] = piece

def checkWinner(b):
    #checking horizontally if there are 5 in a row
    counter = 0
    for i in range(len(b)):
        for j in range(len(b[i])-1):
            if b[i][j] == b[i][j+1] and b[i][j] != "🔲":
                counter = counter + 1
            else:
                counter = 0
            if counter == 4:
                return b[i][j]
    #checking vertically if there are 5 in a column
    counter = 0
    for i in range(len(b[0])):
        for j in range(len(b)-1):
            if b[j][i] == b[j+1][i] and b[j][i] != "🔲":
                counter = counter + 1
            else:
                counter = 0
            if counter == 4:
                return b[j][i]
    #checking diagonally down right for a winner
    for i in range(len(b)-4):
        for j in range(len(b[i])-4):
            counter = 0
            for k in range(1,5):
                if b[i][j] == b[i+k][j+k] and b[j][i] != "🔲":
                    counter += 1
                if counter == 4:
                    return b[i][j]
    #checking diagonally up right for a winner
    for i in range(4,len(b)):
        for j in range(len(b[i])-4):
            counter = 0
            for k in range(1,5):
                if b[i][j] == b[i-k][j+k] and b[j][i] != "🔲":
                    counter += 1
                if counter == 4:
                    return b[i][j]
    return False




board = generateBoard()

while(True):
    printBoard(board)
    makeMove("🐙", board)
    if checkWinner(board) != False:
       printBoard(board)
       break
    printBoard(board)
    makeMove("🐷", board)
    if checkWinner(board) != False:
       printBoard(board)
       break