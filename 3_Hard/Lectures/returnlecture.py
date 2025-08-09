#Lecture on return statements
#Think of a function as a math equation.
#A typical math equation like area of a rectangle
#area = width x length
#All you need to do is plug in a number for width and length and it will calculate the area for you.
#We've already been doing something similar with parameters.

def area(width, length):
  ans = width * length
  return ans

#just plug in a number to the width and length when using the function, it will automatically calculate area for you

area(8,9)

#the return statement allows the function to give away data that can be used for later

building = area(30,40)

#in this example the function area gives an answer which is then saved to the building variable
#Why is this a good thing? because then we can use the answer in more code later.
#Example:

building = area(40,40)
if building > 1500:
  print("The city is not happy.")
else:
  print("This building fits.")

#Now lets write some more functions that will do calculations for us.

def perimeter(w,l):
  return(2*w+2*l)

def circlearea(r):
  return(3.14*r*r)

def circumference(r):
  return(2*3.14*r)

def trianglearea(b,h):
  return(b*h/2)