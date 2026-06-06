# Monopoly
# roll dice to move around the board, buy properties, and collect rent

# Steps
# - create a list of board spaces
# - create a list of property prices for each space (0 if not buyable)
# - create a list of rent prices for each space (0 if not buyable)

# - create a player position variable and a player money variable
# - create an empty owned properties list

# - print the starting space and starting money

# - ask the player to press enter to roll the dice
# - generate two random numbers between 1 and 6 and add them together
# - add the roll to the player position
# - if the new position is greater than or equal to the length of the board, reset it to 0 and add the leftover steps
# - print the new position and what space the player landed on

# - check if the space has a price greater than 0 (it is buyable)
# - if it is buyable and not already owned, ask the player if they want to buy it
# - if the player says yes, subtract the price from money and add the space to owned list
# - if it is already owned by the player, print that they already own it

# - check if the player landed on "Go" (position 0) and give them 200 dollars
# - check if the player landed on "Go To Jail" and move them to position 10

# - add a second player with their own position and money variables
# - add a second owned properties list for player 2
# - take turns by using a turn counter and checking if it is even or odd

# - add rent: if a player lands on a space owned by the other player, subtract rent from their money
# - add a check after each turn to see if either player has run out of money
# - if a player hits 0 or below, print that they lost and end the game

# Bonus
# - add a chance card list and draw one when landing on a chance space
# - keep track of how many properties each player owns and print a scoreboard


import random

board = [
    "Go", "Mediterranean Ave", "Community Chest", "Baltic Ave", "Income Tax",
    "Reading Railroad", "Oriental Ave", "Chance", "Vermont Ave", "Connecticut Ave",
    "Jail", "St. Charles Place", "Electric Company", "States Ave", "Virginia Ave",
    "Pennsylvania Railroad", "St. James Place", "Community Chest", "Tennessee Ave", "New York Ave",
    "Free Parking", "Kentucky Ave", "Chance", "Indiana Ave", "Illinois Ave",
    "B&O Railroad", "Atlantic Ave", "Ventnor Ave", "Water Works", "Marvin Gardens",
    "Go To Jail", "Pacific Ave", "North Carolina Ave", "Community Chest", "Pennsylvania Ave",
    "Short Line Railroad", "Chance", "Park Place", "Luxury Tax", "Boardwalk"
]

prices = [
    0, 60, 0, 60, 0,
    200, 100, 0, 100, 120,
    0, 140, 150, 140, 160,
    200, 180, 0, 180, 200,
    0, 220, 0, 220, 240,
    200, 260, 260, 150, 280,
    0, 300, 300, 0, 320,
    200, 0, 350, 0, 400
]

rents = [
    0, 2, 0, 4, 0,
    25, 6, 0, 6, 8,
    0, 10, 15, 10, 12,
    25, 14, 0, 14, 16,
    0, 18, 0, 18, 20,
    25, 22, 22, 15, 24,
    0, 26, 26, 0, 28,
    25, 0, 35, 0, 50
]

p1_pos = 0
p1_money = 1500
p1_owned = []

p2_pos = 0
p2_money = 1500
p2_owned = []

turn = 0

print("Welcome to Monopoly!")
print("Player 1 starts at " + board[p1_pos] + " with $" + str(p1_money))
print("Player 2 starts at " + board[p2_pos] + " with $" + str(p2_money))

while p1_money > 0 and p2_money > 0:

    if turn % 2 == 0:
        current_player = "Player 1"
        pos = p1_pos
        money = p1_money
        my_owned = p1_owned
        other_owned = p2_owned
    else:
        current_player = "Player 2"
        pos = p2_pos
        money = p2_money
        my_owned = p2_owned
        other_owned = p1_owned

    print("--- " + current_player + "'s turn ---")
    print("Money: $" + str(money))
    input("Press Enter to roll...")

    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    roll = die1 + die2
    print("You rolled a " + str(die1) + " and a " + str(die2) + " = " + str(roll))

    pos = pos + roll
    if pos >= len(board):
        pos = pos - len(board)
        money = money + 200
        print("You passed Go! Collect $200.")

    space = board[pos]
    print("You landed on " + space)

    if space == "Go":
        money = money + 200
        print("You landed on Go! Collect $200. Money: $" + str(money))

    if space == "Go To Jail":
        pos = 10
        print("Go to Jail! Moving to " + board[10])

    if space == "Income Tax":
        money = money - 200
        print("Income Tax! Pay $200. Money: $" + str(money))

    if space == "Luxury Tax":
        money = money - 100
        print("Luxury Tax! Pay $100. Money: $" + str(money))

    if prices[pos] > 0:
        if space in my_owned:
            print("You already own " + space)
        elif space in other_owned:
            rent = rents[pos]
            money = money - rent
            if turn % 2 == 0:
                p2_money = p2_money + rent
            else:
                p1_money = p1_money + rent
            print("This property is owned by the other player. You pay $" + str(rent) + " in rent.")
            print("Money: $" + str(money))
        else:
            print(space + " costs $" + str(prices[pos]) + ". Do you want to buy it? (yes/no)")
            answer = input()
            if answer == "yes":
                if money >= prices[pos]:
                    money = money - prices[pos]
                    my_owned.append(space)
                    print("You bought " + space + "! Money: $" + str(money))
                else:
                    print("Not enough money to buy " + space)
            else:
                print("You chose not to buy " + space)

    if turn % 2 == 0:
        p1_pos = pos
        p1_money = money
    else:
        p2_pos = pos
        p2_money = money

    print("Player 1: $" + str(p1_money) + " | Properties: " + str(len(p1_owned)))
    print("Player 2: $" + str(p2_money) + " | Properties: " + str(len(p2_owned)))

    if p1_money <= 0:
        print("Player 1 has run out of money. Player 2 wins!")
        break
    if p2_money <= 0:
        print("Player 2 has run out of money. Player 1 wins!")
        break

    turn = turn + 1