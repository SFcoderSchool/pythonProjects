# Kaleidoscope
# loop through a list of colors and angles to draw mirrored lines outward from the center

# Steps
# - import turtle and set up the screen with a black background
# - set turtle speed to 0 and hide the turtle

# - create a list of colors to cycle through
# - create a list of line lengths that grow larger each step
# - create a list of angles that the turtle rotates between each line

# - create a counter variable to track position in the color list
# - start a loop that runs for the length of the angles list
# - set the pen color using the color counter
# - draw a line forward using the matching length value
# - turn right by the matching angle value
# - add 1 to the color counter
# - if the color counter reaches the end of the colors list reset it to 0

# - add a second loop that mirrors the first by turning left instead of right
# - this creates the reflected side of the kaleidoscope
# - cycle through colors the same way using the counter

# - wrap both loops in an outer loop that repeats the full pattern multiple times
# - each repeat rotate the turtle slightly before starting
# - store the rotation amounts in a list and loop through them

# - add a third pass that draws shorter lines at a tighter angle between each main line
# - loop through the angles list again and draw a smaller line at half the length
# - rotate by a fraction of the original angle to fill in the gaps

# Bonus
# - add a list of pen sizes and change thickness each pass for a layered look
# - add a background redraw after each full rotation to create a fading trail effect


import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Kaleidoscope")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "violet", "magenta", "white"]
lengths = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 180, 160, 140, 120, 100, 80, 60, 40]
angles = [30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 150, 135, 120, 105, 90, 75, 60, 45]
rotations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180]

for r in range(len(rotations)):
  t.right(rotations[r])

  color_index = 0

  for i in range(len(angles)):
    t.pencolor(colors[color_index])
    t.forward(lengths[i])
    t.right(angles[i])
    color_index = color_index + 1
    if color_index == len(colors):
      color_index = 0

  color_index = 0

  for i in range(len(angles)):
    t.pencolor(colors[color_index])
    t.forward(lengths[i])
    t.left(angles[i])
    color_index = color_index + 1
    if color_index == len(colors):
      color_index = 0

  color_index = 0

  for i in range(len(angles)):
    t.pencolor(colors[color_index])
    t.forward(lengths[i] // 2)
    t.right(angles[i] // 3)
    color_index = color_index + 1
    if color_index == len(colors):
      color_index = 0

turtle.done()