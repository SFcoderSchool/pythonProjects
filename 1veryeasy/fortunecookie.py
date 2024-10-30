#1 choose a random number

#2 using conditionals, print a fortune

#bonus: 
# add more fortunes


import random

cookie = random.randint(1,4)

if cookie == 1:
  print('you will win $100')

elif cookie == 2:
  print('you will slip on a banana peel')

elif cookie == 3:
  print("you will meet Ariana Grande")

else:
  print('a bird will poop on you')