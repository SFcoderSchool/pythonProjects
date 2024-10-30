import os
import time
import random


# 5. Implement a scoring system
score = 0

# 1. create the actions and make a parallel list that will be what the user needs to enter
actions = ["Spin it!", "Flick it!", "Pull it!", "Twist it!", "Shout it!", "Shake it!"]
# this is what the user needs to type (action strings)
actioninput = ["spin", "flick", "pull", "twist", "shout", "shake"]

while True:
    os.system("clear")
    
    # 2. randomly choose an action using randint (not random.choice).
    actionNum = random.randint(0,5)
    current_action = actions[actionNum]

    # 3. Show the action for a small amount of time, then hide it
    print(current_action)
    print("wait...")
    time.sleep(max(0.1, 2 - (score/10)))
    os.system("clear")

    # 4. ask the user to enter the action they saw 
    # Bonus: record the amount of time it takes to enter the input and end game if too slow
    starttime = time.time()
    print("Go!", end="\n > ")
    user = input()
    endtime = time.time()
    elapsed = endtime - starttime
    # if elapsed > max(0.5, 2-(score/10)):
        # print("Too slow!")
        # break

    # 4. Check if the input matches the action string
    if user.lower() == actioninput[actionNum]:
        score += 1
    else:
        print("You lose!")
        break


print("Score:", score)