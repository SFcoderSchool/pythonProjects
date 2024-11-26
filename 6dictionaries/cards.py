#for loops to generate dictionary of cards


suits = ["♦", "♣", "♥", "♠"]

cards = {}
i = 0
for num in range(1,14):
    for s in range(4):
        cardname = str(num)+suits[s]
        cards[cardname] = i
        i += 1

print(cards)