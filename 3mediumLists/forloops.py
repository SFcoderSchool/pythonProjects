# Use a for loop when you know the number of times you want to repeat
# example: eat 10 hotdogs
# questions: what happens if you die? Who cares.. computers will follow instructions no matter what. there are methods to stop loops


#1 for loop as repeat count
for i in range(10):
  print("hello")


#2 check variable in for loop-variable can be any name
for i in range(10):
  print(i)


#3 parameters or range (start, stop, change) 
#stop parameter is always short one
for i in range(0,10,1):
  print(i)


#4 adjust parameters
for i in range(1,11,1):
  print(i)



#exercises:
#print numbers 1 through 100 inclusive
#print numbers 100 through 1 inclusive
#print numbers 1-50 by 2's inslusive
#print numbers 10-1 by 1 inclusive (backwards)
#print numbers 1-100. using a conditional, stop for loop at 50
