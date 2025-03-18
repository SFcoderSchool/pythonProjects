import random

chicken = "🐔"
car = "🚘"
road = "🛣️"
cash = 100

while True:
    street = []
    for i in range(10):
        street.append(road)
    
    print("Your cash:", cash)
    bet = int(input("How much do you want to bet?"))
    cash = cash - bet

    for i in range(10):
        print(street)
        choice = input("do you want to cross the street?")
        if choice == "yes":
            coin = random.randint(1,4)
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

