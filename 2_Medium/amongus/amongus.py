import time
import random
nonsus = ["hello","hi","how's your day going?","have you done your task yet?","Do you think there are enough resources?","Everyday, I feel like someone is watching me.","Today, I was looking at the cameras, everything was good! Until...I ran out of coffee","Lately, out plants have been growing wildy!","Is there still pizza in the fridge?","How's the lab?"]
sus = ["Today...I saw an imposter down in the vents...","Um?! Me?! I..uh..was..just um...sharpenig my knife! heh...","I,uh was in the kitchen, no, not sus no. do not vote me","Ya want a knife for 40 dollars?","do you think..I..should rig the asteroid laser controls?","don't mind me! just pass...ing by to elertical..!","IT's HIM! He..hE..HE..iS IT!!","wow..you think i'm it...","Hey! HANDS UP! I..am the sheriff!...oh no..where's my knife..","Here's a shady deal-I'll tell you who's it. Just come here with me in the vents..","sus? me? hahahaha!!! umm..no..not..me..dont vote me..."]
#loading players...
players = []
#THE NONSUS 
for i in range(4):
  rand = nonsus[random.randint(0,9)]
  players.append(rand)

#THE SUS 
for i in range(2):
  rand = sus[random.randint(0,9)]
  players.append(rand)

random.shuffle(players)
crewMates = 4
thesusamongus = 2

while True:
  print(players)
  
  sus = input("wHicH pL@yEr iS Sus?")
  
  sentence = players[int(sus)]
  print("The sus among us said:",sentence )
  if sentence in sus:
    print("You got him! ")
    print("Imposter was suffocated to death in space due to no air")
    thesusamongus -= 1
    players.pop(int(sus))
    time.sleep(2)
  else:
    print("No! You got the wrong one! ")
    print("a poor Random Innocent who never committed a single crime was suffocated to death in space due to no air")
    players.pop(int(sus))
    crewMates -=1
  if crewMates < 1:
    print("ERROR: You were outsmarted by the imposter(s)")
    break
    time.sleep(2)
  if thesusamongus < 1:
    print("YOU WON: You outsmarted the imposters without using fancy wigs or James Bonds grappling hooks or any cool explosions that could've gotten you in real trouble and real hurt ")
    time.sleep(2)
    break
  if thesusamongus > 1:
    po = random.randint(0,5)
    players.pop(po)
    print("A random person was killed somehow...")