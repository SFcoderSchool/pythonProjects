import random

#PART 1
####generate a dice and check if it is a win or a loss
# dice = random.randint(1,6)
# print(dice)
# if dice > 3:
#   print("win!")
# if dice <= 3:
#   print("loss :(")

#PART 2 (add to the existing code)
#### a variable to tally the wins and losses
# wins = 0
# loss = 0
# dice = random.randint(1,6)
# print(dice)
# if dice > 3:
#   wins = wins + 1
#   print("win!")
# if dice <= 3:
#   loss = loss + 1
#   print("loss :(")
# print("WINS ", wins)
# print("LOSS ", loss)

#PART3 (modify the existing code)
### add in repetition
wins = 0
loss = 0

for i in range(6):
  dice = random.randint(1,6)
  print(dice)
  if dice > 3:
    wins = wins + 1
    print("win!")
  if dice <= 3:
    loss = loss + 1
    print("loss :(")

print("WINS ", wins)
print("LOSS ", loss)

#BONUS CHALLENGE!
#check if there are more wins than losses