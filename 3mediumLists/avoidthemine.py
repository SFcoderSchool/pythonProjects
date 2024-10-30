#1 define bomb, safe, blank space. Use emoji or text is ok.
#2 create empty board list to store 10 blank characters.
#3 create variable and store random index to represent bomb's location
#4 display empty board for player to see
#5 let user pick a location
#6 if the input matches the bombs location flip into bomb. If not, flip into safe.
#7 allow player two to have a turn
#8 loop game until someone triggers the bomb
#9 announce winnet and loser

#bonus: try switching inputs fro 0-9 to 1-10
#bonus: try switching turn picking into a function (only if you have covered functions)
#bonus: try using a while loop instead of for loop




import random

bomb = "💣"
safe = "😏"
blank = "⬜"

board = []

for i in range(10):
  board.append(blank)

bomblocation = random.randint(0,9)

print("".join(board))

### FOR LOOP METHOD ###
for turn in range(5):
  p1 = int(input("choose location: "))
  if p1 != bomblocation:
    board[p1] = safe
    print("".join(board))
  else:
    board[p1] = bomb
    print("".join(board))
    print("p2 wins. gameover")
    break
  
  
  p2 = int(input("choose location: "))
  if p2 != bomblocation:
    board[p2] = safe
    print("".join(board))
  else:
    board[p2] = bomb
    print("".join(board))
    print("p1 wins. gameover")
    break


### WHILE LOOP METHOD ###
# p1 = ""
# p2 = ""

# while p1 != bomblocation and p2 != bomblocation:
#   p1 = int(input("choose location: "))
#   board[p1] = safe
#   print("".join(board))
#   p2 = int(input("choose location: "))
#   board[p2] = safe
#   print("".join(board))
    
# if p1 == bomblocation: 
#   print("p2 wins")
# else:
#   print("p1 wins")
