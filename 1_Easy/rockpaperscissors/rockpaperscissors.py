# RockPaperScissors
# Difficulty:
# simulates rock paper scissors against the computer

# Steps:
# 1. identify that the computer will represent 1 as rock, 2 as paper, 3 as scissors
# 2. generate a random number from 1 to 3 
# 3. depending on the number, output rock, paper, or scissors

# 4. ask the user to enter in a number 1 to 3 depending on the what they would like to choose

# 5. check to see if the user typed in "1" and the computer chose 1, output tie
# 6. repeat for all of the situations when the user types in "1"

# 7. repeat for all other situations and output tie, win, loss accordingly

# Bonus:
# 1. add a repeat and keep track of how many wins you get
# 2. stop the game when points have reached 3 or -3

import random

points = 0
while True:
  choice = input("Do you want to use 1)rock 2)paper 3)scissors? ")
  
  computer = random.randint(1,3)
  
  if choice=='1' and computer==1:
    print("Player throws rock, computer throws rock, tie!")
  if choice=='1' and computer==2:
    print("Player throws rock, computer throws paper, you lose!")
    points=points-1
  if choice=='1' and computer==3:
    print("Player throws rock, computer throws scissors, you win!")
    points=points+1
  
  if choice=='2' and computer==1:
    print("Player throws paper, computer throws rock, you win!")
    points=points+1
  if choice=='2' and computer==2:
    print("Player throws paper, computer throws paper, tie!")
  if choice=='2' and computer==3:
    print("Player throws paper, computer throws scissors, you lose!")
    points=points-1
  
  if choice=='3' and computer==1:
    print("Player throws scissors, computer throws rock, you lose!")
    points=points-1
  if choice=='3' and computer==2:
    print("Player throws scissors, computer throws paper, you win!")
    points=points+1
  if choice=='3' and computer==3:
    print("Player throws scissors, computer throws scissors, tie!")

  print(points)
  if points==3:
    print("You win the whole game! :)")
    break
  if points==-3:
    print("You lose the whole game :(")
    break