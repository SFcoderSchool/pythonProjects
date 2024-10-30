score = 0

print("1. If a backyard is 50 feet long and 20 feet wide, how many square feet is the yard?")
answer = input()
if "1000" in answer: #flexible answer to include sq ft
  print('you are correct')
  score = score + 1
else: 
  print("you are incorrect")


print("2. On the periodic table, which element is represented by the letter N?")
answer = input()
if answer.lower() == "nitrogen": #flexible answer for case sensitivity
  print('you are correct')
  score = score + 1
else: 
  print("you are incorrect")


print("3. How many feet are there in 75 yards?")
answer = input()
if "225" in answer:
  print('you are correct')
  score = score + 1
else: 
  print("you are incorrect")


print("4. What gas do humans need in order to live?")
answer = input()
if answer.lower() == "oxygen":
  print('you are correct')
  score = score + 1
else: 
  print("you are incorrect")


print("5. Who invented the lightbulb?")
answer = input()
if answer.lower() == "thomas edison":
  print('you are correct')
  score = score + 1
else: 
  print("you are incorrect")


print("6. What are the large rocks that orbit the sun between Mars and Jupiter called?")
answer = input()
if "asteroid" in answer.lower(): #includes asteroid or asteroids
  print('you are correct')
  score = score + 1
else: 
  print("you are incorrect")


print("7. Maine borders which U.S. state?")
answer = input()
if answer == "New Hampshire": #strict and requires Capitalized letters
  print('you are correct')
  score = score + 1
else: 
  print("you are incorrect")


print("8. Whose picture is on the five-dollar bill?")
answer = input()
if "Abraham Lincoln" in answer: #can include President Abraham Lincoln but must be case sensitive
  print('you are correct')
  score = score + 1
else: 
  print("you are incorrect")


if score > 6:
  print("you are smarter than a fifth grader")
else:
  print("you are not smarter than a fifth grader")