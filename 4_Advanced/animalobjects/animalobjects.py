#PART 1: class attributes#
#write a class to represent an Animal in real life
#ask the student to think about what variables you can use to describe an animal

class Animal:
  def __init__(self):
    self.species = "dog"
    self.color = "brown"
    self.size = "medium"
    self.diet = "carnivore"

#generate the Animal character and store it into a variable

dog = Animal()
#print the dog as well as print out the seperate variables in the character
print(dog)
print(dog.species)
print(dog.color)
print(dog.size)
print(dog.diet)

#make a second Animal character
cat = Animal()
#show the student that you can access the variables in the object and modify them
cat.species = "cat"
cat.color = "orange"
cat.size = "small"
cat.diet = "carnivore"
#print the cat as well as print out the seperate variables in the character
print(cat)
print(cat.species)
print(cat.color)
print(cat.size)
print(cat.diet)

print()


#PART2: methods in the class
#I like to describe methods/functions in the class as what actions the virtual character can perform
#modify the class to include several methods/functions
class Animal:
  def __init__(self):
    self.species = "dog"
    self.color = "brown"
    self.size = "medium"
    self.diet = "carnivore"
  def selfIntro(self):
    print("Hi I am a "+ self.species)
    print("I am colored " + self.color)
    print("I am " +self.size)
    print("I like to eat " + self.diet)
  def sleep(self):
    print(self.species + " has went to sleep.")
  def eat(self):
    print(self.species + " went to eat " +self.diet)
  def play(self):
    print(self.species + " is playing around.")

dog = Animal()
cat = Animal()
cat.species = "cat"
cat.color = "orange"
cat.size = "small"
cat.diet = "carnivore"

dog.selfIntro()
cat.selfIntro()
dog.play()
cat.sleep()

print()

#PART3: initialize function
#let the student know that the __init__ function activates when creating the Animal character
#now we will modify the function so that it will have parameters to simplify the creation of new animals with different descriptors

class Animal:
  def __init__(self, sp, c, s, d):
    self.species = sp
    self.color = c
    self.size = s
    self.diet = d
  def selfIntro(self):
    print("Hi I am a "+ self.species)
    print("I am colored " + self.color)
    print("I am " +self.size)
    print("I like to eat " + self.diet)
  def sleep(self):
    print(self.species + " has went to sleep.")
  def eat(self):
    print(self.species + " went to eat " +self.diet)
  def play(self):
    print(self.species + " is playing around.")

dog = Animal("dog", "brown", "medium", "carnivore")
cat = Animal("cat", "orange", "small", "carnivore")
#create several more Animals using the new initialization method
horse = Animal("horse","brown","large","herbivore")
sheep = Animal("sheep","white","medium","herbivore")

dog.selfIntro()
cat.selfIntro()
horse.selfIntro()
sheep.selfIntro()

dog.play()
cat.sleep()
horse.play()
sheep.eat()