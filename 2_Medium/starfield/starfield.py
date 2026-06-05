# Starfield
# fill a list with random star positions and sizes, draw them to simulate flying through space

# Steps
# - import turtle and random, set up the screen with a black background
# - create an empty list for star x positions
# - create an empty list for star y positions
# - create an empty list for star sizes

# - use a loop to fill each list with 100 random values
# - x positions should be random between -400 and 400
# - y positions should be random between -300 and 300
# - sizes should be random between 1 and 5

# - set up the turtle to draw dots with no delay
# - loop through the stars list using a counter from 0 to the length of the list
# - for each star, move the turtle to its x and y position
# - draw a dot using the size at the same index

# - add a second list for star brightness using random values between 1 and 3
# - use the brightness value to pick a color from a list of grey shades
# - draw each star with its matching color

# - add a speed list where each star has a random speed between 1 and 4
# - wrap the drawing in a while loop to animate the stars moving to the right
# - each frame add the star's speed to its x position
# - if a star moves past the right edge, reset its x to -400

# Bonus
# - add a list of star colors and randomly assign each star a color from the list
# - add a depth effect by making faster stars slightly larger


import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Starfield")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.penup()

star_x = []
star_y = []
star_size = []
star_brightness = []
star_speed = []

for i in range(100):
    star_x.append(random.randint(-400, 400))
    star_y.append(random.randint(-300, 300))
    star_size.append(random.randint(1, 5))
    star_brightness.append(random.randint(1, 3))
    star_speed.append(random.randint(1, 4))

shades = ["gray30", "gray60", "white"]

while True:
    t.clear()

    for i in range(len(star_x)):
        t.goto(star_x[i], star_y[i])
        t.dot(star_size[i], shades[star_brightness[i] - 1])

        star_x[i] = star_x[i] + star_speed[i]

        if star_x[i] > 400:
            star_x[i] = -400
            star_y[i] = random.randint(-300, 300)

    screen.update()

screen.mainloop()