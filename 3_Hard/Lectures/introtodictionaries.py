# Intro to Dictionaries (A new data type)

# a dictionary is like a list of variables and their values
menu = {
    "chicken": 6,
    "bread": 4,
    "apple": 2
}
# in this example "chicken" is holding the value of 6
# "bread" has the value of 4
# "apple" has the value of 2

# we refer to this as the key and their value
# next we will program how to look up a value in the dictionary

print(menu["chicken"])

# the syntax is simlar to accessing data in a list 
# except we don't use index # but rather we look up what "chicken" is equal to in the dictionary

# Exercise:
# 1) print out the value of bread in the dictionary
# 2) print out the value of apple in the dictionary
# 3) create a dictionary of 5 electronic devices and their costs


# Some useful tools/techniques to remember:
# all the keys in the dictionary listed out for you
allKeys = menu.key() 
print(allKeys)

# outputs an dict_keys object; can't index it like a list therefore convert to list
allKeys = list(allKeys)
print(allKeys)

# iterate through all keys in the list with a for loop
for i in range(len(allKeys)):
    print(allKeys[i])

# print all VALUES in the list by iterating through all keys in the list with a for loop
for i in range(len(allKeys)):
    eachKey = allKeys[i]
    print(menu[eachKey])

