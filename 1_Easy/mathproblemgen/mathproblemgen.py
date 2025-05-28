# Math equation generator
# Difficulty:
# Generate math equations and ask the user to solve the equation

# Steps:
# 1. Create 2 variables and save a number in each variable
# 2. output a string equation using the variables as the numbers

# 3. ask the user to solve the equation
# 4. check to see if the user is correct
# 5. NOTE: make sure to cast the data to match properly

# 6. replace the numbers with random numbers

# 7. repeat with subtraction, multiplication

# Bonus:
# 1. add a loop to repeat 10 times
# 2. set random number to select the type of equation seperately

import random

score = 0
problemnum = 1

for i in range(10):
    number1 = random.randint(1, 30)
    number2 = random.randint(1, 30)

    operator = random.randint(1, 4)
    #addition
    if operator == 1:
        question = str(problemnum) + ". " + str(number1) + "+" + str(number2) + "="
        answer = input(question)
        answer = int(answer)
        if answer == number1 + number2:
           print("correct")
           score = score + 1
        else:
            print("incorrect! Answer was", number1 + number2)

    #subtraction
    elif operator == 2:
        question = str(problemnum) + ". " + str(number1) + "-" + str(number2) + "="
        answer = input(question)
        answer = int(answer)
        if answer == number1 - number2:
            print("correct")
            score = score + 1
        else:
            print("incorrect! Answer was", number1 - number2)

    #multiplication
    elif operator == 3:
        question = str(problemnum) + ". " + str(number1) + "*" + str(number2) + "="
        answer = input(question)
        answer = int(answer)
        if answer == number1 * number2:
            print("correct")
            score = score + 1
        else:
            print("incorrect! Answer was", number1 * number2)

    #division
    elif operator == 4:
        question = str(problemnum) + ". " + str(number1) + "/" + str(number2) + "="
        answer = input(question)
        answer = float(answer)
        if answer == round(number1 / number2, 2):
            print("correct")
            score = score + 1
        else:
            print("incorrect! Answer was", round(number1 / number2, 2))

    #problem number
    problemnum = problemnum + 1

print("Score:", score)
