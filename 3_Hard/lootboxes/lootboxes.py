import random
itemsDiction = {
    "glasses": 3,
    "gloves": 2,
    "shoes": 2,
    "bag": 3,
    "sweater": 5,
    "shirt": 5,
    "pants": 5,
    "hoodie": 6,
    "necklace": 10,
    "ring": 14
}

items = list(itemsDiction.keys())

inventory = []

for i in range(10):
    input("Press Enter to get a lootbox:")
    prize = items[random.randint(0,9)]
    print("You got a:", prize)
    inventory.append(prize)


print("Worth of all prizes!")
cash = 0
for i in range(len(inventory)):
    keyName = inventory[i]
    money = itemsDiction[keyName]
    print(keyName, "is worth", money)
    cash += money

print("Its all worth", cash)

