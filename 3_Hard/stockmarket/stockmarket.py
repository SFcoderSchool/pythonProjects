import random
import os

companies = ["Apple", "Google", "Amazon", "Microsoft", "Meta", "Netflix"]
stocks = {}
portfolio = {}
for i in range(len(companies)):
    stocks[companies[i]] = random.randint(100, 500)
    portfolio[companies[i]] = 0

money = 10000



def displayStocks():
    print("Here are the current stock prices:")
    for i in range(len(companies)):
        print(companies[i], ":", stocks[companies[i]])

def buyStock():
    global money
    choice = input("Which stock would you like to buy? ")
    if choice in companies:
        amount = int(input("How many shares would you like to buy? "))
        total_cost = amount * stocks[choice]
        if money >= total_cost:
            money -= total_cost
            portfolio[choice] += amount
            print(f"You bought {amount} shares of {choice}.")
        else:
            print("You don't have enough money to make this purchase.")
    else:
        print("Invalid stock choice.")

def sellStock():
    global money
    choice = input("Which stock would you like to sell? ")
    if choice in companies:
        total = portfolio[choice] * stocks[choice]
        money += total
        print(f"You sold {portfolio[choice]} shares of {choice}.")
        portfolio[choice]= 0
    else:
        print("Invalid stock choice.")

def changePrices():
    global stocks
    companies = list(stocks.keys())
    for i in range(len(companies)):
        company = companies[i]
        change = random.randint(-20, 20)
        stocks[company] += change
        if stocks[company] < 1:
            stocks[company] = 1

def displayPortfolio():
    print("Your current portfolio:")
    for company, shares in portfolio.items():
        print(f"{company}: {shares} shares")
    print(f"Total money available: ${money}")

print("\nWelcome to the Stock Market Simulator!")
while True:
    os.system('cls || clear')
    displayStocks()
    print()
    displayPortfolio()
    print()
    choice = input("Would you like to buy or sell? ")
    
    if choice == "buy":
        buyStock()
    if choice == "sell":
        sellStock()
    
    changePrices()  # Change stock prices after each action
