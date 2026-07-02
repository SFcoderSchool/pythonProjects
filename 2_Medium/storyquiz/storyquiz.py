# Story Quiz
# slowly display a story, then ask the user 5 random questions out of 10

# Steps
# - import time for the slow display and random for picking questions
# - create a single string that holds the entire story

# - add extra spaces to the end of the story string
# - this gives the scrolling effect room to fade out at the very end

# - create a window_size variable set to 15
# - build the starting visible string by looping through the first window_size characters of the story

# - loop through the story string one time for every character it contains
# - each loop, print the current visible string using a carriage return so it overwrites the same line

# - figure out which character is the next one to scroll in
# - this is the character sitting window_size spaces ahead of the current loop position
# - wrap back to the start of the story once the position goes past the end

# - build a new visible string by looping through the current visible starting at its second character
# - add each of those characters one at a time to the new string
# - then attach the new incoming character onto the end of the new string
# - replace visible with this new string

# - add a tiny delay each loop so the scroll is readable instead of instant

# - create a list of 10 questions about the story
# - create a matching list of 10 correct answers, lined up by index with the questions

# - create an empty list called asked to track which question indexes have been used
# - create a score variable starting at 0

# - loop 5 times to ask 5 questions
# - inside the loop, pick a random index between 0 and 9
# - use a while loop to keep picking a new random index if it is already in the asked list
# - add the chosen index to the asked list

# - print the question at that index
# - ask the user for their answer
# - compare the user answer to the correct answer at that index, ignoring uppercase and lowercase
# - if it matches, add 1 to the score and print "Correct!"
# - if it does not match, print "Incorrect. The answer was " plus the correct answer

# - after the loop finishes, print the final score out of 5

# Bonus
# - add a list of hints lined up with the questions and let the user ask for one before answering
# - change the delay speed based on how many questions the user gets right


import time
import random

story = "Once upon a time, a young explorer named Mira set out into the Whispering Forest. She carried only a lantern, a map drawn by her grandmother, and a small wooden compass. Deep in the forest, the trees began to glow faintly blue, guiding her further inside. Mira found a hidden cave behind a waterfall, exactly where the map said it would be. Inside the cave she discovered an old chest, locked tight with a rusted iron latch. She used her compass as a makeshift key, and the latch clicked open with a soft hiss. Inside the chest was not gold, but a single seed that glowed the same blue as the trees. Mira planted the seed at the edge of the forest, and a new tree began to grow instantly. The villagers later named the tree the Heartwood, a symbol of courage and curiosity. Mira returned many times, but she always said the forest still had more secrets to find."

window_size = 60

story = story + (" " * window_size)

visible = ""
for j in range(window_size):
  visible = visible + story[j]

for i in range(len(story)):
  print("\r" + visible, end="", flush=True)
  time.sleep(0.04)

  new_letter = story[(i + window_size) % len(story)]

  new_visible = ""
  for j in range(1, len(visible)):
    new_visible = new_visible + visible[j]
  new_visible = new_visible + new_letter

  visible = new_visible

print()

questions = [
  "What was the name of the young explorer?",
  "What forest did Mira explore?",
  "What three items did Mira carry?",
  "What color did the trees glow?",
  "What was hidden behind the waterfall?",
  "What did the chest use to lock it shut?",
  "What did Mira use to open the chest?",
  "What was inside the chest?",
  "Where did Mira plant the seed?",
  "What did the villagers name the tree?"
]

answers = [
  "mira",
  "whispering forest",
  "lantern, map, compass",
  "blue",
  "a cave",
  "an iron latch",
  "her compass",
  "a seed",
  "the edge of the forest",
  "heartwood"
]

asked = []
score = 0

print("\nThe story is over! Time for 5 questions.\n")

for i in range(5):
  index = random.randint(0, 9)

  while index in asked:
    index = random.randint(0, 9)

  asked.append(index)

  print(questions[index])
  user_answer = input("Your answer: ")
  user_answer = user_answer.lower()

  if user_answer == answers[index]:
    score = score + 1
    print("Correct!\n")
  else:
    print("Incorrect. The answer was " + answers[index] + "\n")

print("You scored " + str(score) + " out of 5!")