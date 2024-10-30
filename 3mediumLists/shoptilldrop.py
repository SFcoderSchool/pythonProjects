import random

items = ["1. Potatoes","2. Grapes","3. Chips","4. Water","5. Gummy Bears","6. Soap", "7. Pickles", "8. Vitamins"]

Costs = [5, 7, 4, 15, 3, 2, 6, 22]

wallet = random.randint(60,150)

print("wallet: ", wallet)

print("Inventory")
for i in range(len(items)):
  print(items[i], "$"+ str(Costs[i]))
  

while True:
  item = input("select item to purchase (s to checkout): ")
  if item == "s":
    break
  wallet = wallet - Costs[(int(item)-1)]

print("wallet: ", wallet)
if wallet < 1: 
  print("Arrested")
elif wallet < 4:
  print("you were very close to spending all your money")
else:
  print('you did not spend all your money!')
  

  
  