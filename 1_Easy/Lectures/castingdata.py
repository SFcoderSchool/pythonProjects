#Review on data types
#INTEGERS VS STRINGS

#integers - whole numbers
num = 7
#strings - text/words/anything in quotations
number = "seven"

#QUESTION!
a = 8
b = "8"
#How do they differ????


#CONCATENATION - adding two strings together to form a larger sentence
phrase1 = "The quick brown fox "
phrase2 = " jumped over the silly dog."
sentence = phrase1 + phrase2
print(sentence)
#Now can I add a number in between the sentences?
#sentence2 = phrase1 + 777 + phrase2
#No I cannot as 777 is an integer. The CONCATENATION will fail.
#To solve this problem we will perform type casting.
#TYPE CASTING - changing the data type of integer -> string
# or changing the data type from string -> integer
sentence2 = phrase1 + str(777) + phrase2
print(sentence2)

#Another example, lets say you are making a game and have a score.
score = 9999
print(score)
#This will simply show 9999. To make it more interesting or informative we will add a label(string) in front of the number.
print("Score: " + str(score))
#Type casting was performed to add the score variable behind the string.

#Exercise 1:
#roll 3 dices
#print out the 3 dices in this format
#Dice1: 2
#Dice2: 4
#Dice3: 1


#Exercise 2:
#generate a sentence
#add a number at the end of the sentence and print it out




