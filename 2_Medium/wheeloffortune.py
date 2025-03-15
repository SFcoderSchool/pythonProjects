import random, os
phrase = "i am hungry today"
wallet = 0

blanks = []
for i in range(len(phrase)):
  if phrase[i] == " ":
    blanks.append(" ")
  else:
    blanks.append("_")

while "_" in blanks:
  print("wallet: ", wallet)
  print(" ".join(blanks))
  
  wheel = [1000, 500, 300, 200, 50, 750, 0]
  
  spin = random.choice(wheel)
  if spin == 0:
    print("you landed on bankrupt")
    wallet = 0
  else:
    print('you landed on', spin)
  
  guess = input('Guess a letter: ')
  for i in range(len(phrase)):
    if phrase[i] == guess:
      blanks[i] = guess
      wallet = wallet + spin
  os.system("clear")

print("wallet: ", wallet)
print(" ".join(blanks))

