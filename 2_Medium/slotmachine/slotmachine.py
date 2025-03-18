
import random
credits = 100
#have student build out list for more practice
slots = ["🤡","💩","👽","👾","🤖","🎃","😺","🥷"]

#set play conditions 
#1 play until out of money or win a certain amount
#2 play for a # of rounds
#3 play until you want to exit


# print('you have $' + str(credits))

# while True: 
#   bet = int(input("place your bet: ")) 
#   while bet > credits: #enforce bet limit of what you have
#     print("you don't have enough")
#     bet = int(input("place your bet: "))
  
#   slot1 = slots[random.randint(0,7)]
#   slot2 = slots[random.randint(0,7)]
#   slot3 = slots[random.randint(0,7)]
  
#   print(slot1, slot2, slot3)
  
#   #check for 3 in a row
#   if slot1 == slot2 == slot3:
#     credits = credits + (bet*10)
#     print("Jackpot! You win $"+ str(bet*10)) #do string conversion for format
  
  
#   #check for a pair
#   elif slot1 == slot2 or slot2 == slot3 or slot3 == slot1:
#     credits = credits + (bet*3)
#     print("You got a match! You win $"+ str(bet*3))
  
#   #else nothing
#   else:
#     credits = credits - bet
#     print("no matches")

#   print('you have $' + str(credits))


#BONUS: show the slots rolling

# import time
# import replit
# wait = 0.01
# for i in range(20):
#   slot1 = slots[random.randint(0,7)]
#   slot2 = slots[random.randint(0,7)]
#   slot3 = slots[random.randint(0,7)]
#   replit.clear()
#   print(slot1, slot2, slot3)
#   time.sleep(wait)
#   wait = wait + 0.02