import random
import time

menu = {
    "pot stickers": 8,
    "tilapia": 12,
    "beef": 16,
    "pork": 15,
    "orange chicken": 14,
    "fried rice": 12
}

dishes = list(menu.keys())

print(dishes)

cash = 0

for i in range(50):
    customerChoice = dishes[random.randint(0,5)]
    price = menu[customerChoice]
    cash += price
    print("Customer bought", customerChoice, "for", price, "dollars")
    time.sleep(1)
print("You earned", cash, "today!")