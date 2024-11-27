import random
#16 dictionary entries and which topic it belongs to
connections = {
    "strawberries": "red",
    "fire truck": "red",
    "roses": "red",
    "apple": "red",
    "saphire":"blue",
    "blueberry":"blue",
    "sky":"blue",
    "ocean":"blue",
    "orange":"orange",
    "carrot":"orange",
    "pumpkin":"orange",
    "tiger":"orange",
    "grass":"green",
    "avocado":"green",
    "frog":"green",
    "leaves":"green"
}


#get all the 16 keys into a list, randomize the order
words = list(connections.keys())
random.shuffle(words)

#a function that will print the words in 4 rows of 4 words each
#they are also numbered based on their index
def printWords():
    index = 0
    rows = int(len(words)/4)
    for i in range(rows):
        line = ""
        for j in range(4):
            line += str(index) + ")" + words[index] + " \t"
            index += 1
        print(line)

#a function that will ask the user to select 4 words each
def select4words():
    #each word the user select is placed into a list
    selection = []
    for i in range(4):
        num = int(input("Select a word #: "))
        selection.append(words[num])
    #looks up the word in the dictionary
    #check if they all have the same topic
    if connections[selection[0]] == connections[selection[1]] == connections[selection[2]] == connections[selection[3]]:
        print("The category was: " + connections[selection[0]])
        #if they all have the same topic remove the word from the words list
        for i in range(4):
            words.remove(selection[i])
    

while True:
    printWords()
    select4words()
    #if no more words in the words list you got all the words, end the game
    if len(words) == 0:
        print("Congratz you grouped all words!")
        break