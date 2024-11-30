
from pprint import pprint
#create a list of fruits put 4 fruits inside
#print the first item or second item
#in the third index add a list in the list

fruits = ["apple","grapes","banana"]
print(fruits[0])

#add a third item to the list next and have it be a list
fruits = ["apple","grapes",["oranges", "pears", ""],"banana"]


groceries = [
    ["apple","grapes","banana"],
    ["beef", "pork"],
    ["chip","soda"]
]

#access pork or beef



#automation of generating a 2dlist
list2d = []

#generating a single row that will contain 10 numbers
row = []
for i in range(10):
    row.append(0)
#after the row is full of numbers append to the list2d
list2d.append(row)

#repeat the creation of the row and the appending of the row
for j in range(9):
    row = []
    for i in range(10):
        row.append(0)
    list2d.append(row)

pprint(list2d)

#Exercise: try making 8 rows and each row has 8 random numbers each
#dont forget to append the 8 rows to a list



