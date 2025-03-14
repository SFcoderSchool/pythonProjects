#A function is define set of reusable instructors.You can apply functions anytime and anywhere.
#

def print10Hello():
  for i in range(10):
    print("Hello")


#activating the box of code 3x instead of copy pasting the for loop lowers the mess
print10Hello()
print10Hello()
print10Hello()


#you can also write the function and use it later for organization purposes
def count10():
  for i in range(10):
    print(i)


print10Hello()
count10()
print10Hello()
count10()
print10Hello()

#So far we've only written functions that does ONE thing but imagine a function that can print different words or count different numbers.
#We can write code that performs the same task but give different results through the use of parameters.
def print10Word(word):
  for i in range(10):
    print(word)

def countTo(num):
  for i in range(num):
    print(i)

#Parameters are just variables in the parentheses. They are not equal to anything until we activate the function. Think of parameters as variables to be define only during use.
print10Word("toothbrush")
countTo(3)
#"toothbrush" and 3 will determine what the word and num variables are then the code will run with those values

countTo(11)
countTo(22)
countTo(7)
print10Word("cellphone")
print10Word("laptop")
#once again functions are reuseable so I can activate the box of code again and again and each time I do I can count to a different number or print a different word

#Finally functions can have more than 1 parameter.
def printXword(word, num):
  for i in range(num):
    print(word)

printXword("candy",5)
printXword("chocolate",7)
printXword("youtube", 88)

####################################
#Problem 1 build a function with 1 parameter (integer). print that value squared (num x num). Find the square of 7, 9 and 15.




#problem 2 build a function prints every item in a list. Check the following lists below.

n1 = [1,4,7,2]
n2 = [7,6,5,4,2,8,4]
w1 = ["hello","bye","iphone"]



#problem 3 build a function to shuffle words.