#PART 1
#start with defining heads and tails as 1 and 2

# coin = 2
# if coin == 1:
#   print('heads')
# if coin == 2:
#   print("tails")



#PART 2 
# modify the existing code to randomize selection 
# import random
# coin = random.randint(1,2)
# if coin == 1:
#   print('heads')
# if coin == 2:
#   print("tails")


#FINAL PART 
#modify the existing code to Flip coins best out of 5
import random



heads = 0
tails = 0

for i in range(5):
  coin = random.randint(1,2)
  if coin == 1:
    print('heads')
    heads = heads + 1
  if coin == 2:
    print("tails")
    tails = tails + 1
  if heads == 3 or tails == 3:
    break

print("heads",heads)
print("tails",tails)

