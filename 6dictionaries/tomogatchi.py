import random
from pprint import pprint

pet = {
    "name": "Pikachu",
    "health": 20,
    "belly": 20,
    "rest": 20,
    "happiness": 20,
    "age": 1
}

def feed():
    print("You feed " + pet["name"])
    pet["belly"] += random.randint(5,10)

def play():
    print("You played with " + pet["name"])
    pet["happiness"] += random.randint(5,10)
    pet["rest"] -= random.randint(5,10)
    pet["belly"] -= random.randint(5,10)

def sleep():
    print(pet["name"] + " went to sleep")
    pet["rest"] += random.randint(5,10)

def nextDay():
    pet["belly"] -= random.randint(5,10)
    pet["rest"] -= random.randint(5,10)
    pet["age"] += 1
    print("The day is over, everyone went to sleep, see you tomorrow.")



def randomMisfortune():
    dice = random.randint(1,6)
    if dice == 1:
        print(pet["name"] + " had a bad night.")
        pet["rest"] -= random.randint(5,10)
    if dice == 2:
        print(pet["name"] + " got sick :(")
        pet["health"] -= random.randint(5,10)
    if dice == 3:
        print(pet["name"] + " woke up on the wrong side of the bed and is now angry at you.")
        pet["happiness"] -= random.randint(10,20)
    if dice == 4:
        print(pet["name"] + " is extra hungry today.")
        pet["belly"] -= random.randint(5,10)

def checkGameOver():
    if pet["health"] <= 0:
        print("Your pet has died.")
        return True
    if pet["belly"] <= 0:
        print("Your pet has starved.")
        return True
    if pet["rest"] <= 0:
        print("Your pet is exhausted.")
        return True
    if pet["happiness"] <= 0:
        print("Your pet has ran away.")
        return True
    return False

def threeActivities():
    for i in range(3):
        print("What would you like to do?")
        choice = input("1)Feed 2)Play 3)Sleep ")
        if choice == "1":
            feed()
        if choice == "2":
            play()
        if choice == "3":
            sleep()

while True:
    pprint(pet)
    threeActivities()
    nextDay()
    randomMisfortune()
    if checkGameOver():
        print(pet["name"] + " has disappeared at the age of " + str(pet["age"]))
        break

