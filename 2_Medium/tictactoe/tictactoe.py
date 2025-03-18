#this is a 2 player game meant to be player with someone else near you


row0 = ["_","_","_"]
row1 = ["_","_","_"]
row2 = ["_","_","_"]



while True:
  print(row0)
  print(row1)
  print(row2)
  
  r = int(input("Which row do you pick? "))
  c = int(input("Which column do you pick?"))
  
  if r==0:
    row0[c] = "X"
  if r==1:
    row1[c] = "X"
  if r==2:
    row2[c] = "X"

  #finally check if a player has won the game
  #Copy and paste this here last
  # if row0[0]==row0[1]==row0[2] and row0[0]!="_":
  #   print("Player X has won the game!")
  #   break
  # if row1[0]==row1[1]==row1[2] and row1[0]!="_":
  #   print("Player X has won the game!")
  #   break
  # if row2[0]==row2[1]==row2[2] and row2[0]!="_":
  #   print("Player X has won the game!")     
  #   break
  # if row0[0]==row1[0]==row2[0] and row0[0]!="_":
  #   print("Player X has won the game!")     
  #   break
  # if row0[1]==row1[1]==row2[1] and row0[1]!="_":
  #   print("Player X has won the game!")     
  #   break
  # if row0[2]==row1[2]==row2[2] and row0[2]!="_":
  #   print("Player X has won the game!")     
  #   break
  # if row0[0]==row1[1]==row2[2] and row0[0]!="_":
  #   print("Player X has won the game!")     
  #   break
  # if row0[2]==row1[1]==row2[0] and row0[2]!="_":
  #   print("Player X has won the game!")     
  #   break
  
  print(row0)
  print(row1)
  print(row2)
  
  r = int(input("Which row do you pick? "))
  c = int(input("Which column do you pick?"))
  
  if r==0:
    row0[c] = "O"
  if r==1:
    row1[c] = "O"
  if r==2:
    row2[c] = "O"

  #finally check if a player has won the game
  if row0[0]==row0[1]==row0[2] and row0[0]!="_":
    print("Player O has won the game!")
    break
  if row1[0]==row1[1]==row1[2] and row1[0]!="_":
    print("Player O has won the game!")
    break
  if row2[0]==row2[1]==row2[2] and row2[0]!="_":
    print("Player O has won the game!")     
    break
  if row0[0]==row1[0]==row2[0] and row0[0]!="_":
    print("Player O has won the game!")     
    break
  if row0[1]==row1[1]==row2[1] and row0[1]!="_":
    print("Player O has won the game!")     
    break
  if row0[2]==row1[2]==row2[2] and row0[2]!="_":
    print("Player O has won the game!")     
    break
  if row0[0]==row1[1]==row2[2] and row0[0]!="_":
    print("Player O has won the game!")     
    break
  if row0[2]==row1[1]==row2[0] and row0[2]!="_":
    print("Player O has won the game!")     
    break

    