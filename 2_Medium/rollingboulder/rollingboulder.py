# Boulder Run
# advance through a list of terrain trying to outrun a boulder before it catches you

# Steps
# - create emoji variables for basic terrain, boost, trap, player, boulder, and finish
# - create an empty track list and fill it with basic terrain using a loop

# - set the finish at the last index
# - place boosts at fixed indexes by setting those positions directly

# - loop through the track from index 4 to the second to last space
# - skip any index that is already a boost
# - generate a random number and if it is 1 place a trap at that index

# - create a player position variable starting at 0
# - create a boulder position variable starting at 0
# - give the player a head start by setting player position to 3

# - print the track using join to show the full board

# - start a while loop that runs as long as boulder position is less than player position
# - and as long as player position is less than the last index

# - roll a dice for the player and advance their position
# - if player position goes past the end clamp it to the last index

# - check what emoji is at the new player position
# - if it is a boost move the player forward 2 more and print a message
# - if it is a trap move the player back 3 and print a message

# - update the track to show the player marker at their position
# - print the track

# - roll a dice for the boulder and advance its position
# - if boulder position goes past the end clamp it to the last index
# - update the track to show the boulder marker at its position

# - check if boulder has caught or passed the player and break with a lose message
# - check if player has reached the last index and break with a win message

# Bonus
# - print the gap between player and boulder
# - if the gap is 2 or less print a warning
# - add a stumble trap that skips the player next turn instead of sending them back
# - add a second boulder that starts further back but rolls with a higher dice range


import random

basic  = "🟫"
boost  = "⭐"
trap   = "💀"
player = "🏃"
boulder = "🪨 "
finish = "🏁"

size = 30
track = []

for i in range(size):
  track.append(basic)

track[size - 1] = finish

for i in range(0, size, 5):
  if i != 0:
    track[i]  = boost

for i in range(4, len(track) - 1):
  if track[i] != boost:
    if random.randint(1, 3) == 1:
      track[i] = trap

player_pos = 3
boulder_pos = 0

track[player_pos] = player
track[boulder_pos] = boulder

print("".join(track))
print()

track[player_pos] = basic
track[boulder_pos] = basic

while boulder_pos < player_pos and player_pos < len(track) - 1:
  input("roll the dice (Enter)")

  player_roll = random.randint(1, 6)
  print("You rolled a " + str(player_roll))
  player_pos = player_pos + player_roll

  if player_pos >= len(track):
    player_pos = len(track) - 1

  space = track[player_pos]

  if space == boost:
    print("Boost! Forward 2 extra spaces.")
    player_pos = player_pos + 2
    if player_pos >= len(track):
      player_pos = len(track) - 1
  elif space == trap:
    print("Trap! Back 3 spaces.")
    player_pos = player_pos - 3
    if player_pos < 0:
      player_pos = 0

  boulder_roll = random.randint(1, 6)
  print("Boulder rolled a " + str(boulder_roll))
  boulder_pos = boulder_pos + boulder_roll

  if boulder_pos >= len(track):
    boulder_pos = len(track) - 1

  gap = player_pos - boulder_pos

  track[player_pos]  = player
  track[boulder_pos] = boulder
  print("".join(track))
  track[player_pos]  = space
  track[boulder_pos] = basic

  print("Gap: " + str(gap) + " spaces")

  if gap <= 2 and gap > 0:
    print("The boulder is right behind you!")

  print()

  if boulder_pos >= player_pos:
    print("The boulder caught you! You have been crushed.")
    break

  if player_pos >= len(track) - 1:
    print("You reached the finish! You outran the boulder!")
    break