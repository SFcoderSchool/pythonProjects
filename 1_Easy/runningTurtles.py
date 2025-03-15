import turtle
import random

screen = turtle.Screen()
screen.setup(1.0, 1.0)


bob = turtle.Turtle()
bob.shape("turtle")
bob.color("lightblue")

jim = turtle.Turtle()
jim.shape("turtle")
jim.color("lightgreen")

kelly = turtle.Turtle()
kelly.shape("turtle")
kelly.color("pink")

while True:
    bob.forward(10)
    dice = random.randint(1,3)
    if dice == 1:
        bob.right(90)
    if dice == 2:
        bob.left(90)

    jim.forward(10)
    dice = random.randint(1,3)
    if dice == 1:
        jim.right(90)
    if dice == 2:
        jim.left(90)

    kelly.forward(10)
    dice = random.randint(1,3)
    if dice == 1:
        kelly.right(90)
    if dice == 2:
        kelly.left(90)



screen.mainloop()