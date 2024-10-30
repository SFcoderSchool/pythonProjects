#The main focus of this project is the Factory design where a class/object has the job of generating new objects.
#Also a good showcase of two seperate objects, Factory and Shop, interacting with each other through the use of functions and parameters to transfer shipment data.

#######PART 1##############
#1) write a class to represent a virtual Item with a name and price
#2) program a class Factory with a catalog of item names
#3) write a function where the Factory produces an Item object with a random name from the catalog and a random price
#########Part 2###########
#1) program a class Shop to represent a virtual Shop
#2) the shop requires a list of inventory to represent what the shop has avaliable for sale
#3) program a restock function with a parameter to accept outside data into the function
#   -append the parameter data to the inventory list
#4) program a sell function that will randomly pick a random item from the inventory list and sell it
###########Part 3##########
#1) generate a Factory object
#2) generate a Shop object
#3) tell the Factory to makeItem and store the returned data to a variable, shipment
#4) activate the restock function in the Shop and transfer the shipment data to the parameters of the function
#5) repeat 10 times
#6) tell the Shop to sell items 5 times

import random

class Item:
  def __init__(self, name, price):
    self.name = name
    self.price = price

class Factory:
  def __init__(self):
    self.catalog = ['chocolate', 'gummy candies', 'coloring books', 'crayons', 'toy cars', 'bubbles', 'stickers', 'snack packs', 'juice boxes', 'balloons', 'straws', 'soda', 'stuffed animals', 'sidewalk chalk', 'toothbrush', 'jelly', 'vitamins', 'silly putty', 'books', 'handheld games', 'slime']
  def makeItem(self):
    index = random.randint(0, len(self.catalog)-1)
    name = self.catalog[index]
    price = random.randint(5,10)
    return Item(name,price)


class Shop:
  def __init__(self):
    self.inventory=[]
    self.money = 0
  def restock(self, i):
    self.inventory.append(i)
    print("Received " + i.name + " as shipment.")
  def sell(self):
    index = random.randint(0, len(self.inventory)-1)
    item = self.inventory.pop(index)
    self.money += item.price
    print("Sold " +item.name+". Gained $" + str(item.price))


myFactory = Factory()
myShop = Shop()

for i in range(10):
  shipment = myFactory.makeItem()
  myShop.restock(shipment)


for i in range(5):
  myShop.sell()