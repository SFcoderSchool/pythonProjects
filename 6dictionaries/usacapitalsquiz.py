import random
E = {"California":"Sacramento", "Montana":"Helena", "Idaho":"Boise","Georgia":"Atlanta","Washington":"Olympia","Maine":"Agusta","Rhode Island":"Providence","Texas":"Austin","Colorado":"Denver", "Oklahoma":"Oklahoma City","New Jersey":"Trenton","New York":"Albany","Arkansas":"Little Rock","New Mexico":"Santa Fe","Wisconsin":"Madison","Ohio":"Columbus","Missouri":"Jefferson City"}

States = list(E.keys())
random.shuffle(States)

for s in range(0,len(States)):
  state=States[s]
  print("What is the capital of",state+"?")
  ans = input()
  Capital = E[state]
  if ans == Capital:
    CorrectAnswers = ["Correct,Good Job!", "Correct,Nice memory","Correct, You know your capitals!"]
    Bg = random.randint(0,len(CorrectAnswers)-1)
    print(CorrectAnswers[Bg])
  else:
    print("Wrong the actual capital is",Capital)