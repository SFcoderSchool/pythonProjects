# Go Fish
# player asks for a card, if the opponent contains the card then give player all the requested card
# game ends when there is no more deck; person with the most sets (four of a kind) wins

# Steps
# - create the empty deck list
# - create the build_deck function, fill the deck with numbers 1 to 13 4 times, the shuffle the list
# - create the draw_card function, take the top card and store it in a variable, remove the top card, and return the stored top card

# - create the player and bot lists
# - make the start_game function, build the deck and pass out 5 cards to the player and bot
# - call the function and print out the lists to check that it is working

# - create the player_move function
# - print out the player's list
# - ask the user what number card they want
# - check to see if the bot has the card, if they do then take all of the cards from the bot
# - if they don't then say go fish and draw a card

# - create the bot_move function
# - random generate a number for the bot to take
# - check to see if the player has the card, if they do then take all of the cards from the player
# - if they don't then say go fish and draw a card

# - call player_move and bot_move to test
# - loop it and stop the loop when there are no more cards

# - need a way to count numbers in for both player and bot lists
# - create function count_num with 2 parameters (list, int)
# - create a count variable and increment the count and remove from the list the number until there are no more
# - return the count

# - create points variable for player and bot
# - use the count_num function to count all number 1 to 13 for both player and bot
# - if the function returns 4 then increment the relative point variable

# - check to see who has the higher points or tie



import random
deck = []
player = []
bot = []

def build_deck():
  for i in range(1,14,1):
    for j in range(4):
      deck.append(i)

  random.shuffle(deck)

def draw_card():
  top_card = deck[0]
  deck.pop(0)
  return top_card

def start_game():
  build_deck()

  for i in range(5):
    card = draw_card()
    player.append(card)

    card = draw_card()
    bot.append(card)

def player_move():
  print(player)
  print("bot has", len(bot), "amount of cards")

  user = input("What card are you looking for? (1-13) ")
  user = int(user)

  if user in bot:
    while user in bot:
      bot.remove(user)
      player.append(user)
  else:
    print("go fish")
    card = draw_card()
    player.append(card)

def bot_move():
  num = random.randint(1,13)

  if num in player:
    while num in player:
      player.remove(num)
      bot.append(num)
  else:
    print("go fish")
    card = draw_card()
    bot.append(card)

def count_num(hand, num):
  count = 0
  while num in hand:
    hand.remove(num)
  return count



start_game()

while True:
  player_move()
  if len(deck) == 0:
    break
  
  bot_move()
  if len(deck) == 0:
    break

player_points = 0
bot_points = 0

for i in range(1, 14):
  p_count = count_num(player, i)
  if p_count == 4:
    player_points = player_points + 1
  
  b_count = count_num(bot, i)
  if b_count == 4:
    bot_points = bot_points + 1
  
if player_points > bot_points:
  print("Player wins")
elif bot_points > player_points:
  print("Bot wins")
else:
  print("tie")