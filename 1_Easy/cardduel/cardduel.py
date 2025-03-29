# Card Duel
# Difficulty: ⭐
# Gain a random card and duel against the computer's random card

# Steps
# 1. assign a number to player and computer and output the numbers

# 2. ask the user if they want to challenge the computer
# 3. if yes then check to see which is bigger
# 4. if no say denied

# 5. create a score and start it at 10
# 6. lose / gain the difference of the cards when they accept the duel
# 7. lose 1 point when they deny the challenge

# 8. randomize the cards

# 9. repeat the game 10 times (steps 1 to 7)

# 10. say you win if score is above 20

import random

score = 10

for i in range(10):
  playercard = random.randint(1,13)
  computercard = random.randint(1,13)
  print("Your card", playercard)
  choice = input("Do you challenge the computer to a duel?")
  if choice == "yes":
    print("The computer's card is", computercard)
    if playercard > computercard:
      print("You win!")
      diff = playercard - computercard
      score = score + diff
    elif playercard < computercard:
      print("You lose!")
      diff = computercard - playercard
      score = score - diff
    else:
      print("It's a tie!")
  else:
    print("You denied the challenge")
    score = score - 1

  print("score",score)

if score >= 20:
  print("You beated your opponent!")
elif score <= 0:
  print("You lost to your opponent!")
else:
  print("You tied with your opponent!")