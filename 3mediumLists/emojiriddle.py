#CREDITS OG CREATOR ABBY LEE
#ARTIST: TAYLOR SWIFT

#1: Create a list of all of the songs
#2: Create a list of all of the emoji hints (make sure they share index)
#3: display a random song and allow the user to guess
#4: check answer index that matches the song index
#5: using a for loop, repeat through every song and remove them after answered
#6: build score


import random

songs = ["bejeweled","message in a bottle","paper rings", "miss americana and the heartbreak prince","london boy"]

emojis = ["🐝💎" , "📜➡️🍼" ,"📃💍💍", "👩‍🦰🇺🇸💔🤴", "💂👦"]


score = 0

for i in range(len(songs)):
  
  randomquestion = random.randint(0,len(songs))
  print(emojis[randomquestion])
  
  guess=input("guess the song ")
  
  if guess.lower()==songs[randomquestion].lower():
    print ("good job!")
    score = score + 1
    
  else:
    print("incorrect.")
    
  print()
  
  songs.pop(randomquestion)
  emojis.pop(randomquestion)
  

print("your score was:", score)

