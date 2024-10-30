#Questions: What number is the largest?

# 4, 6, 2, 3

#How do you know? 

#Step 1 Build list
n = [3,2,3,5]

###################################################

#Step 2 Read through each value. 

  #1 print each value
  # print(n[0])
  # print(n[1])
  # print(n[2])
  # print(n[3])
  
  #2 build a loop to find the index values
  # for i in range(0,4,1):
  #   print(i)
  
  
  #3 index with newly found numbers
  # for i in range(0,4,1):
  #   print(n[i])

###################################################

#Step 3 First value will be stored as largest value. All subsequent larger values will replace the previous.

#using list in line 3
# biggest = n[0]
# for i in range(1,4):
#   if n[i] > biggest:
#     biggest = n[i]
# print(biggest)

###################################################
#Step 4 What if i dont want to keep counting how many values are in my list? Use len() function to retrieve info

# print(len(n))

#apply into loop to replace the max parameter in the range function
# biggest = n[0]
# for i in range(1,len(n)):
#   if n[i] > biggest:
#     biggest = n[i]
# print(biggest)



###################################################
#Problem 1 build a list of 5 colors and print all of them 1 by 1 using a for loop.




#Problem 2 using the same list, find the index position of white in the list.





#Problem 3 using the same list, print the first, third and fifth colors in the list.