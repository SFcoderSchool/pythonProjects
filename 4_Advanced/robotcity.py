#The purpose of this project is to write a class and generate several objects with the class. Then use a list to store the object data and have it represent the population of the robot city. 

#1) write a Robot class to represent a robot character in the city
#2) give the Robot these variables name,job,fuel
#3) create parameter in the init function requiring a name and job as parameter when spawning the Robot
#4) write a function showInfo in the Robot class to print out all the variables in the Robot
#5) write a work function that will give the Robot the ability to work
#6) generate a Robot object
#7) tell the Robot to work then showInfo
#8) create 5 more Robots and put them into a list
#9) iterate through the list and tell them all to work
#10) have them work for 7 days
#11) at the end of the 7 days tell them to showInfo

import random

class Robot:
  def __init__(self, name, job):
    self.name = name
    self.job = job
    self.fuel=100
  def showInfo(self):
    print(self.name, self.job, self.fuel)
  def work(self):
    if self.fuel < 0:
      print(self.name + " has no more fuel to work.")
    else:
      print(self.name + " is working thier job as " + self.job)
      self.fuel -= random.randint(10,20)



names = ['Emma', 'Liam', 'Olivia', 'Noah', 'Ava', 'Isabella', 'Sophia', 'Mia', 'Charlotte', 'Amelia', 'Harper', 'Evelyn', 'Abigail', 'Emily', 'Elizabeth', 'Mila', 'Ella', 'Avery', 'Sofia', 'Camila']
jobs = ['Construction Worker', 'Electrician', 'Plumber', 'Carpenter', 'Landscaper', 'Chef', 'Hair Stylist', 'Fitness Instructor', 'Truck Driver', 'Janitor']

#generating a robot with a random name and a random job
index1 = random.randint(0, len(names)-1)
name = names[index1]
index2 = random.randint(0, len(jobs)-1)
job = jobs[index2]

robot1 = Robot(name,job)
#telling that robot to go to work and show their information
robot1.work()
robot1.showInfo()
#putting that robot into a list
robots = [robot1]
#generating 4 more robots and putting them into the list
for i in range(4):
  index1 = random.randint(0, len(names)-1)
  name = names[index1]
  index2 = random.randint(0, len(jobs)-1)
  job = jobs[index2]
  
  robot = Robot(name,job)
  robots.append(robot)

#make every robot go to work for 7 days
for days in range(7):
  print()
  print("Day:",days)
  for i in range(5):
    robots[i].work()

for i in range(5):
  robots[i].showInfo()