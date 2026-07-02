# Pig Latin Converter
# ask the user for a word and convert it to pig latin

# Steps
# - ask the user to enter a word and store it in a variable

# - create an empty string to build the new word
# - loop through each letter in the word starting from the second letter
# - add each letter to the new string one at a time

# - create a variable for the vowels to check against
# - check if the first letter of the word is a vowel
# - if it is a vowel, add "way" to the end of the original word instead

# - if it is not a vowel, take the built new string and add the first letter to the end
# - then add "ay" to the end

# - print the final pig latin word

# - wrap the program in a while loop so the user can keep converting words
# - ask the user if they want to convert another word
# - stop the loop if they type "no"

# Bonus
# - handle words that start with multiple consonants by moving them all instead of just one
# - keep the first letter capitalized if the original word was capitalized


vowels = "aeiou"

while True:
  word = input("Enter a word: ")
  word = word.lower()

  first_letter = word[0]

  rest_of_word = ""
  for i in range(1, len(word)):
    rest_of_word = rest_of_word + word[i]

  if first_letter in vowels:
    pig_word = word + "way"
  else:
    pig_word = rest_of_word + first_letter + "ay"

  print("Pig Latin: " + pig_word)

  answer = input("Convert another word? (yes/no): ")
  if answer == "no":
    break