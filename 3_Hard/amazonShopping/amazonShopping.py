import os
catalog = ["toy","food","furniture","tech","fruits"]
prices = [8,3,4,10,3]
budget = 100
total = 0

shopping_cart = []

def print_catalog():
  for i in range(len(catalog)):
    print(i,catalog[i])

def select_item(item):
  item = catalog[item]
  shopping_cart.append(item)

def checkout():
  total = len(shopping_cart) * 4
  print("Your total is: ", total)

while True:
  os.system("clear")
  print(shopping_cart)
  print_catalog()

  ans = input("Which item would you like to buy? (-1 to quit)")
  if ans == "-1":
    checkout()
    break

  ans = int(ans)
  cost = prices[ans]
  print("item costs", cost)
  
  if cost <= budget:
    select_item(ans)
    total = total + cost
    budget = budget - cost
  else:
    print("Not within the budget")
  