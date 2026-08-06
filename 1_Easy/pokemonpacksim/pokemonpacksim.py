import random

money=10
while True:
  print("you have " + str(money) + " bucks")
  user=input ("how many card packs do you want to open? ")
  user=int(user)

  if money>=user*10:
    money=money-10*user
    for i in range(user):
      print("opening a card pack #" + str(i))
      for j in range(10):
        sir=random.randint(1,500)
        ir=random.randint(1,20)
        if sir==1:
          print("You pulled a secret illustration rare!")
          money=money+300
        elif ir==1:
          print("you pulled an illustration rare")
          money=money+25
        else:
          print ("you got a common card..")
  else:
    print("you don't have enough money")