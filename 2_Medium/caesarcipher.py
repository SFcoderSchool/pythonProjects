alphabet = "abcdefghijklmnopqrstuvwxyz"
phrase = "Warriors are the best"

#loop through the letters in the phrase
for i in range(len(phrase)): 
  #finds position of letter in alphabet
  for letter in range(len(alphabet)): 
    #lower case letters
    if phrase[i].lower() == alphabet[letter]:
      break
  #display the found position -3 (or whatever your cypher wants)
  print(alphabet[letter-3], end="")
  