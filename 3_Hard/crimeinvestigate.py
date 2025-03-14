import random

# Crime Investigation Game: Develop a detective game where players must solve a crime using clues stored in dictionaries. 
# Each suspect is a key, and their alibi, motive, and evidence are stored as values. 
# Players piece together the clues to solve the case.

#James was murdered at work, who killed him?
killer = "Thomas"

dialogue1 = {
    "Herman": "James was my best friend!",
    "Amy": "I loved James.",
    "Thomas": "James and I worked together.",
    "Henry": "I saw James once at the grocery store.",
    "Kelly": "I don't know who James is."
}

dialogue2 = {
    "Herman": "I was hanging out with James.",
    "Amy": "I was at home.",
    "Thomas": "I was at work.",
    "Henry": "I was at the grocery store.",
    "Kelly": "I don't know who James is."
}

dialogue3 = {
    "Herman": "James and I parted ways afterwards.",
    "Amy": "I was at home.",
    "Thomas": "I was doing my work.",
    "Henry": "I saw james walk into work.",
    "Kelly": "I don't know who James is."
}

#Thomas is the killer because Henry last saw James last walked into work. Thomas was at work.

print("James was murdered at work, who killed him!?")
people = ["Herman", "Amy", "Thomas", "Henry", "Kelly"]

def question():
    for i in range(len(people)):
        print(i, people[i])
    num = input("Who would you like to question?")
    if num == "stop":
        return False
    num = int(num)
    person = people[num]
    dice = random.randint(1,3)
    if dice == 1:
        print(dialogue1[person])
    if dice == 2:
        print(dialogue2[person])
    if dice == 3:
        print(dialogue3[person])
    return True

while True:
    ans = question()
    if ans == False:
        break

guess = input("Who was the killer? ")
if guess == killer:
    print("You're right!")
else:
    print("You're wrong!")