#good guys and bad guys
#dialogue
#bad guys can say bad things
import random
import time
import os

#dictionary of mafia roles and their dialogues
mafia_dialogues = {
    "Mafia": [
        "Let’s not rush to conclusions it's definitely not me.",
        "I think we should get rid of anyone suspicious.",
        "Maybe we should hear from everyone before deciding.",
        "It’s hard to know who to trust right now.",
        "That guy is suspicious. Let's keep discussing."
    ],
    "Detective": [
        "I have a strong feeling about who the Mafia is.",
        "I need more clues, but I think we're getting close.",
        "I’ve been observing, and some people seem suspicious.",
        "I trust some people here, but I’m not sure about others.",
        "We need to work together to catch the Mafia."
    ],
    "Doctor": [
        "I’ll do my best to protect someone tonight.",
        "I have to guess who the Mafia might target next.",
        "Let’s focus on finding the Mafia, and I’ll keep us safe.",
        "We need to be cautious—everyone’s life depends on it.",
        "I'll be keeping an eye out tonight."
    ],
    "Townsperson": [
        "I don’t have special information, but I want to help.",
        "I feel like someone here is acting strange.",
        "Let’s discuss and work out who’s lying.",
        "We need to think carefully before we vote.",
        "I trust some people, but not everyone."
    ]
}



names = ["Ace", "Blaze", "Shadow", "Viper", "Raven", "Whisper", "Echo", "Spike", "Frost", "Nova", "Jinx", "Maverick", "Phoenix", "Storm", "Hunter", "Fox", "Rogue", "Bullet", "Rebel", "Steel", "Dash", "Sparrow", "Ghost", "Blade", "Venom"]

#creating a dictionary of player names and their roles
townsPeople = {}
townsPeopleNames = []

def assignPlayerRoles():
    global townsPeople, townsPeopleNames
    for i in range(8):
        name = names[random.randint(0,len(names)-1)]
        townsPeople[name] = "Townsperson"
    print(townsPeople) 
    #getting the list of player names in this town
    townsPeopleNames = list(townsPeople.keys())
    #a random player(Townsperson) becomes the doctor
    doctor = townsPeopleNames[random.randint(0,len(townsPeopleNames)-1)]
    townsPeople[doctor] = "Doctor"
    #a random player becomes the dective
    detective = townsPeopleNames[random.randint(0,len(townsPeopleNames)-1)]
    #as long as the player is not a "Townsperson" (they have a different role) pick a new person to be the detective
    while townsPeople[detective] != "Townsperson":
        detective = townsPeopleNames[random.randint(0,len(townsPeopleNames)-1)]
    townsPeople[detective] = "Detective"
    #2 random players become the mafia
    for i in range(2):
        mafia = townsPeopleNames[random.randint(0,len(townsPeopleNames)-1)]
        #as long as the player is not a "Townsperson" (they have a different role) pick a new person to be the mafia
        while townsPeople[mafia] != "Townsperson":
            mafia = townsPeopleNames[random.randint(0,len(townsPeopleNames)-1)]
        townsPeople[mafia] = "Mafia"

def townSpeak():
    for i in range(len(townsPeople)):
        #have every player say a dialogue dependent on their roles
        n = townsPeopleNames[i]
        role = townsPeople[n]
        dialogues = mafia_dialogues[role]
        print(n + ": " + dialogues[random.randint(0,len(dialogues)-1)])

def playerGuess():
    print(townsPeopleNames)
    guess = input("Who do you think the mafia is? ")
    if guess in townsPeopleNames:
        townsPeopleNames.remove(guess)
        selected = townsPeople.pop(guess)
        print(guess+" was the "+selected)

def checkWinner():
    mafiaCount = 0
    #count how many mafia members are left
    for i in range(len(townsPeople)):
        if townsPeople[townsPeopleNames[i]] == "Mafia":
            mafiaCount+=1
    #if no mafia members are left towns people win
    if mafiaCount == 0:
        return "TownsPeople"
    #if ONLY mafia members are left mafia wins
    elif len(townsPeople) == mafiaCount:
        return "Mafia"
    #otherwise no one wins
    else:
        return "No One"

def nightTime():
    global townsPeople, townsPeopleNames
    print("Everyone goes to sleep.")
    time.sleep(1)
    protected = ""
    killed = ""
    #check if the Doctor role is still in the dictionary pick a random person to protect
    if "Doctor" in list(townsPeople.values()):
        protected = townsPeopleNames[random.randint(0,len(townsPeopleNames)-1)]
    #if there are still Mafia memebers pick a random person to kill off
    if "Mafia" in list(townsPeople.values()):
        killed = townsPeopleNames[random.randint(0,len(townsPeopleNames)-1)]
    #if doctor did not protect this person kill them off
    if protected != killed:
        print("Mafia killed " +killed)
        townsPeopleNames.remove(killed)
        selected = townsPeople.pop(killed)
        print(killed+" was the "+selected)
    else:
        print("The doctor protected " + protected)
    if "Detective" in townsPeople:
        investigate = townsPeopleNames[random.randint(0,len(townsPeopleNames)-1)]
        if townsPeople[investigate] == "Mafia":
            print(investigate + " is a Mafia member.")
        else:
            print(investigate + " is not a Mafia member.")



assignPlayerRoles()


night = 1
while True:
    print("Its day time.")
    time.sleep(1)
    townSpeak()
    input("press Enter to move on")
    os.system("clear || cls")
    nightTime()
    print("Night",night)
    playerGuess()
    final = checkWinner()
    if final == "Mafia":
        print("Mafia Wins!")
        break
    if final == "TownsPeople":
        print("Towns People win")
        break
    night += 1
