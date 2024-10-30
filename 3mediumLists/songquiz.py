#CREDITS: MADE BY ABBY LEE

#1 create a list to hold the lyrics
#2 create a list to hold the songs
#3 choose random lyric to display
#3 allow user to guess (use lower function to lower case both answer and guess)
#4 check to see if correct from matching index of answers
#5 create score variable
#6 do a total of 5 lyrics
#7 5 "super fan", 4 "fan", 2-3 "casual fan" , 0-1 "not a fan"


import random

lyrics = ["""The wine is cold
Like the shoulder that I gave you in the street
Cat and mouse for a month or two or three""",

"""Why'd you have to lead me on?
Why'd you have to twist the knife?
Walk away and leave me bleedin', bleedin'?""",

"""New money, suit and tie
I can read you like a magazine
Ain't it funny? Rumors fly""",

"""Walk in the streets with you in your worn-out jeans
I can't help thinking this is how it ought to be
Laughing on a park bench thinking to myself""",

"""But one of these things is not like the others
Like a rainbow with all of the colors
Baby doll, when it comes to a lover"""
]

songs = ["paper rings",
         "say don't go",
         "blank space",
         "you belong with me",
         "me"
        ]

score = 0
for i in range(len(lyrics)):
  randomsong = random.randint(0,len(lyrics)-1)

  print (lyrics[randomsong],"\n")
  guess=input("guess the taylor swift song: ")
  if guess.lower()==songs[randomsong].lower():
    print ("great job! that's correct")
    score = score + 1
  else:
    print ("incorrect")
  songs.pop(randomsong)
  lyrics.pop(randomsong)
  print()

#score check
if score > 4:
  print("super fan")
elif score >3:
  print("fan")
elif score >1 :
  print("casual fan")
else:
  print("not a fan")