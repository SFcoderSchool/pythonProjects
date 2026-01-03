# Nested List Lecture

# warmup:
# create a list of fruits put 3 fruits inside
# print the first item
fruits = ["apple","grapes","banana"]
print(fruits[0])

# create another list of meat products and put 2 values inside
# print out the list
meats = ["beef", "pork"]
print(meats)

# Problem: I want to be able to store the fruits and meats into 1 variable, but still keep them contained as fruits and meats
# Solution: throw the lists into another list
# this time lets create a list that would ONLY hold other lists

# add an extra list into groceries for snacks
groceries = [
    fruits,
    meats,
    ["chip","soda"]
]

# access fruits from groceries
print(groceries[0])
# from fruits in groceries, access grapes
print(groceries[0][1])
# access list of snacks
# access pork


# Able to treat the outerlist (groceries) like any other list
# - using len function
print(len(groceries))    # size of different types of groceries
print(len(groceries[0])) # size of fruits

# - changing data
groceries[1][1] = "chicken"
print(groceries)

# - using append, pop, remove
groceries.append(["cheese", "milk", "yogurt"])
print(groceries)

groceries.pop(0)
print(groceries)

groceries.remove(["chip", "soda"])
print(groceries)


# automation of generating a 2dlist 10 x 10
# start empty
list2d = []

# generating a single row that will contain 10 numbers
# row = []
# for i in range(10):
#     row.append(0)
# list2d.append(row)

# this needs to happen 10 times, wrap this code with a for loop
# repeat the creation of the row and the appending of the row
for j in range(10):
    row = []
    for i in range(10):
        row.append(0)
    list2d.append(row)

print(list2d)

# print out each row
for i in range(len(list2d)):
    print(list2d[i])

#Exercise: try making 8 rows and each row has 8 random numbers (1 to 10) each
#dont forget to append the 8 rows to a list



