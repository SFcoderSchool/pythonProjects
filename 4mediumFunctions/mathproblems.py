

def area(w,l):
  print(w*l)

def perimeter(w,l):
  print(2*w+2*l)

def circlearea(r):
  print(3.14*r*r)

def circumference(r):
  print(2*3.14*r)

def trianglearea(b,h):
  print(b*h/2)

def addition(a, b):
  print(a+b)

def subtraction(a,b):
  print(a-b)

def multiplication(a,b):
  print(a*b)

def division(a,b):
  print(a/b)

def exponent(a,b):
  print(a**b)

print("What would you like to do?")
print("1. Area")
print("2. Perimeter")
print("3. Circle Area")
print("4. Circle Perimeter")
print("5. Triangle Area")
print("6. Addition")
print("7. Subtraction")
print("8. Multiplication")
print("9. Division")
print("10. Exponent")
answer = input()

if answer == "1":
  print("What is the width?")
  width = input()
  print("What is the length?")
  length = input()
  area(int(width),int(length))

if answer == "2":
  print("What is the width?")
  width = input()
  print("What is the length?")
  length = input()
  perimeter(int(width),int(length))

if answer == "3":
  print("What is the radius?")
  radius = input()
  circlearea(int(radius))

if answer == "4":
  print("What is the radius?")
  radius = input()
  circumference(int(radius))

if answer == "5":
  print("What is the base?")
  base = input()
  print("What is the height?")
  height = input()
  trianglearea(int(base),int(height))

if answer == "6":
  print("What is the first number?")
  firstnumber = input()
  print("What is the second number?")
  secondnumber = input()
  addition(int(firstnumber),int(secondnumber))

if answer == "7":
  print("What is the first number?")
  firstnumber = input()
  print("What is the second number?")
  secondnumber = input()
  subtraction(int(firstnumber),int(secondnumber))

if answer == "8":
  print("What is the first number?")
  firstnumber = input()
  print("What is the second number?")
  secondnumber = input()
  multiplication(int(firstnumber),int(secondnumber))

if answer == "9":
  print("What is the first number?")
  firstnumber = input()
  print("What is the second number?")
  secondnumber = input()
  division(int(firstnumber),int(secondnumber))

if answer == "10":
  print("What is the first number?")
  firstnumber = input()
  print("What is the second number?")
  secondnumber = input()
  exponent(int(firstnumber),int(secondnumber))

