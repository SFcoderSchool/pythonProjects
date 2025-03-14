import random, os
Battle = []
Water = "🌊"
Ship = "🚢"
Boom = "💥"
Miss = "❌"
for i in range(10):
  box = []
  for j in range(10):
    box.append(Water)
  Battle.append(box)
  
def display():
  print(" ",0,1,2,3,4,5,6,7,8,9)
  for i in range(len(Battle)):
    print(i,"".join(Battle[i]))  


# creates a function to place ships
def ship_place(Long,Ships):
  Match = True
  while Match:
    Match = False
    ship_location = []
    Orientation = random.choice(["vert","hori"])
    # creates a choice between vertical or horizontal placement
    if Orientation == "hori":
      Row = random.randint(0,len(Battle)-Long)
      Column = random.randint(0,9)
      # Row has limited spaces depending on how long the ship is
      for i in range(Row,Row+Long):
        ship_location.append([Column,i])
    else:
      Row = random.randint(0,9)
      Column = random.randint(0,len(Battle)-Long)
          # Column has limited spaces depending on how long the ship is
      for j in range(Column,Column+Long):
        ship_location.append([j,Row])
    for i in range(len(Ships)):
      for j in range(Long):
        if Ships[i] == ship_location[j]:
          Match = True
          break
  return ship_location


def main():
  display() #displays gameboard
  Ships = [] #creates an empty list to hold ship placements
  Ships = ship_place(3,Ships) + ship_place(2,Ships) + ship_place(1, Ships) + ship_place(4,Ships)
  return Ships


Ships = main()
for i in range(100): #change to guess until win
  guess = input("Enter a position between 0 to 9 (vertical,horizontal)")
  posi = [int(guess[0]),int(guess[-1])]
  if posi in Ships:
    print(True)
    Battle[int(guess[0])][int(guess[-1])] = Boom
  else:
    Battle[int(guess[0])][int(guess[-1])] = Miss
  os.system('clear')
  display()
