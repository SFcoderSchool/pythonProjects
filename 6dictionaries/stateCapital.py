capitals = {
    "California": "Sacramento",
    "Texas": "Austin",
    "Florida": "Tallahassee",
    "New York": "Albany",
    "Illinois": "Springfield",
    "Pennsylvania": "Harrisburg",
    "Ohio": "Columbus",
    "Georgia": "Atlanta",
    "Michigan": "Lansing",
    "North Carolina": "Raleigh"
}
states = list(capitals.keys())
score = 0
for i in range(len(states)):
    state = states[i]
    answer = input("What is the capital of " + state + "? ")
    if answer == capitals[state]:
        print("Correct!")
        score = score + 1
    else:
        print("Wrong!")

print("Your final test score is:", score)

#pokemon quiz