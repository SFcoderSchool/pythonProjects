#genereate a list of numbers with user input

#genereate a second list of random numbers representing the random numbers the computer picks


#forever roll a dice and cross out numbers that matches with your choices

#whoever crosses out all 3 numbers first wins

import random

playerChoices = []
computerChoices = []


for i in range(3):
    num = random.randint(1,9)
    computerChoices.append(num)

for i in range(3):
    num = input("Please enter a number for bingo: ")
    num = int(num)
    playerChoices.append(num)


while True:
    print("Player Nums:", playerChoices)
    print("Computer Nums:", computerChoices)
    input("Press enter to get a number")
    bingoNum = random.randint(1,9)
    print("Num:",bingoNum)
    if bingoNum in playerChoices:
        playerChoices.remove(bingoNum)
        print("Player Bingo!")
    if bingoNum in computerChoices:
        computerChoices.remove(bingoNum)
        print("Computer Bingo!")
    if len(playerChoices) == 0:
        print("Player wins!")
        break
    if len(computerChoices) == 0:
        print("Computer wins!")
        break
