#CREDITS OG CREATOR ABBY LEE
#ARTIST: TAYLOR SWIFT

#1: Create a variable and store the emojis you want your user to see
#2: display the emojis
#3: allow user to guess the song
#4: check if right or wrong
#5: build score

score = 0

song1="1.🐝💎"
print (song1)
answer=input("guess the song ")
if answer=="bejeweled":
  print ("good job!")
  score = score + 1
else:
  print("incorrect.")
print()

song2="2.📜➡️🍼"
print (song2)
answer=input("guess the song ")
if answer=="message in a bottle":
  print ("good job!")
  score = score + 1
else:
  print ("incorrect.")
print()

song3="3.📃💍💍"
print (song3)
answer=input("guess the song ")
if answer=="paper rings":
  print ("good job!")
  score = score + 1
else:
  print ("incorrect.")
print()

song4="4.👩‍🦰🇺🇸💔🤴"
print (song4)
answer=input("guess the song ")
if answer=="miss americana and the heartbreak prince":
  print ("good job!")
  score = score + 1
else:
  print ("incorrect")
print()

song5="5.💂👦"
print (song5)
answer=input("guess the song ")
if answer=="london boy":
  print ("good job!")
  score = score + 1
else:
  print ("incorrect")
print()

print("your score was:", score)

