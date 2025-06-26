# Glass Bridge
# Based off of the squid game / mr.beast bridge game
# Create a list of valid sides for the user to walk on; either left or right. See how far the user can travel without guessing wrong.
# restart again when the user guesses wrong and falls off

# Steps
# 1. create an empty list called glassBridge
# 2. fill the list with 10 coin flips for "left" or "right"

# 3. ask the user to pick left and right
# 4. check to see if the first choice in the bridge matches with their guess
# 5. if it did then say "congrats", if not then say "failed"

# 6. track the position on the bridge with a variable called rowNum
# 7. replace the index in the list to use rowNum instead of just index 0

# 8. add a while True loop and repeat
# 9. increment the rowNum if they got it correct
# 10. set back to 0 if they got it incorrect

# 11. stop the game when they reach the end

import random


glassBridge = []
for i in range(10):
  coin = random.randint(1,2)
  if coin == 1:
    glassBridge.append("left")
  else:
    glassBridge.append("right")


rowNum = 0
while True:
  print("row:",rowNum,"🪟 🪟 ")
  choice = input("left or right glass?")

  if glassBridge[rowNum] == choice:
    print("CONGRATZ you move forward to the next row! 🔝")
    rowNum = rowNum + 1
  else:
    print("OH NO THE GLASS WAS FAKE YOU FELL OFF 🧗")
    print("start from the beginning again")
    rowNum = 0

  if rowNum == 10:
    print("You reached the end! you win!")
    break