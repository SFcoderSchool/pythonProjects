#1) write a class to represent a Student character
#2) give the Student variables name, score, and energy
#3) program a showId function that would print out the name, score, and energy of the Student
#4) use the class to create a Student object/character
#5) program functions that would allow the Student to perform the actions eat, sleep, play, study and then test them out
#6) create a randomAction function that would activate a random function, eat, sleep, play, or sleep


import random

class Student:
  def __init__(self, name):
    self.name = name
    self.score = 0
    self.energy = 100
  def showId(self):
    print("Name:", self.name)
    print("Score:", self.score)
    print("Energy:", self.energy)
  def eat(self):
    print(self.name + " is eatting food.")
    self.energy += random.randint(20,40)
  def sleep(self):
    print(self.name + " is sleeping.")
    self.energy = 100
  def play(self):
    print(self.name + " is playing games.")
    self.energy -= random.randint(20,40)
  def study(self):
    print(self.name + " is studying!")
    self.energy -= random.randint(20,40)
    self.score += random.randint(1,10)
  def randomAction(self):
    dice = random.randint(1,4)
    if dice == 1:
      self.eat()
    elif dice==2:
      self.sleep()
    elif dice==3:
      self.play()
    elif dice == 4:
      self.study()


jeff = Student("Jeff")
jeff.eat()
jeff.sleep()
jeff.play()
jeff.study()
jeff.randomAction()

names = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", "Ian", "Jenny"]

students = []

for i in range(10):
  s = Student(names[random.randint(0,len(names)-1)])
  students.append(s)


for days in range(90):
    print("Day",days)
    for i in range(10):
        students[i].randomAction()

for i in range(10):
  students[i].showId()