import os
catalog = ["toy","food","furniture","tech","fruits"]


shopping_cart = []

def print_catalog():
  for i in range(len(catalog)):
    print(i,catalog[i])


def select_item():
  num = input("Which item would you like to buy? (-1 to quit)")
  num = int(num)
  if num == -1:
    return "quit"
  item = catalog[num]
  shopping_cart.append(item)
  return "continue"

def checkout():
  total = len(shopping_cart) * 4
  return total

while True:
  os.system("clear")
  print(shopping_cart)
  print_catalog()
  ans = select_item()
  if ans == "quit":
    price = checkout()
    print("Your total is: ", price)
    break