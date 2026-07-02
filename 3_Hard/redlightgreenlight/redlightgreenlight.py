import turtle
import random
import time
import os
player = turtle.Turtle()
cpu = turtle.Turtle()

screen = turtle.Screen()
screen.setup(1.0,1.0)

ref = turtle.Turtle()
ref.pensize(5)
ref.penup()
ref.goto(220,125)
ref.pendown()
ref.right(90)
ref.forward(250)
ref.hideturtle()

player.shape("turtle")
cpu.shape("turtle")
player.speed(0)
cpu.speed(0)
player.color("blue")
cpu.color("grey")
player.penup()
cpu.penup()
player.goto(-200,100)
cpu.goto(-200,-100)
player.pendown()
cpu.pendown()
time_passed = 0
playgame = True

def move():
  global playgame, time_passed, screen
  if lightcolor != "red":
    player.forward(10)
  if lightcolor == "red":
    playgame = False
    

screen.bgcolor("green")
start_time = time.time()

screen.onkey(move," ")
screen.listen()
lightcolor = "green"

while True:
  end_time = time.time()
  time_passed = end_time - start_time
  if time_passed > 7:
    lightcolor = "green"
    screen.bgcolor("green")
    start_time = time.time()
  elif time_passed > 5:
    lightcolor = "red"
    screen.bgcolor("red")
  elif time_passed > 4:
    lightcolor = "yellow"
    screen.bgcolor("yellow")
  
  if playgame == False:
    break    

 
  if lightcolor != "red":
    cpu.forward(.56)
  if cpu.xcor() > 220:
    print("Cpu won!")
    break
  elif player.xcor() > 220:
    print("Player won!")
    
    break
    

   

screen.exitonclick()