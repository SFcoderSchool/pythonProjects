#1 Generate a random card value (hidden value)

#2 Generate a random card value (show value) and display this value

#3 allow user to guess if the shown card is higher or lower than the hidden card

#4 play until you get three correct


#5 how many attempts did it take to get 3 correct


import random

score = 0
attempts = 0

while True:

  hiddenCard = random.randint(1,13)
  shownCard = random.randint(1,13)
  
  print('hidden card: ?')
  print("card:",shownCard)
  answer = input("higher or lower: ")
  print('Hidden card:',hiddenCard)
  attempts = attempts + 1
  if answer == "higher":
    if hiddenCard > shownCard:
      print("Correct!")
      score = score + 1
    else:
      print("Wrong!")
  
  if answer == "lower":
    if hiddenCard < shownCard:
      print("Correct!")
      score = score + 1
    else:
      print("Wrong!")

  if score==3:
    break

  #for new line  
  print()

print("attempts: ",attempts)