################################################################
# PART 1
################################################################

#1 Generate a random number between 1 and 6 to simulate a dice roll

#2 Roll a second dice 

#3 check if you get doubles

# import random

# dice1 = random.randint(1,6)
# dice2 = random.randint(1,6)

# print("dice 1:",dice1)
# print("dice 2:",dice2)

# if dice1 == dice2:
#   print("doubles")


################################################################
# PART 2
################################################################

#4 generate a third dice

#5 check if you get doubles using OR conditional

#6 check if you get triples using AND conditional


# import random

# dice1 = random.randint(1,6)
# dice2 = random.randint(1,6)
# dice3 = random.randint(1,6)

# print("dice 1:",dice1)
# print("dice 2:",dice2)
# print("dice 3:",dice3)


# if dice1 == dice2 or dice1 == dice3 or dice2 == dice3:
#   print("doubles")

# if dice1 == dice2 and dice2 == dice3:
#   print("triples")


################################################################
# PART 3
################################################################

#7 use a while loop to forever roll dices, stop when hitting triples

#8 count how many times you rolled until you stop at triples

import random

count = 0

while True:
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  dice3 = random.randint(1,6)
  count = count + 1
  print("dice 1:",dice1)
  print("dice 2:",dice2)
  print("dice 3:",dice3)


  if dice1 == dice2 or dice1 == dice3 or dice2 == dice3:
    print("doubles")

  if dice1 == dice2 and dice2 == dice3:
    print("triples")
    break

print("Counter:",count)

#Bonus: at the final triples it says "doubles" then "triples" because technically a triple counts as a double
#ask your student how to fix that