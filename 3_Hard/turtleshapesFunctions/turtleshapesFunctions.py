# Shapes with Turtle and Functions
# Draw shapes with turtle and functions

# Steps:
# - setup the turtle environment

# - create bob the Turtle
# - draw a square with a for loop
# - convert that code to a function and use the function instead

# - repeat process with pentagon, triangle, hexagon, octagon
# - use all the functions and draw all the shapes

# - set a forever loop around all the shape functions
# - create a variable to pick a random shape to draw

# - create a teleport function
# - generate a random x and y
# - pick up the turtle pen and goto that position
# - put the pen back down

# - use the function before the drawing the shapes

# Bonus:
# - create a function to randomly set the color of the shapes
# - add a coin flip to determine whether to fill in the shape 

import turtle
import random

screen = turtle.Screen()
screen.setup(1.0, 1.0)


bob = turtle.Turtle()
bob.shape("turtle")
bob.color("lightblue")

def square():
    for i in range(4):
        bob.forward(100)
        bob.right(90)

def triangle():
    for i in range(3):
        bob.forward(100)
        bob.right(120)

def pentagon():
    for i in range(5):
        bob.forward(100)
        bob.right(72)

def hexagon():
    for i in range(6):
        bob.forward(100)
        bob.right(60)

def octogon():
    for i in range(8):
        bob.forward(100)
        bob.right(45)

def teleport():
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)

    bob.penup()
    bob.goto(x,y)
    bob.pendown()

while True:
    teleport()

    shape = random.randint(1,5)
    if shape == 1:
        square()
    elif shape == 2:
        triangle()
    elif shape == 3:
        pentagon()
    elif shape == 4:
        hexagon()
    elif shape == 5:
        octogon()

screen.mainloop()