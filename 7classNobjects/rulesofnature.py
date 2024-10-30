import random

class Animal:
    def __init__(self,s):
        self.species = s
        self.fullness = random.randint(0,50)
        self.power = random.randint(0,50)
    def showStats(self):
        print("Name:", self.species)
        print("Fullness:",self.fullness)
        print("Power:",self.power)
    def eat(self, otherAnimal):
        print(self.species,"ate", otherAnimal.species)
        self.fullness += otherAnimal.fullness/2
        self.power += otherAnimal.power/2

#two test animals
animal1 = Animal("Lion")
animal2 = Animal("Bunny")

def clash(a1, a2):
    a1.showStats()
    a2.showStats()
    if a1.power > a2.power:
        a1.eat(a2)
    else:
        a2.eat(a1)

#activate test case
clash(animal1,animal2)


