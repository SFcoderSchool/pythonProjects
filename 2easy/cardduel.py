import random


#pass out a playing card to both you and the computer
#get asked if you challenge the computer to a duel
#if yes then check if your card is higher than the computer's

#just like yugioh the score(lifepoint) you lose or gain is based on the difference between your card and the computer's

#lose point no matter what when denying the challenge

#your score is 10, 
#you win when you get above 20 score at the end

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