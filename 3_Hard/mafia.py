#good guys and bad guys
#dialogue
#bad guys can say bad things
import random

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


#getting the keys
mafia_roles = list(mafia_dialogues.keys())


names = ["Ace", "Blaze", "Shadow", "Viper", "Raven", "Whisper", "Echo", "Spike", "Frost", "Nova", "Jinx", "Maverick", "Phoenix", "Storm", "Hunter", "Fox", "Rogue", "Bullet", "Rebel", "Steel", "Dash", "Sparrow", "Ghost", "Blade", "Venom"]

#creating a dictionary of player names and their roles
players = {}

for i in range(4):
    name = names[random.randint(0,len(names)-1)]
    players[name] = mafia_roles[i]

print(players) 


player_names = list(players.keys())
#the first player is always the mafia
mafia = player_names[0]
random.shuffle(player_names)


for j in range(5):
    print("Night",j)
    for i in range(4):
        #have every player say a dialogue dependent on their roles
        n = player_names[i]
        role = players[n]
        dialogues = mafia_dialogues[role]
        print(n + ": " + dialogues[random.randint(0,len(dialogues)-1)])

#guess who the mafia is 
guess = input("Who is the mafia?")
if guess == mafia:
    print("You found the mafia!")
else:
    print("Mafia got you.")


#multiple choice quiz instead