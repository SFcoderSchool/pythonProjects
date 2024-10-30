import random
import readchar
import time
import os

simon = []

letters = ["w","a","s","d"]

play = True

while play:
    chosen = letters[random.randint(0,3)]
    simon.append(chosen)

    for i in range(len(simon)):
        print(simon[i])
        time.sleep(0.5)
    os.system("clear || cls")


    for i in range(len(simon)):
        k = readchar.readkey()
        if k != simon[i]:
            print("You lose.")
            play = False
            break

