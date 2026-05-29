# Choose your own adventure
# Difficulty: ⭐
# A text-based choice story. Try to survive till the end.

# Steps
# 1. output a statement for the background of the story
# 2. output the first choices the user can pick and allow the to pick
# 3. check to see what they inputted and output the message depending out their choice

# 4. choose a choice and output the second choices to the user
# 5. check to see what they inputted and output the message depending out their choice

# 6. mark certain lines as gameover!
# 7. continue adding more levels

# Magic Forest Adventure
print("*******************************")
print("*  MAGIC FOREST ADVENTURE!   *")
print("*******************************")
print()
print("You are in a magical forest. A talking squirrel runs up.")
print('"Two paths ahead," it says. "Choose wisely!"')
print()

# -----------------------------------------------
# CHOICE 1: Which path?
# -----------------------------------------------

path = input("Go 'left' toward the dark cave, or 'right' toward the sunny meadow? ")
path = path.lower()

if path == "left":
    print("You approach the dark cave. A sign reads: DRAGON INSIDE!")

    # CHOICE 2A
    cave_choice = input("Do you 'go in' or 'run away'? ")
    cave_choice = cave_choice.lower()
    if cave_choice == "go in":
        # DEAD END 1
        print("You tiptoe in and trip over a rock. CRASH!")
        print("The dragon wakes up. You are lost in the cave. GAME OVER!")
    elif cave_choice == "run away":
        print("You sprint away and stumble into a hidden clearing.")
        print("A glowing door is built into a big oak tree.")

        # CHOICE 3 (from cave branch)
        door_choice = input("Do you 'open' the door or 'walk past' it? ")
        door_choice = door_choice.lower()

        if door_choice == "open":
            # WIN
            print("Inside is a cozy room and a friendly wizard!")
            print('"Brave adventurer!" he says. He hands you a bag of gold')
            print("and a map home. You win! GREAT ADVENTURE!")

        elif door_choice == "walk past":
            # DEAD END 2
            print("The path gets darker and darker. You are lost. GAME OVER!")
        else:
            print("You stare so long the door disappears. GAME OVER!")
    else:
        print("You wander into the cave by accident. GAME OVER!")
elif path == "right":
    print("You step into a sunny meadow. A glowing butterfly lands on your nose!")
    # CHOICE 2B
    butterfly_choice = input("Do you 'follow' the butterfly or 'ignore' it? ")
    butterfly_choice = butterfly_choice.lower()

    if butterfly_choice == "ignore":
        # DEAD END 3
        print("The meadow is huge and you walk in circles. GAME OVER!")

    elif butterfly_choice == "follow":
        print("The butterfly leads you to a hidden part of the forest.")
        print("A glowing door is built into a big oak tree.")

        # CHOICE 3 (from meadow branch)
        door_choice = input("Do you 'open' the door or 'walk past' it? ")
        door_choice = door_choice.lower()
        if door_choice == "open":
            # WIN
            print("Inside is a cozy room and a friendly wizard!")
            print('"Brave adventurer!" he says. He hands you a bag of gold')
            print("and a map home. You win! GREAT ADVENTURE!")
        elif door_choice == "walk past":
            # DEAD END 4
            print("The path gets darker and darker. You are lost. GAME OVER!")
        else:
            print("You stare so long the door disappears. GAME OVER!")
    else:
        print("You stand there confused and get very lost. GAME OVER!")
else:
    print("You wander off the path. GAME OVER! (Try 'left' or 'right' next time!)")