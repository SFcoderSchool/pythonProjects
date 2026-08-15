# Tortoise vs Hare
# race to the finish line but the hare might fall asleep and lose their turn

# Steps
# - create emoji variables for tortoise, hare, track, and finish
# - create an empty track list and fill it with track emojis using a loop
# - set the last index to the finish emoji

# - create a tortoise position variable and a hare position variable both starting at 0
# - print the starting track using join

# - start a while loop that runs until either the tortoise or hare reaches the last index

# - roll a dice for the tortoise between 1 and 3 and advance its position
# - if tortoise position goes past the end clamp it to the last index

# - create a sleep variable for the hare set to False
# - create a sleep counter variable set to 0

# - if sleep is False roll a dice for the hare between 1 and 6 and advance its position
# - if hare position goes past the end clamp it to the last index
# - after moving generate a random number between 1 and 4
# - if it equals 1 set sleep to True and print that the hare has fallen asleep

# - check if the hare is sleeping using the sleep variable
# - if sleep is True add 1 to the sleep counter
# - if the sleep counter reaches 3 set sleep to False and reset sleep counter to 0
# - print that the hare is still sleeping and skip their movement

# - place the tortoise and hare markers into the track list at their positions
# - print the track using join
# - restore both positions back to the track emoji after printing

# - check if either player has reached the last index
# - if the hare is there print that the hare wins
# - if the tortoise is there print that the tortoise wins
# - if both are there on the same turn print that it is a tie

# Bonus
# - add a guess at the beginning of the race to see who would win
# - add a mud patch at a random position that slows whoever lands on it by sending them back 2
# - add a round counter and print how many rounds the race lasted


import random
import time

tortoise = "🐢"
hare     = "🐇"
track    = "🟩"
finish   = "🏁"
both     = "🔀"

road = []

for i in range(20):
  road.append(track)

road[19] = finish

tortoise_pos = 0
hare_pos = 0

sleeping = False
sleep_counter = 0

print("".join(road))
print()

while tortoise_pos < len(road) - 1 and hare_pos < len(road) - 1:

  tortoise_roll = random.randint(1, 3)
  tortoise_pos = tortoise_pos + tortoise_roll
  if tortoise_pos >= len(road):
    tortoise_pos = len(road) - 1

  if sleeping == True:
    sleep_counter = sleep_counter + 1
    print("Hare is sleeping... zzz (" + str(sleep_counter) + "/3)")
    if sleep_counter >= 3:
      sleeping = False
      sleep_counter = 0
      print("Hare wakes up!")
  else:
    hare_roll = random.randint(1, 6)
    hare_pos = hare_pos + hare_roll
    if hare_pos >= len(road):
      hare_pos = len(road) - 1

    if random.randint(1, 4) == 1:
      sleeping = True
      print("The hare has fallen asleep!")

  if tortoise_pos == hare_pos:
    road[tortoise_pos] = both
  else:
    road[tortoise_pos] = tortoise
    road[hare_pos] = hare

  print("".join(road))

  road[tortoise_pos] = track
  road[hare_pos] = track
  road[19] = finish

  time.sleep(0.5)
  print()

  if tortoise_pos >= len(road) - 1 and hare_pos >= len(road) - 1:
    print("It is a tie!")
    break
  elif tortoise_pos >= len(road) - 1:
    print("The tortoise wins! Slow and steady!")
    break
  elif hare_pos >= len(road) - 1:
    print("The hare wins! Speed prevails!")
    break