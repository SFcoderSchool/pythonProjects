# Are you smarter than a 5th grader
# Difficulty:⭐
# A series of questions to check if you are smarter than a 5th grader

# Steps
# 1. Ask the user a question and allow them to answer
# 2. Check to see if the user is corrrect or incorrect

# 3. will run into issue with answers like "1000 sqft"

# 4. Repeat with more questions

# 5. will run into issue with answers like "Nitrogen"

# 6. provide questions and answers, allow students to work on more questions on their own

# 7. Create a score variable
# 8. Keep track of how many correct the user got
# 9. output if the user is smarter than a 5th grader or not

#Important!!!!!!!!!!!!!!!!!!!
#Show the students how to do the first two questions which allows you to utilize 'in' and lower() 

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


#Important!!!!!!!!!!!!!
#Now let the students do 6 more questions on their own.

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