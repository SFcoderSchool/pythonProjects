
from pprint import pprint
#lets start by creating 3 lists called row 1, 2, &3
row1 = [1,2,3]
row2 = [7,8,9]
row3 = [12,13,14]
#now these 3 lists are independent of each other
#to group these 3 lists together we put them into another list
grid = [row1, row2, row3]
#grid is now a list that holds 3 other lists
print(grid)
#to access row1
print(grid[0])
#now that we've extablised grid[0] is equivalent to row1
#lets access the first number of row1
print(row1[0])
print(grid[0][0])
#both are equivalent since grid[0] is row1
#row1[0] is the same as grid[0][0]
#Exercise
#print index 2 of row3 using the grid
#print index 1 or row2 using the grid



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