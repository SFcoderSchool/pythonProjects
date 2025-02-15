import random

score = 0

while True:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice3 = random.randint(1,6)
    choice = input("Is it even or odd?")
    print("The dices:", dice1, dice2, dice3)
    total = dice1 + dice2 + dice3
    if choice == "even" and total % 2 == 0:
        print("You are correct!")
        score = score + 2
        #a bonus for evens! check if boxcar (triple 6)
        if dice1 == 6 and dice2 == 6 and dice3 == 6:
            print("boxcar! you were right AND hit the jackpot!")
            score = score * 6
    elif choice == "odd" and total % 2 == 1:
        print("You are correct!")
        score = score + 2
        #a bonus for odds! check if snake eyes (triple 1's)
        if dice1 == 1 and dice2 == 1 and dice3 == 1:
            print("snake eyes! you were right AND hit the jackpot!")
            score = score * 6
    else:
        print("You are wrong :(")

    print("Score:",score)

