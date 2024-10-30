#1 use if statements to check data
number = 5

#if equal
if number == 5:
  print("yes")

#if not equal
if number != 5:
  print("no")



#2 use if statements efficiently when looking for 1 answer from multiple options

name = "jeff"
if name == 5:
  print('yes')
else:
  print("no")


#3 what if i have more than 2 options

#check to see if i have a banana. print statements will allow you to see which if statement worked

basket = "banana"
if basket == "apple":
  print(1)
elif basket == "pineapple":
  print(2)
elif basket == "grape":
  print(3)
elif basket == "banana":
  print(4)
elif basket == "durian":
  print(5)

#why did we not use else? because if basket is not banana, the else statment will still run as if we found the banana.
#else covers all other options 

basket = "banana"
if basket == "apple":
  print(1)
elif basket == "pineapple":
  print(2)
elif basket == "grape":
  print(3)
elif basket == "blueberry":
  print(4)
else:
  print(5)

#Common operators
#greater than > 
#less than< 
#equal to == 
#not equal to !=


#exercise 1: print the larger of the two numbers using conditionals to check
num1 = 50
num2 = 30


#exercise 2: check to see if any of these variables are holding the color "pink"
c1 = "red"
c2 = "purple"
c3 = "pink"
c4 = "silver"


#exercise 3: create a variable and enter a number. using the chart below, output the result.

# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# 0-59: F


