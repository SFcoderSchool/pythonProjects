#1 how to build a list
fruits = ["apple", "banana", "cherry"]
cost = [3,6,4]
#can include multiple data types



#2 how to access list using index
#first item in fruits
print(fruits[0])
#second item in cost
print(cost[1])
#going backwards
print(fruits[-1])

# find out the size of the list
print(len(fruits))



#3 how to add new items into existing list
fruits.append("orange")



#4 how to remove items from list
fruits.pop(2)
#removes based on index

cost.remove(3)
#removes based on value (first instance only)


#5 how to insert items into specified positions (position, item)
fruits.insert(1,"french fries")


#6 how to modified a existing index
fruits[1] = "nevermind"

#7 check if items exist in list. Can also apply with if statements for additional uses.
print("apple" in fruits)



#exercises

#1 generate a list of 6 colors 
#2 allow the user to input 2 new colors
#3 change the first color into "bluegreen"
#4 remove the 2nd colors from your list
#5 remove "white" from list if it exist (must write code even if you don't have white)
#6 print 2nd to last color
#7 print 3rd color
#8 insert "brown" into the 3rd spot