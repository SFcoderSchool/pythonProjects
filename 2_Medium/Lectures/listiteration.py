#Questions: How would you analyze all the numbers one at a time

#Step 1 Build list
n = [3,2,3,5]

###################################################

#Step 2 Read through each value. 

#1 print each value
print(n[0])
print(n[1])
print(n[2])
print(n[3])

#2 too many prints; notice a pattern
#  build a loop to find the index values; i matches that pattern
for i in range(0,4,1):
  print(i)

#3 index with newly found numbers
for i in range(0,4,1):
  print(n[i])

#4 what if you don't know how many numbers are in the list
for i in range(0,len(n),1):
  print(n[i])

###################################################
#Problem 1 build a list of 5 colors and print all of them 1 by 1 using a for loop (include white as a color).




#Problem 2 using the same list, find the index position of white in the list.



