class Card:
    def __init__(self, num, suit):
        self.num = num
        self.suit = suit
        self.name = str(self.num) + self.suit
    def __str__(self):
        return self.name
    

card1 = Card(9,"heart")
print(card1)