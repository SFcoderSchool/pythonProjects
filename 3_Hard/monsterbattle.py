import random

pikachu = {
    "name": "Pikachu",
    "health": 100,
    "defense": 20,
    "attack": 20
}

pidgey = {
    "name": "Pidgey",
    "health": 100,
    "defense": 20,
    "attack": 20
}

#monster1 will do damage to monster2
def attack(mon1, mon2):
    print(mon1["name"] + " has attacked " + mon2["name"])
    mon2["health"] -= mon1["attack"] - mon1["attack"] * (mon2["defense"]/100)
    print(mon2["name"] + "'s health " + str(mon2["health"]))

#lowers the attack of the selected monster
def growl(mon1, mon2):
    print(mon1["name"] + " used growl!")
    print(mon2["name"] + "'s attack lowered!")
    mon2["attack"] -= 5

def tailWhip(mon1,mon2):
    print(mon1["name"] + " used tail whip!")
    print(mon2["name"] + "'s defense lowered!")
    mon2["defense"] -= 5

def growth(mon):
    print(mon["name"] + "'s attack rose!")
    mon["attack"] += 5

def curl(mon):
    print(mon["name"] + "'s defense rose!")
    mon["defense"] += 5

while True:
    print(pidgey)
    print(pikachu)
    print("Your Pikachu moves: attack, growl, tail whip, growth, curl")
    choice = input("What would you do?")
    if choice == "attack":
        attack(pikachu, pidgey)
    if choice == "growl":
        growl(pikachu, pidgey)
    if choice == "tail whip":
        tailWhip(pikachu, pidgey)
    if choice == "growth":
        growth(pikachu)
    if choice == "curl":
        curl(pikachu)
    
    if pidgey["health"] <= 0:
        print("Pidgey has fainted")
        break

    dice = random.randint(1,5)
    if dice == 1:
        attack(pidgey, pikachu)
    if dice == 2:
        growl(pidgey, pikachu)
    if dice == 3:
        tailWhip(pidgey, pikachu)
    if dice == 4:
        growth(pidgey)
    if dice == 5:
        curl(pidgey)

    if pikachu["health"] <= 0:
        print("Pikachu has fainted")
        break