# card game
# go fish
# the one with the most pairs wins
# can't ask for a card you don't have
# ask if they have a number
# if they have number, don't draw card and take card from opponent and place the pair down on the table
# same player asks for another number.
# if player doesn't have number, draw from deck,next players turn
# 
import random
deck = []
player = []
bot = []
player_score = 0
bot_score = 0

def startgame():
  global player_score,bot_score
  #deck is a list of numbers with 4 copies each
  for s in range(1,14):
    for v in range(4):
      deck.append(s)
  
  random.shuffle(deck)
  
  #passing out 5 cards to each player
  for t in range(5):
    card1 = deck.pop(0)
    if card1 in player:
      player.remove(card1)
      player_score += 1
      print("You got a pair.")
    else:
      player.append(card1)
    
    card2 = deck.pop(0)
    if card2 in bot:
      bot.remove(card2)
      bot_score +=1
    else:
      bot.append(card2)

#write a function called playerMove
#player asks for a card that they have in hand
#check if the bot has this card
#if they do bot loses this card remove(#)
#you also drop this card remove(#) and get a score
#if they dont have this card you have to go fish (draw a card from the deck)
def playerMove():
  global player_score
  print(player)
  card = input("Please ask the bot for a card you have in your hand:  ")
  if int(card) in bot:
    bot.remove(int(card))
    player.remove(int(card))
    player_score +=1 
    print("You got a pair",card)
    print("Your score is",player_score)
  elif int(card) not in bot:
    print("Go Fish")
    card1 = deck.pop(0)
    if card1 in player:
      player.remove(card1)
      player_score += 1
      print("You got a pair.", card1)
    else:
      player.append(card1)

#write a function called botMove
#bot asks for a random card that they have in hand
#check if the player has this card
#if they do player loses this card remove(#)
#bot also drops this card remove(#) and get a score
#if they dont have this card bot has to go fish (draw a card from the deck)

def botmove():
  global bot_score
  bot_random = bot[random.randint(0,len(bot)-1)]
  print("Do you have a",bot_random)
  if int(bot_random) in player:
    bot.remove(int(bot_random))
    player.remove(int(bot_random))
    bot_score += 1
    print("Bot Score is",bot_score) 
  elif int(bot_random) not in player:
    print("Gofish")
    card2 = deck.pop(0)
    if card2 in bot:
      bot.remove(card2)
      bot_score +=1
    else:
      bot.append(card2)
 
  

startgame()
while True:
  playerMove()
  if len(player) == 0:
    break
  
  botmove()
  if len(bot) == 0:
    break

print("Bot Score:",bot_score)
print("Player Score:",player_score)
if player_score > bot_score:
  print("Player Wins!!")
elif bot_score > player_score:
  print("Bot Wins!!")
else:
  print("You Tied...")