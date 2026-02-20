import random

player = []
computer = []

playerPoints = 0
computerPoints = 0

topCard = random.randint(1,13)

for i in range(5):
  player.append(random.randint(1,13))
  computer.append(random.randint(1,13))

while True:
  print("Player", playerPoints)
  print("Computer", computerPoints)

  print(player)
  print("Top Card", topCard)

  playable = False
  for i in range(len(player)):
    if player[i] >= topCard:
      playable = True

  if playable == True:
    user = input("Pick a Card to play: ")
    user = int(user)
    while player[user] < topCard:
      user = input("Pick a Card to play: ")
      user = int(user)

    topCard = player.pop(user)
    player.append(random.randint(1,13))
  else:
    print("No playable cards")
    computerPoints = computerPoints + 1

    print("New Top Card")
    topCard = random.randint(1,13)
    

  print("Computer Turn")
  # print(computer)
  print("Top Card", topCard)

  playable = False
  for i in range(len(computer)):
    if computer[i] >= topCard:
      playable = True
      
      topCard = computer.pop(i)
      computer.append(random.randint(1,13))
      print("Computer played", topCard)

      break

  if playable == False:
    print("Computer has no playable cards")
    topCard = random.randint(1,13)
    playerPoints = playerPoints + 1

  if playerPoints == 10 or computerPoints == 10:
    break

