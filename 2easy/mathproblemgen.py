#1 Create 2 variables and store integers in them

#2 Generate an addition math problem with the 2 values

#3 Allow user to answer the math problem

#4 Check answer to see if correct. input > str to int
#if incorrect, print the answer

#5 randomize the 2 numbers

#6 loop for 10 problems

#7 total correct

#Bonus: include subtraction

#Bonus: inlude multiplication
#max out number at 30

#Bonus: include division only if the group is comfortable with float type and round()0

import random

score = 0
problemnum = 1

for i in range(10):
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)

    operator = random.randint(1, 4)
    #addition
    if operator == 1:
        question = str(problemnum) + ". " + str(number1) + "+" + str(number2) + "="
        answer = int(input(question))
        if answer == number1 + number2:
           print("correct")
           score = score + 1
        else:
            print("incorrect! Answer was", number1 + number2)

    #subtraction
    elif operator == 2:
        question = str(problemnum) + ". " + str(number1) + "-" + str(number2) + "="
        answer = int(input(question))
        if answer == number1 - number2:
            print("correct")
            score = score + 1
        else:
            print("incorrect! Answer was", number1 - number2)

    #multiplication
    elif operator == 3:
        #change numbers to make problem easier :)
        number1 = random.randint(1, 30)
        number2 = random.randint(1, 30)
        question = str(problemnum) + ". " + str(number1) + "*" + str(number2) + "="
        answer = int(input(question))
        if answer == number1 * number2:
            print("correct")
            score = score + 1
        else:
            print("incorrect! Answer was", number1 * number2)

    #division
    elif operator == 4:
        number1 = random.randint(1, 30)
        number2 = random.randint(1, 30)
        question = str(problemnum) + ". " + str(number1) + "/" + str(number2) + "="
        #make sure to change to float type and limit to 2 decimal point
        answer = float(input(question))
        if answer == round(number1 / number2, 2):
            print("correct")
            score = score + 1
        else:
            print("incorrect! Answer was", round(number1 / number2, 2))

    #problem number
    problemnum = problemnum + 1

print("Score:", score)
