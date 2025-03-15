import random

recommended = {
    "VR head set": 499,
    "television": 699,
    "computer": 1200,
    "gaming console": 499,
    "laptop": 299
}


items = list(recommended.keys())
cart = []

buying = True
while buying:
    print(items)
    choice = ""
    choice = input("What would you like to buy? ")
    if choice == "stop":
        buying = False
    elif choice in items:
        cart.append(choice)
    else:
        print("Item not available")
    
total = 0
for i in range(len(cart)):
    item = cart[i]
    price = recommended[item]
    total += price

print("Your total checkout is:", total)