import random

#both player gets a list of 5 cards
#they will select 1 card to play against each other
#the higher card gets a point
#game ends once they use up all their cards

playerscore = 0
computerscore = 0

#making the player hand by giving them 5 random cards
playerhand = []
for i in range(5):
  playerhand.append(random.randint(1,13))

#making the computer hand by giving them 5 random cards
computerhand = []
for i in range(5):
  computerhand.append(random.randint(1,13))


#DO THIS WHILE LOOP or FOR LOOP LAST!
while len(playerhand) > 0:

  
  #show the player hand and ask them to play a card
  print(playerhand)
  num = int(input("Which card would you like to play?"))
  #pop the card from the player's hand and throw it out to play against the computer
  #Note: popping also removes the card from the list
  playercard = playerhand.pop(num)
  
  #computer pops a random card from their hand to throw against the computer
  num = random.randint(0,len(computerhand)-1)
  computercard = computerhand.pop(num)

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



