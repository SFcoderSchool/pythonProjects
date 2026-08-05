# Story Quiz
# slowly scroll a story across the screen then quiz the user on what they read

# Steps
# - import time and random
# - create a single string that holds the entire story
# - add 15 spaces to the end of the story string so the scroll fades out cleanly

# - create a window_size variable set to 15
# - build the starting visible string by looping through the first window_size characters of story

# - loop through the story string once for every character it contains
# - print the current visible string using a carriage return to overwrite the same line
# - find the next incoming character using the loop counter plus window_size wrapped by the story length
# - build a new visible string by looping through visible starting at its second character
# - attach the incoming character onto the end and replace visible with the new string
# - add a small delay each loop

# - wait for the user to press enter to continue to the quiz
# - clear the screen by printing many blank lines

# - create a dictionary where each key is a question string and each value is the answer string

# - create a list of all the keys from the dictionary
# - create an empty list to track which question indexes have already been asked
# - create a score variable starting at 0

# - loop 5 times to ask 5 questions
# - pick a random index into the keys list
# - use a while loop to keep picking a new index if it is already in the asked list
# - add the chosen index to the asked list

# - use the key at that index to print the question
# - ask the user for their answer
# - compare the lowercased user answer to the lowercased value in the dictionary at that key
# - if it matches add 1 to score and print correct
# - if it does not match print incorrect and show the right answer

# - after all 5 questions print the final score out of 5

# Bonus
# - make multiple stories and store them into a dictionary with the questions and answers for that story
# {story1 : {q1 : a1, q2 : a2} , story2 : {q1 : a1, q2 : a2} }


import time
import random
import os

story = ("Once upon a time, a young explorer named Mira set out into the Whispering Forest. "
  "She carried only a lantern, a map drawn by her grandmother, and a small wooden compass. "
  "Deep in the forest, the trees began to glow faintly blue, guiding her further inside. "
  "Mira found a hidden cave behind a waterfall, exactly where the map said it would be. "
  "Inside the cave she discovered an old chest, locked tight with a rusted iron latch. "
  "She used her compass as a makeshift key, and the latch clicked open with a soft hiss. "
  "Inside the chest was not gold, but a single seed that glowed the same blue as the trees. "
  "Mira planted the seed at the edge of the forest, and a new tree began to grow instantly. "
  "The villagers later named the tree the Heartwood, a symbol of courage and curiosity. "
  "Mira returned many times, but she always said the forest still had more secrets to find.")

print(story)

input("\nPress Enter to start the quiz...")
os.system("clear")

qa = {
  "What was the name of the young explorer?"        : "mira",
  "What forest did Mira explore?"                   : "whispering forest",
  "What three items did Mira carry?"                : "lantern, map, compass",
  "What color did the trees glow?"                  : "blue",
  "What was hidden behind the waterfall?"           : "a cave",
  "What was used to lock the chest shut?"           : "an iron latch",
  "What did Mira use to open the chest?"            : "her compass",
  "What was inside the chest?"                      : "a seed",
  "Where did Mira plant the seed?"                  : "the edge of the forest",
  "What did the villagers name the tree?"           : "heartwood"
}

keys = list(qa.keys())
random.shuffle(keys)

score = 0

questions = 5
print("Answer " + str(questions) + " questions about the story.\n")

for i in range(5):
  question = keys[i]
  print(question)
  user_answer = input("Your answer: ").lower()

  if user_answer == qa[question]:
    score = score + 1
    print("Correct!\n")
  else:
    print("Incorrect. The answer was " + qa[question] + "\n")

print("You scored " + str(score) + " out of " + str(questions) + "!")