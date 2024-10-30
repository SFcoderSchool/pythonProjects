import random
import time

catalog = {
    "apple": 2,
    "banana": 4,
    "pear": 2,
    "cherries": 5,
    "grapes": 4,
    "orange": 2
}

fruits = list(catalog.keys())

print(fruits)

cash = 0

for i in range(50):
    customerChoice = fruits[random.randint(0,5)]
    price = catalog[customerChoice]
    cash += price
    print("Customer bought", customerChoice, "for", price, "dollars")
    time.sleep(1)
print("You earned", cash, "today!")