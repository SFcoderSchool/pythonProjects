import random

ground = []
for i in range(10):
    ground.append("  ")

for i in range(4):
    ground[random.randint(0,9)] = "🪙"

for i in range(3):
    ground[random.randint(0,9)] = "💰"

for i in range(2):
    ground[random.randint(0,9)] = "💎"

# print(ground)

grass = []
for i in range(10):
    grass.append("🌱")


money = 0
for i in range(5):
    print(grass)
    index = input("Where would you like to dig?")
    index = int(index)
    if ground[index] == "💎":
        print("You found a gem!")
        grass[index] = "💎"
        money += 50
    elif ground[index] == "💰":
        print("You found a bag of money!")
        grass[index] = "💰"
        money += 25
    elif ground[index] == "🪙":
        print("You found a coin!")
        grass[index] = "🪙"
        money += 10
    else:
        print("You found nothing. :(")
        grass[index] = "  "

print(grass)
print("You found this much treasure", money)
