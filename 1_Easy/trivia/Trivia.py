#Focus: \n and how to use it

score = 0


q = input("What does www stand for? \nwe were weird, well known web, world wide web, wizard waffle wagon: ")

if q == "world wide web":
  print("correct\n")
  score = score  + 1
else:
  print("incorrect\n")



q = input("Which game has a diamond sword? \nroblox, valorant, candy crush, minecraft: ")
if q == "minecraft":
  print("correct\n")
  score = score  + 1
else:
  print("incorrect\n")


q = input("Who bought twitter? \nmark zuckerburg, jeff bezos, elon musk, michelle obama: ")
if q == "elon musk":
  print("correct\n")
  score = score  + 1
else:
  print("incorrect\n")


q = input("When was Minecraft created? \n2011, 2004, 2009, 1989: ")
if q == "2011":
  print("correct\n")
  score = score  + 1
else:
  print("incorrect\n")



q = input("Most popular basketball player on Warriors? \nsteph curry, lebron james, kobe bryant, patrick beverley: ")
if q == "steph curry":
  print("correct\n")
  score = score  + 1
else:
  print("incorrect\n")


print("You got",score,"questions correct!")
