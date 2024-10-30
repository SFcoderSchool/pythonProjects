import random

chicken = "🐔"
car = "🚘"
road = "🛣️"
cash = 100
street = []
bet = 0

def generateStreet():
    global street
    street = []
    for i in range(10):
        street.append(road)


def askForBet():
    global cash, bet
    while True:
        print("Your cash:", cash)
        bet = int(input("How much do you want to bet?"))
        if bet > cash:
            print("Not enough money")
        else:
            cash = cash - bet
            break

def playGame():
    global cash, bet, street
    for i in range(10):
        print(street)
        choice = input("do you want to cross the street?")
        if choice == "yes":
            coin = random.randint(1,2)
            if coin == 1:
                street[i] = car
                print("You got ran over!")
                print(street)
                break
            else:
                street[i] = chicken
                bet = bet * 2
        else:
            print("You chickened out and ran away with the money:", bet)
            cash = cash + bet
            break



while True:
    generateStreet()
    
    askForBet()

    playGame()

    if cash == 0:
        print("you have no more money, gambling is bad")
        break