import random

#Create your story behind your project
print("Your plane crash lands on a deserted island. \n")

level1 = input("1. Search for food\n2. Search for water\n3. Search for shelter\n")

if level1 == "1":
  print("You find some fruits and berries. \n")
  level2 = input("1. Eat the berry\n2. Feed fruits and berries to a nearby squirrel\n3. Look for other options for food\n")
  if level2 == "1":
    print("You ate the poisonous berries and died. Game Over") #gameover
  elif level2 == "2":
    print("the squirrel dies from the poisonous berries! Phew! Close one!")
  elif level2 =="3":
    print("You find a coconut tree and eat the coconut. \n")


elif level1 == "2":
  print("You find a lake with pirahnas and get eaten. Game Over!\n") #GAMEOVER


elif level1 == "3":
  print("You find a cave \n")
  level2 = input("1. Enter the cave\n2. Look for other options\n")
  if level2 == "1":
    print("You enter the cave and find a treasure chest. \n")
  elif level2 == "2": 
    print("You find an abandon cabin")
    
   