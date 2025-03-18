########PART 1#############
#1) write a class to represent a Player character and give them some stats
#2) write a showInfo function to print out some of the stats of the character
#3) use the class to generate the Player object and activate the function to show the player's info

#4) repeat the same process for an Enemy character

########PART 2#############
# I like to describe functions as what abilities these virtual characters can perform
#5) write a attack function for the player to give them the ability to attack
#6) write a takeDamage function for the enemy to give them the ability to take damage
#7) activate both functions
#8) now repeate the process vice versa to give the enemy the ability to attack and the player the ability to take damage

########PART 3#############
#9) program more abilities for the player so that it is more similar to a RPG game
#   -program functions for the player to heal and defend
#10) program inputs to ask what action the player wants to perfrom
#11) surround it in a while loop so that the RPG game can continue on forever
#12) end the program when the enemy or player has no more hp
######### Bonus ############
# use mathematics to utilize the luck variable as a percent chance to increase your damage/heal/dodge

import random

class Player:
  def __init__(self):
    self.name = "Bob the Awesome"
    self.hp = 100
    self.att = 10
    self.defense = 10
    self.luck = 30
    self.defending = False
  def showInfo(self):
    print(self.name)
    print("HP:",self.hp)

  ######## Part 2 ##########
  def attack(self):
    print(self.name, "lifts their sword to attack!")
    ####Bonus Portion####
    if random.randint(1,100) < self.luck:
      print("Its a critical attack!")
      return(self.att*3)
    ####Bonus Portion####
    return(self.att)
  def takeDamage(self, number):
    ####Bonus Portion####
    if random.randint(1,100) < self.luck:
      print(self.name, "has dodged the attack!")
      return
    ####Bonus Portion####
    if self.defending == True:
      print(self.name, "has blocked the attack!")
      self.defending = False
    else:
      self.hp -= number
      print(self.name, "has taken", number, "damage!")

  ######## Part 3 ###########
  def heal(self):
    h = random.randint(5,15)
    ####Bonus Portion####
    if random.randint(1,100) < self.luck:
      h*=3
    ####Bonus Portion####
    self.hp += h
    print(self.name, "healed", h, "hp")
  def defend(self):
    print(self.name, "has prepared to defend!")
    self.defending = True
    
    
  
class Enemy:
  def __init__(self):
    self.name = "Todd the Liar"
    self.hp = 100
    self.att = 10
    self.defense = 10
    self.luck = 10
  def showInfo(self):
    print(self.name)
    print("HP:",self.hp)
    
  ######## Part 2 ##########
  def takeDamage(self, number):
    self.hp -= number
    print(self.name, "has taken", number, "damage!")
  def attack(self):
    print(self.name, "swings their dagger!")
    return(self.att)


###########Part 1################
player = Player()
player.showInfo()

enemy = Enemy()
enemy.showInfo()

###########Part 2################
damage = player.attack()
enemy.takeDamage(damage)

damage = enemy.attack()
player.takeDamage(damage)

###########Part 3################
while True:
  print()
  player.showInfo()
  enemy.showInfo()
  print("What should the player do:")
  print("1)attack")
  print("2)heal")
  print("3)defend")
  option = input()
  
  if option == "attack":
    damage = player.attack()
    enemy.takeDamage(damage)
  if option == "heal":
    player.heal()
  if option == "defend":
    player.defend()
  
  #enemy will always attack you in response
  damage = enemy.attack()
  player.takeDamage(damage)

  if enemy.hp <= 0:
    print("Player has defeated the enemy!")
    break
  if player.hp <= 0:
    print("Enemy has defeated the player!")
    break