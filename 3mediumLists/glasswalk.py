import random

#this is similar to the squid game/mr. beast's glass walking game
#there is a left and right glass
#one side is weak glass and you will fall
#falling will make you start from the beginning again
#the other side will be strong glass and you get to move forward


#generating a list of correct answers
glassRoad = []
for i in range(10):
  coin = random.randint(1,2)
  if coin == 1:
    glassRoad.append("left")
  else:
    glassRoad.append("right")


#start a row number 0, the first pair of glass
rowNum = 0
while True:
  print("row:",rowNum,"🪟 🪟 ")
  choice = input("left or right glass?")
  #looking up the answer key for the row number
  #if the answer for the list index at rowNum matches your choice
  #you get to move forward
  if glassRoad[rowNum] == choice:
    print("CONGRATZ you move forward to the next row! 🔝")
    rowNum = rowNum + 1
  else:
    print("OH NO THE GLASS WAS FAKE YOU FELL OFF 🧗")
    print("start from the beginning again")
    rowNum = 0
  #if reached the end then stop the game you win!
  if rowNum == 10:
    print("You reached the end! you win!")
    break