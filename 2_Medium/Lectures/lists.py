#1 how to build a list
fruits = ["apple", "banana", "cherry"]
cost = [3,6,4]
#can include multiple data types



#2 how to access list using index
#first item in fruits
print(fruits[0])
#second item in cost
print(fruits[1])

# find out the size of the list
print(len(fruits))

#3 how to add new items into existing list
fruits.append("orange")



#4 how to remove items from list
fruits.pop(2)
#removes based on index

fruits.remove("apple")
#removes based on value (first instance only)


#6 how to modified a existing index
fruits[0] = "nevermind"

#7 check if items exist in list. Can also apply with if statements for additional uses.
print("apple" in fruits)



#exercises

#1 generate a list of 6 colors 
#2 allow the user to append 2 new colors
#3 change the first color into "bluegreen"
#4 remove the 2nd colors from your list
#6 print last color
#7 print 3rd color
