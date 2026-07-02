# Monopoly Hard
# roll dice to move around the board, buy properties stored as dictionaries, and collect rent

# Steps
# - create a list of board space names
# - create a dictionary for each buyable property with keys: "price", "rent", "color", "owner"
# - store all property dictionaries inside one master dictionary using the space name as the key
# - non-buyable spaces like Go, Jail, and Chance do not get an entry in the properties dictionary

# - create a player dictionary for each player with keys: "pos", "money", "jail"
# - store both player dictionaries in a players dictionary with keys "Player 1" and "Player 2"

# - create a chance cards list where each entry is a dictionary with keys: "text" and "effect"
# - effect values will be strings like "money+100" or "goto_jail" that get checked later

# - write a roll_dice function that generates two random numbers and returns their sum
# - also print what each die landed on inside the function

# - write a move_player function that takes a player dictionary and a roll
# - add the roll to the player pos key
# - if pos goes past the board length, subtract the board length, add 200, and print passing Go
# - return the space name the player landed on

# - write a draw_chance function that takes a player dictionary and the chance cards list
# - pick a random card, print the text, and apply the effect to the player money or pos
# - if the effect is goto_jail set pos to 10 and jail to True

# - write a land_on_property function that takes the current player, other player, and space name
# - look up the property in the properties dictionary using space as the key
# - if owner is None offer to buy it, subtract price and set owner if the player says yes
# - if owner is the other player subtract rent from current and add it to the other
# - if owner is the current player print that they already own it

# - write a print_scoreboard function that takes the players dictionary and properties dictionary
# - loop through player names and count how many properties each owns
# - print each player's money and property count

# - write a check_bankruptcy function that takes the players dictionary
# - check if either player money is 0 or below and print who won, return True if the game is over

# - set up the main while loop using a turn counter and a player names list
# - call roll_dice to get the roll, call move_player to update position and get the space
# - use if elif to check the space and call the matching function
# - call print_scoreboard and check_bankruptcy after each turn

# Bonus
# - add a "houses" key to each property dictionary
# - after landing on their own property ask if they want to build a house for extra rent
# - add a build_house function that checks funds, increments the houses key, and raises rent


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

properties = {
  "Mediterranean Ave":     {"price": 60,  "rent": 2,  "color": "brown",   "owner": None},
  "Baltic Ave":            {"price": 60,  "rent": 4,  "color": "brown",   "owner": None},
  "Reading Railroad":      {"price": 200, "rent": 25, "color": "railroad", "owner": None},
  "Oriental Ave":          {"price": 100, "rent": 6,  "color": "cyan",    "owner": None},
  "Vermont Ave":           {"price": 100, "rent": 6,  "color": "cyan",    "owner": None},
  "Connecticut Ave":       {"price": 120, "rent": 8,  "color": "cyan",    "owner": None},
  "St. Charles Place":     {"price": 140, "rent": 10, "color": "pink",    "owner": None},
  "Electric Company":      {"price": 150, "rent": 15, "color": "utility", "owner": None},
  "States Ave":            {"price": 140, "rent": 10, "color": "pink",    "owner": None},
  "Virginia Ave":          {"price": 160, "rent": 12, "color": "pink",    "owner": None},
  "Pennsylvania Railroad": {"price": 200, "rent": 25, "color": "railroad","owner": None},
  "St. James Place":       {"price": 180, "rent": 14, "color": "orange",  "owner": None},
  "Tennessee Ave":         {"price": 180, "rent": 14, "color": "orange",  "owner": None},
  "New York Ave":          {"price": 200, "rent": 16, "color": "orange",  "owner": None},
  "Kentucky Ave":          {"price": 220, "rent": 18, "color": "red",     "owner": None},
  "Indiana Ave":           {"price": 220, "rent": 18, "color": "red",     "owner": None},
  "Illinois Ave":          {"price": 240, "rent": 20, "color": "red",     "owner": None},
  "B&O Railroad":          {"price": 200, "rent": 25, "color": "railroad","owner": None},
  "Atlantic Ave":          {"price": 260, "rent": 22, "color": "yellow",  "owner": None},
  "Ventnor Ave":           {"price": 260, "rent": 22, "color": "yellow",  "owner": None},
  "Water Works":           {"price": 150, "rent": 15, "color": "utility", "owner": None},
  "Marvin Gardens":        {"price": 280, "rent": 24, "color": "yellow",  "owner": None},
  "Pacific Ave":           {"price": 300, "rent": 26, "color": "green",   "owner": None},
  "North Carolina Ave":    {"price": 300, "rent": 26, "color": "green",   "owner": None},
  "Pennsylvania Ave":      {"price": 320, "rent": 28, "color": "green",   "owner": None},
  "Short Line Railroad":   {"price": 200, "rent": 25, "color": "railroad","owner": None},
  "Park Place":            {"price": 350, "rent": 35, "color": "blue",    "owner": None},
  "Boardwalk":             {"price": 400, "rent": 50, "color": "blue",    "owner": None},
}

