import time
import random
#a list of dialogue of non-suspicious things people say in amongus
nonsus = ["hello","hi","how's your day going?","have you done your task yet?","Do you think there are enough resources?","Everyday, I feel like someone is watching me.","Today, I was looking at the cameras, everything was good! Until...I ran out of coffee","Lately, out plants have been growing wildy!","Is there still pizza in the fridge?","How's the lab?"]
#a list of dialogue of suspicious things people say in amongus
sus = ["Today...I saw an imposter down in the vents...","Um?! Me?! I..uh..was..just um...sharpenig my knife! heh...","I,uh was in the kitchen, no, not sus no. do not vote me","Ya want a knife for 40 dollars?","do you think..I..should rig the asteroid laser controls?","don't mind me! just pass...ing by to elertical..!","IT's HIM! He..hE..HE..iS IT!!","wow..you think i'm it...","Hey! HANDS UP! I..am the sheriff!...oh no..where's my knife..","Here's a shady deal-I'll tell you who's it. Just come here with me in the vents..","sus? me? hahahaha!!! umm..no..not..me..dont vote me..."]
#loading players... (a list of dialouge each player says in the game of amongus)
players = []
#THE NONSUS: picking out 4 random non-suspicious dialogues to add to the group chat
for i in range(4):
  rand = nonsus[random.randint(0,9)]
  players.append(rand)

#THE SUS : picking out 2 random suspicious dialogues to add to the group chat
for i in range(2):
  rand = sus[random.randint(0,9)]
  players.append(rand)

#shuffle the group chat
random.shuffle(players)
#record how many cremates and imposters we have at the start
crewMates = 4
thesusamongus = 2

while True:
  #print ou the group chat
  print(players)
  #ask who to kick out from the group chat by typing an index number
  sus = int(input("wHicH pL@yEr iS Sus?"))
  
  sentence = players[sus]
  print("The sus among us said:",sentence )
  #check if the sentence we picked is in the suspicious list
  if sentence in sus:
    #you found the imposter!
    print("You got him! ")
    print("Imposter was suffocated to death in space due to no air")
    thesusamongus -= 1
    players.pop(int(sus))
    time.sleep(2)
  #if the sentence we picked is not in the suspicious list
  else:
    #you ended up kicking out a crewmate
    print("No! You got the wrong one! ")
    print("a poor Random Innocent who never committed a single crime was suffocated to death in space due to no air")
    players.pop(int(sus))
    crewMates -=1

  #if the amount of crewmates you have is less than 1 you lose
  if crewMates < 1:
    print("ERROR: You were outsmarted by the imposter(s)")
    break
    time.sleep(2)
  #if the amount of imposters you have is less than 1 that means you win
  if thesusamongus < 1:
    print("YOU WON: You outsmarted the imposters without using fancy wigs or James Bonds grappling hooks or any cool explosions that could've gotten you in real trouble and real hurt ")
    time.sleep(2)
    break
  #if there is atleast more than 1 imposter on board.....
  #picke a random person to kick out of the group chat
  if thesusamongus > 1:
    po = random.randint(0,len(players)-1)
    players.pop(po)
    print("A random person was killed somehow...")
