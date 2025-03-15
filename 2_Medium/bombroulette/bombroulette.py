import random

# Based on the hit game "buckshot roulette" a 2 player russian roulette game!
# 1: generate a list of bombs either a dud or a real bomb
# 2: player decides if they will bomb themselves (russian roulette) or bomb the opponent
# 3: you want to throw a bomb at yourself because the duds will heal you
# 4: becareful when throwing a bomb at the computer because duds will heal them
# (HINT: there's 3 duds and 3 real bombs in the list, count how many are left before reloading)
# 5: computer's turn they make a random choice to bomb themselves or you

# Steps
# 1. define playerLives and computerLives variables
# 2. define bombs variable with an empty list
# 3. add 3 "dud" and 3 "bomb" into the list and then shuffle

# 4. display the playerLives and computerLives informatiion
# 5. display the bombsLeft using len()

# 6. ask the user if they would like to target (self / computer)
# 7. check to see if the bomb is "bomb" then say "it was a bomb" otherwise say "it was a dud"
# 8. make chosen target lose a life if it is a "bomb"
# 9. make chosen targets gain a life if it is a "dud"

# 10. the computer will pick target at random 1 and 2 (computer / player)
# 11. check to see if the bomb is "bomb" then say "it was a bomb" otherwise say "it was a dud"
# 12. make chosen target lose a life if it is a "bomb"
# 13. make chosen targets gain a life if it is a "dud"

# 14. check to see if bombs list is empty, if it is then add 3 "dud" and 3 "bomb" into the list and then shuffle

# 15. add a while True to repeat steps 4 to 12
# 16. include a condition to stop the game when either computer or player run out of lives

# bonus 1: update code to stop the while loop with a condition




bombs = []
for i in range(3):
  bombs.append("dud")
  bombs.append("bomb")
random.shuffle(bombs)

playerlives = 4
computerlives = 4


while playerlives>0 and computerlives>0:
  print("Your lives:", playerlives)
  print("Computer lives:", computerlives)
  print("Bombs left:", len(bombs))
  
  hand = bombs.pop(0)
  choice = input("who will you throw bomb at?")
  if hand == "bomb":
    print("it was a bomb")
    if choice == "self":
      print("you threw a bomb at yourself, lose a life")
      playerlives = playerlives - 1
    if choice == "computer":
      print("you threw a bomb at the computer, computer loses a life")
      computerlives = computerlives - 1
  else:
    print("it was a dud")
    if choice == "self":
      print("you threw a dud at yourself, gain a life")
      playerlives = playerlives + 1
    if choice == "computer":
      print("you threw a dud at the computer, computer gains a life")
      computerlives = computerlives + 1

  hand = bombs.pop(0)
  choice = random.randint(1,2)
  if hand == "bomb":
    print("it was a bomb")
    if choice == 1:
      print("computer threw a bomb at itself, lose a life")
      computerlives = computerlives - 1
    if choice == "computer":
      print("computer threw a bomb at you, you lose a life")
      playerlives = playerlives - 1
  else:
    print("it was a dud")
    if choice == 1:
      print("computer threw a dud at itself, gain a life")
      computerlives = computerlives + 1
    if choice == 2:
      print("computer threw a dud at you, computer gains a life")
      playerlives = playerlives + 1

  if len(bombs) <= 0:
    print("Reloading.....")
    for i in range(3):
      bombs.append("dud")
      bombs.append("bomb")
    random.shuffle(bombs)

  # if playerLives < 0 or computerLives < 0:
  #   break