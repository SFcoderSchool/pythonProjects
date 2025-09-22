# 1 use if statements to check data
number = 5

# if equal
if number == 5:
  print("yes")
# run then check not equal

# if not equal
if number != 5:
  print("no")

# Common Operators for numbers
# greater than     > 
# less than        < 
# equal to         == 
# not equal to     !=


# 2 use else statements when it is otherwise instead of checking the opposite
number = 5
if number == 5:
  print("yes")
else:
  print("no")


# 3 what if i have more than 2 options
# check to see if i have a banana. print statements will allow you to see which if statement worked
basket = "banana"
if basket == "apple":
  print(1)
if basket == "pineapple":
  print(2)
if basket == "banana":
  print(3)
if basket == "grape":
  print(4)

# NOTE: the stacking of if statements will do all of the ifs, ask "do we need to keep checking when I have found my goal?"
# utilize else if to stop asking when my result has been found, and use else "when all else fails then do this"

basket = "pineapple"
if basket == "apple":
  print(1)
elif basket == "pineapple":
  print(2)
elif basket == "banana":
  print(3)
elif basket == "grape":
  print(4)



# exercise 1: check to see if any of these variables are holding the color "pink", if it is then say the number with that variable
c1 = "red"
c2 = "purple"
c3 = "pink"
c4 = "silver"

# answer
if c1 == "pink":
  print(1)
elif c2 == "pink":
  print(2)
elif c3 == "pink":
  print(3)
elif c4 == "pink":
  print(4)
