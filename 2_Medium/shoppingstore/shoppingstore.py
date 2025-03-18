#1) create a list of avaliable items the store has to sell

items = ["apple","orange","banana","grapes","pear"]

#2) create a second list that will act as the shopping basket

basket = []

#3) print out the list of items and ask which item they would like to buy

print(items)
choice = input("What would you like to add to the basket? ")
#3.5) append their choice to the basket
basket.append(choice)
#BONUS: instead of typing in a string, ask for the index number in the input


#4) make a while loop that will repeat the process over and over again to shop for more than one product
while True:
  print(basket)
  choice = input("What would you like to add to the basket? (Type stop to checkout) ")
  #5) stop the loop if they type in the word "stop"
  if choice == "stop":
    break
  else:
    basket.append(choice)


#6) now calculate the checkout price (each item cost $2)
size = len(basket)
total = size*2
print(total, "is your checkout price")