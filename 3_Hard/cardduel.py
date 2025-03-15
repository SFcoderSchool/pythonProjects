import random

#both player gets a list of 5 cards
#they will select 1 card to play against each other
#the higher card gets a point
#game ends once they use up all their cards

playerscore = 0
computerscore = 0


playerhand = []
computerhand = []

def passCards():
  #making the player hand by giving them 5 random cards
  for i in range(5):
    playerhand.append(random.randint(1,13))
  #making the computer hand by giving them 5 random cards
  for i in range(5):
    computerhand.append(random.randint(1,13))

def printHand(list):
  for i in range(len(list)):
    print(i,":",list[i])

def selectPlayerCard():
  printHand(playerhand)
  num = input("Which card: ")
  num = int(num)
  return playerhand.pop(num)

def selectComputerCard():
  rnum = random.randint(0,len(computerhand)-1)
  return computerhand.pop(rnum)


passCards()


while len(playerhand) > 0:

  playercard = selectPlayerCard()
  computercard = selectComputerCard()

  #reveal both player's cards
  print("Player's card", playercard)
  print("Computer's card", computercard)
  
  #check who has the higher card and then assign points
  if playercard > computercard:
    playerscore = playerscore + 1
    print("Player's card beats the computer!")
  elif computercard > playercard:
    computerscore = computerscore + 1
    print("Computer's card beats the player!")
  else:
    print("Tie!")
  
#Lasty write a while or for loop that will stop once both players use up all their cards
#after the loop ends check who has the higher score
print("Player's score", playerscore)
print("Computer's score", computerscore)
if playerscore > computerscore:
  print("Player has won the game!")
elif computerscore > playerscore:
  print("Computer has won the game!")
else:
  print("TIE!")



