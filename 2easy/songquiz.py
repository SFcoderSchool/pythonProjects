#CREDITS: MADE BY ABBY LEE

#1 create variable to hold multiline string of lyric """   """
#2 display lyric (make sure it doesnt have the title in it)
#3 allow user to guess (use lower function to lower case both answer and guess)
#4 check to see if correct
#5 create score variable
#6 do a total of 10 lyrics
#7 8-10 "super fan", 5-7 "fan", 2-4 "casual fan" , 0-1 "not a fan"


score = 0

lyric1 = """The wine is cold
Like the shoulder that I gave you in the street
Cat and mouse for a month or two or three"""
print (lyric1,"\n")
guess=input("guess the taylor swift song: ")
if guess.lower()==("paper rings"):
  print ("great job! that's correct")
  score = score + 1
else:
  print ("incorrect")
print()

lyric2="""Why'd you have to lead me on?
Why'd you have to twist the knife?
Walk away and leave me bleedin', bleedin'?"""
print (lyric2,"\n")
guess=input("guess the taylor swift song: ")
if guess.lower()==("say don't go"):
  print ("great job! that's correct")
  score = score + 1
else:
   print ("incorrect")
print()

lyric3="""New money, suit and tie
I can read you like a magazine
Ain't it funny? Rumors fly"""
print (lyric3,"\n")
guess=input("guess the taylor swift song: ")
if guess.lower()==("blank space"):
  print ("great job! that's correct")
  score = score + 1
else:
  print ("incorrect")
print()

lyric4="""Walk in the streets with you in your worn-out jeans
I can't help thinking this is how it ought to be
Laughing on a park bench thinking to myself"""
print (lyric4,"\n")
guess=input("guess the taylor swift song: ")
if guess.lower()==("you belong with me"):
  print("great job! that's correct")
  score = score + 1
else:
  print ("incorrect")
print()

lyric5="""But one of these things is not like the others
Like a rainbow with all of the colors
Baby doll, when it comes to a lover"""
print (lyric5,"\n")
guess=input("guess the taylor swift song: ")
if guess.lower()==("me"):
  print ("great job! that's correct")
  score = score + 1
else:
  print ("incorrect")
print()

lyric6="""See the lights, see the party, the ball gowns
See you make your way through the crowd
And say, "Hello"""
print (lyric6,"\n")
guess=input("guess the taylor swift song: ")
if guess.lower()==("love story"):
  print ("great job! that's correct")
  score = score + 1
else:
  print ("incorrect")
print()

lyric7="""Your eyes whispered, "Have we met?"
'Cross the room your silhouette
Starts to make its way to me"""
print (lyric7,"\n")
guess=input("guess the taylor swift song: ")
if guess.lower()==("enchanted"):
  print ("great job! that's correct")
  score = score + 1
else:
  print ("incorrect")
print()

lyric8="""Say you'll remember me
Standing in a nice dress
Staring at the sunset, babe"""
print (lyric8,"\n")
guess=input("guess the taylor swift song: ")
if guess.lower()==("wildest dreams"):
  print ("great job! that's correct")
  score = score + 1
else:
  print ("incorrect")
print() 

lyric9="""And it's new, the shape of your body
It's blue, the feeling I've got
And it's ooh, whoa, oh"""
print (lyric9,"\n")
guess=input("guess the taylor swift song: ")
if guess.lower()==("cruel summer"):
  print ("great job! that's correct")
  score = score + 1
else:
  print ("incorrect")
print()

lyric10="""In the middle of the night, in my dreams
You should see the things we do, baby (mmm)
In the middle of the night, in my dreams"""
print (lyric10,"\n")
guess=input("guess the taylor swift song: ")
if guess.lower()==("ready for it"):
  print ("great job! that's correct")
  score = score + 1
else:
  print ("incorrect")
print()

lyric11="""But I got smarter, I got harder in the nick of time
Honey, I rose up from the dead, I do it all the time
I got a list of names, and yours is in red, underlined"""
print (lyric11,"\n")
guess=input("guess the taylor swift song: ")
if guess.lower()==("look what you made me do"):
  print ("great job! that's correct")
  score = score + 1
else:
  print ("incorrect")
print()

#score check
if score > 7:
  print("super fan")
elif score >4:
  print("fan")
elif score >1 :
  print("casual fan")
else:
  print("not a fan")