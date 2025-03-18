import random

name = "Jason"
age = 0
money = 0

print("You were just born, time to grow up and live your life.")

while True:
    dice = random.randint(1,6)
    money = money + dice
    coin = random.randint(1,2)
    if coin == 1:
        money = money * 2
    age = age + 1
    print("Age:", age)
    print("Money:",money)
    if age == 99:
        print(name, "died at the age of 99.")
        print(name, "earned", money, "dollars in their lifetime.")
        break