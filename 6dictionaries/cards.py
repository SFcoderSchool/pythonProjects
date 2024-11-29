import random

#for loops to generate dictionary of cards
suits = ["♦", "♣", "♥", "♠"]

cards = {}
i = 0
for num in range(2,15):
    for s in range(4):
        cardname = str(num)+suits[s]
        if num == 11:
            cardname = "J"+suits[s]
        if num == 12:
            cardname = "Q"+suits[s]
        if num == 13:
            cardname = "K"+suits[s]
        if num == 14:
            cardname = "A"+suits[s]
        cards[cardname] = i
        i += 1

#the index number determines the strength of the card
# print(cards)

keys = list(cards.keys())

random.shuffle(keys)

playercards = []
computercards = []
for i in range(5):
    playercards.append(keys.pop(0))
    computercards.append(keys.pop(0))


def pickPlayerCard():
    print(playercards)
    num = input("Which card index do you play?")
    num = int(num)
    return(playercards.pop(num))

def pickComputerCard():
    num = random.randint(0, len(computercards) - 1)
    return(computercards.pop(num))

playerscore = 0
computerscore = 0
for i in range(5):
    pCard = pickPlayerCard()
    cCard = pickComputerCard()
    print(cCard)
    #looks up the strenght of the card in the dictionary
    if cards[pCard] > cards[cCard]:
        playerscore += 1
        print("Player beats computer.")
    elif cards[cCard] > cards[pCard]:
        computerscore += 1
        print("Computer beats player.")
    else:
        print("Tie")

if playerscore > computerscore:
    print("Player wins!")
elif computerscore > playerscore:
    print("Computer wins!")
else:
    print("Tie")