players = {
  "Player 1": {"pos": 0, "money": 1500, "jail": False},
  "Player 2": {"pos": 0, "money": 1500, "jail": False},
}

chance_cards = [
  {"text": "Bank error in your favor. Collect $100.",    "effect": "money+100"},
  {"text": "Pay school fees of $150.",                   "effect": "money-150"},
  {"text": "Speeding fine. Pay $50.",                    "effect": "money-50"},
  {"text": "Your building loan matures. Collect $150.",  "effect": "money+150"},
  {"text": "Go directly to Jail.",                       "effect": "goto_jail"},
  {"text": "Dividend pays out. Collect $50.",            "effect": "money+50"},
]


def roll_dice():
  die1 = random.randint(1, 6)
  die2 = random.randint(1, 6)
  print("You rolled a " + str(die1) + " and a " + str(die2) + " = " + str(die1 + die2))
  return die1 + die2


def move_player(p, roll):
  p["pos"] = p["pos"] + roll
  if p["pos"] >= len(board):
    p["pos"] = p["pos"] - len(board)
    p["money"] = p["money"] + 200
    print("You passed Go! Collect $200.")
  space = board[p["pos"]]
  print("You landed on " + space)
  return space


def draw_chance(p, cards):
  card = cards[random.randint(0, len(cards) - 1)]
  print("Chance card: " + card["text"])
  if card["effect"] == "money+100":
    p["money"] = p["money"] + 100
  elif card["effect"] == "money+150":
    p["money"] = p["money"] + 150
  elif card["effect"] == "money+50":
    p["money"] = p["money"] + 50
  elif card["effect"] == "money-150":
    p["money"] = p["money"] - 150
  elif card["effect"] == "money-50":
    p["money"] = p["money"] - 50
  elif card["effect"] == "goto_jail":
    p["pos"] = 10
    p["jail"] = True
    print("Moving to Jail.")


def land_on_property(p, o, current, other, space):
  prop = properties[space]
  if prop["owner"] == None:
    print(space + " is unowned. Price: $" + str(prop["price"]) + ". Buy it? (yes/no)")
    answer = input()
    if answer == "yes":
      if p["money"] >= prop["price"]:
        p["money"] = p["money"] - prop["price"]
        prop["owner"] = current
        print("You bought " + space + "! Money: $" + str(p["money"]))
      else:
        print("Not enough money to buy " + space)
    else:
      print("You chose not to buy " + space)
  elif prop["owner"] == other:
    rent = prop["rent"]
    p["money"] = p["money"] - rent
    o["money"] = o["money"] + rent
    print("Owned by " + other + ". You pay $" + str(rent) + " in rent. Money: $" + str(p["money"]))
  else:
    print("You already own " + space)


def print_scoreboard(players, properties):
  print("\n--- Scoreboard ---")
  for name in players:
    count = 0
    for prop_name in properties:
      if properties[prop_name]["owner"] == name:
        count = count + 1
    print(name + ": $" + str(players[name]["money"]) + " | Properties: " + str(count))


def check_bankruptcy(players):
  if players["Player 1"]["money"] <= 0:
    print("Player 1 is bankrupt. Player 2 wins!")
    return True
  if players["Player 2"]["money"] <= 0:
    print("Player 2 is bankrupt. Player 1 wins!")
    return True
  return False


player_names = ["Player 1", "Player 2"]
turn = 0

print("Welcome to Monopoly!")
for name in player_names:
  print(name + " starts at " + board[players[name]["pos"]] + " with $" + str(players[name]["money"]))

while True:
  current = player_names[turn % 2]
  other = player_names[(turn + 1) % 2]
  p = players[current]
  o = players[other]

  print("\n--- " + current + "'s turn ---")
  print("Money: $" + str(p["money"]))
  input("Press Enter to roll...")

  roll = roll_dice()
  space = move_player(p, roll)

  if space == "Go To Jail":
    p["pos"] = 10
    p["jail"] = True
    print("Go to Jail!")
  elif space == "Income Tax":
    p["money"] = p["money"] - 200
    print("Income Tax! Pay $200. Money: $" + str(p["money"]))
  elif space == "Luxury Tax":
    p["money"] = p["money"] - 100
    print("Luxury Tax! Pay $100. Money: $" + str(p["money"]))
  elif space == "Chance":
    draw_chance(p, chance_cards)
  elif space in properties:
    land_on_property(p, o, current, other, space)

  print_scoreboard(players, properties)

  if check_bankruptcy(players):
    break

  turn = turn + 1