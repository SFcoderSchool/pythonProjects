import colored #color error
import random
import os

#Do not give the student how to fix the exceeding 5 character string math problem. See if they have solutions
# common solution: randomize until we get a 5 character string

#build functions one at a time and test with gameplay

def add():
	number = random.randint(0, 9)
	number2 = random.randint(0, 9 - number) #limit second value to not exceed sum 9
	answer = number + number2
	equation = f"{number} + {number2} = {answer}"
	if random.randint(1,2)== 1: #reverse math problem for more randomness
		equation = equation[::-1]
	return equation
	
def subtract():
	number = random.randint(0, 9)
	number2 = random.randint(0, number) 
	answer = number - number2
	equation = f"{number} - {number2} = {answer}"
	if random.randint(1,2)== 1:
		equation = f"{answer} = {number} - {number2}"
	return equation

def multiply():
	number = random.randint(0, 9)
	if number > 4:
		n = 1
	elif number > 3:
		n = 2
	elif number > 2:
		n = 3
	elif number > 1:
		n = 4
	else:
		n = 9
	number2 = random.randint(0, n)
	answer = number * number2
	equation = f"{number} * {number2} = {answer}"
	if random.randint(1,2)== 1:
		equation = equation[::1]
	return equation

def division():
	num = random.randint(2, 9)
	den = random.randint(2, num)
	answer = num // den
	while num % den != 0:
		den = random.randint(1, num)
	equation = f"{num} / {den} = {answer}"
	if random.randint(1, 2)== 1:
		equation = f"{answer} = {num} / {den}"
	return equation


choices = [add(), subtract(), multiply(),division()]
	
equation = random.choice(choices)

def checker(userInput):
	for c in range(0, 9, 2):
		if userInput[c] == equation[c]:
			# slots[0] = userInput[0]
			print (colored.Fore.green + userInput[c] , end = " ")
		elif userInput[c] in equation:
			print (colored.Fore.yellow + userInput[c], end = " ")
		else:
			print (colored.Fore.white + userInput[c], end = " ")
	print (colored.Fore.white+"")



tries = []
guess = 6
userInput = ""
while guess > 0 and userInput != equation:
	userInput = input()
	userInput = list(userInput)
	userInput = " ".join(userInput)
	tries.append(userInput)
	# os.system("clear")
	guess = guess - 1
	for i in range (len(tries)):
		checker(tries[i])
	
	

