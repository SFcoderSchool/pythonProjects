# LootBoxes
# Difficulty:⭐⭐⭐⭐
# recieve randomly from a bunch of items, and see how valuable your collection is

# Steps:
# 1. create a dictionary of 5 items with the item as the key and the price as the value
# 2. pull all the keys from the dictionary and save it 
# 3. NOTE: this is not a list, require to convert to a list

# 4. create an empty list to save all of the pulls you received 
# 5. use input to pause the code 
# 6. randomly pick an item from the keys list and add it to the inventory

# 7. add a for loop to repeat 10 times
# 8. calculate the worth of all the items received

# 9. go through each item stored in the inventory
# 10. output the cost of each item
# 11. save the cost into a variable
# 12. output the total value of the item

# Bonus:
# 1. output the count of each item


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

items = itemsDiction.keys()
items = list(items)

inventory = []

for i in range(10):
    input("Press Enter to get a lootbox:")
    prize = items[random.randint(0,len(items)-1)]
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

