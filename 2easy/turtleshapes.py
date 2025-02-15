import turtle

screen = turtle.Screen()
screen.setup(1.0, 1.0)


bob = turtle.Turtle()
bob.shape("turtle")
bob.color("lightblue")

for i in range(4):
    bob.forward(100)
    bob.right(90)

for i in range(3):
    bob.forward(100)
    bob.right(120)

for i in range(5):
    bob.forward(100)
    bob.right(72)

for i in range(6):
    bob.forward(100)
    bob.right(60)

for i in range(8):
    bob.forward(100)
    bob.right(45)

screen.mainloop()