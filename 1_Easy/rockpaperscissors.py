import random

#1) ask player to pick a move
#2) roll a random number to represent the move the player use against you
#3) check who wins with if statements
#4) look it so the game can be played forever
#bonus: keep track of score, game ends when first to reach 3 points

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