#1. import needed librarys
  #random to shuffle tiles
  #clear to remove previous printed tiles in console
  #time to define wait time before shown data clears

#2. find your emojis and store into a string


#3. find another emoji to represent your "Back of tile"


#4 create a list and add two of every emoji into that list

#5 create a list and add 10 "cover" emoji into it

#4 and 5 can be done together in the same loop.

#6 shuffle the tiles and show the back of tiles

#7 user will guess the position and the tile will flip. User will pick a second tile which will also flip. The two tiles positions are store into a separate list and are compare. If the tiles match, their shown positions remain permanent for the remainder of the game. If not match, the tiles revert back to blank state.

#8 Play game until player has all the matches.

# Bonus: 3 tile matching version

# Bonus: track score

# Bonus: 


import random
import os
import time


emoji="🐕🐬🌺🥭🏅"
cover="🎴"
tiles=[]  
b_tiles=[]

# make blank tile list

# make emoji list

# put 2 of each emoji in the emoji list

# then use random shuffle to shuffle the emoji list

score=0
#split 10x loop into 5x+2x to append for both lists.
for i in range(5):
  for j in range(2):
    tiles.append(emoji[i])
    b_tiles.append(cover)


random.shuffle(tiles)

while "".join(b_tiles).find(cover)!=-1:
  score=score+1  
  print(" ".join(b_tiles))
  
  pair=[]
  #list to hold 2 guesses so you can check. Can also separate into two separate coding sections without a loop
  for i in range(2):
    guess=int(input())
    b_tiles[guess]=tiles[guess]
    pair.append(guess)
    os.system("clear")
    print(" ".join(b_tiles))

  #if tiles do not match, change them back to blank state
  if tiles[pair[0]]!=tiles[pair[1]]:
    b_tiles[pair[0]]=cover
    b_tiles[pair[1]]=cover
    
  time.sleep(1)
  os.system("clear")


if score<10:
  print("Wow you have amazing memory!")
elif score<20:
  print("Good Job")
else:
  print('need more rams')