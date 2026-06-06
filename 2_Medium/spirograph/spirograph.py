# Spirograph
# loop through a list of angles and colors to draw overlapping circles that build a pattern

# Steps
# - import turtle and set up the screen speed
# - create a list of colors to cycle through
# - create a list of angles to rotate by between each circle

# - create a variable to track the current color index
# - create a variable to track the current angle index

# - start a loop that runs for the length of the colors list
# - set the pen color to the current color using the color index
# - draw a circle using turtle.circle()

# - after drawing the circle, rotate the turtle by the current angle
# - move to the next color by adding 1 to the color index
# - move to the next angle by adding 1 to the angle index

# - add a second loop that draws a larger set of overlapping circles
# - this time iterate through the angles list and use each angle value as the circle size too
# - change pen color each time by stepping through the colors list using the loop counter

# - add a third pass that draws a full spirograph by looping 360 times
# - each iteration rotate by 1 degree and draw a small circle
# - cycle through the colors list by using the loop counter and checking when to reset it

# Bonus
# - create a list of different radii and loop through all three lists together using a counter
# - add a background color and change the pen size for thicker lines


import turtle

screen = turtle.Screen()
screen.setup(500,500)
screen.bgcolor("black")
screen.title("Spirograph")

t = turtle.Turtle()
t.speed(0)

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "violet", "white"]
angles = [91, 92, 93, 94, 95, 96, 97, 98]

color_index = 0
angle_index = 0

for i in range(len(colors)):
    t.pencolor(colors[color_index])
    t.circle(80)
    t.right(angles[angle_index])
    color_index = color_index + 1
    angle_index = angle_index + 1

for i in range(len(angles)):
    t.pencolor(colors[i])
    t.circle(angles[i] * 2)
    t.right(angles[i])

color_index = 0

for i in range(360):
    t.pencolor(colors[color_index])
    t.circle(100)
    t.right(1)
    color_index = color_index + 1
    if color_index == len(colors):
        color_index = 0

screen.mainloop()