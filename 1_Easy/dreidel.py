import random
#both players start with 10 coins
player = 10
computer = 10
table = 0
while True:
  #both players put a coin on the table
  player = player - 1
  computer = computer - 1
  table = table + 2
  #player spins the dreidel
  input("Press enter to spin the dreidel!")
  dreidel = random.randint(1,4)
  if dreidel == 1:
    print("nun, you get nothing")
  if dreidel == 2:
    print("gimel, you get all coins on table")
    player = player + table
    table = 0
  if dreidel == 3:
    print("hay, you get half the coins on the table")
    reward = int(table/2)
    player = player + reward
    table = table - reward
  if dreidel == 4:
    print("shin, you lose 1 coin")
    player = player - 1
    table = table + 1
  #computer spins the dreidel
  input("Computer's turn to spin the dreidel!")
  dreidel = random.randint(1,4)
  if dreidel == 1:
    print("nun, computer get nothing")
  if dreidel == 2:
    print("gimel, computer get all coins on table")
    computer = computer + table
    table = 0
  if dreidel == 3:
    print("hay, computer get half the coins on the table")
    reward = int(table/2)
    computer = computer + reward
    table = table - reward
  if dreidel == 4:
    print("shin, computer lose 1 coin")
    computer = computer - 1
    table = table + 1
  print("your coins", player)
  print("computer coins", computer)
  if player <= 0:
    break
  if computer <= 0:
    break