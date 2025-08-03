# Hard Math Quiz
# generate math problems and try to solve them

# Steps:
# - Create a function called addition with 2 parameters (int, int) output the equation and return the answer
# - test the function with 2 numbers

# - generate 2 random numbers and pass them into the function
# - store the function return in a variable
# - ask the user to answer the equation printed by the function
# - check to see if they got it correct

# - repeat with subtraction, multiplication, division
# - NOTE: when doing division, round to the nearest 2 decimals
# - NOTE: convert input into a float when division is displayed

# - randomize what equation shows up

# Bonus
# - Make problems for exponents, area, perimeter, etc.
# - Add a repeat to keep the questions going
# - Keep a count of how many user got correct / incorrect


import random

def addition(a, b):
  equation = str(a) + "+" + str(b) + "=?"
  print(equation)
  answer = a+b
  return answer

def subtraction(a,b):
  equation = str(a) + "-" + str(b) + "=?"
  print(equation)
  answer = a-b
  return answer

def multiplication(a,b):
  equation = str(a) + "*" + str(b) + "=?"
  print(equation)
  answer = a*b
  return answer

def division(a,b):
  equation = str(a) + "/" + str(b) + "=? (round to 2 decimal places)"
  print(equation)
  answer = round(a/b, 2)
  return answer

# -----------------------------------------------------------------------------------------------

def exponent(a,b):
  equation = str(a) + " to the power of " + str(b) + "=?"
  print(equation)
  answer = a**b
  return answer

def area(w,l):
  print("What is the area with length " + str(l) + " and width " + str(w))
  answer = w * l
  return answer

def perimeter(w,l):
  print("What is the perimeter with length " + str(l) + " and width " + str(w))
  answer = 2*w+2*l
  return answer

def circlearea(r):
  print("What is the circle area with radius " + str(r))
  answer = 3.14 * r**2
  return answer

def circumference(r):
  print("What is the circumference with radius " + str(r))
  answer = 3.14 * r * 2
  return answer

def trianglearea(b,h):
  print("What is the triangle area with height " + str(h) + " and base " + str(b))
  answer = b*h/2
  return answer



problem = random.randint(1, 10)

if problem == 1:
  num1 = random.randint(1, 10)
  num2 = random.randint(1, 10)
  answer = addition(num1,num2)

if problem == 2:
  num1 = random.randint(1, 10)
  num2 = random.randint(1, 10)
  answer = subtraction(num1,num2)

if problem == 3:
  num1 = random.randint(1, 10)
  num2 = random.randint(1, 10)
  answer = multiplication(num1,num2)

if problem == 4:
  num1 = random.randint(1, 10)
  num2 = random.randint(1, 10)
  answer = division(num1,num2)

if problem == 5:
  num1 = random.randint(1, 10)
  num2 = random.randint(1, 10)
  answer = exponent(num1,num2)

if problem == 6:
  width = random.randint(1, 10)
  length = random.randint(1, 10)
  answer = area(width,length)

if problem == 7:
  width = random.randint(1, 10)
  length = random.randint(1, 10)
  answer = perimeter(width,length)

if problem == 8:
  radius = random.randint(1, 10)
  answer = circlearea(radius)

if problem == 9:
  radius = random.randint(1, 10)
  answer = circumference(radius)

if problem == 10:
  base = random.randint(1, 10)
  height = random.randint(1, 10)
  answer = trianglearea(base,height)


user = input("Answer: ")

if problem == 4:
  user = float(user)
else:
  user = int(user)

if user == answer:
  print("correct")
else:
  print("incorrect, it was", answer)