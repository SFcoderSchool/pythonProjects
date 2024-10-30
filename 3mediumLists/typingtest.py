import time

paragraph = "I have five potatoes in my basket."

#2 extra print because the replit clear (trash buttom=n) gets in the way
print()
print()
print(paragraph)

start = time.time()

typing = input()

end = time.time()

print('completed in ' + str(round(end-start,2)) + "seconds")


#Accuracy of letter in proper space
letterError = abs(len(paragraph)-len(typing)) # start at 0 and change to absolute of difference between paragraph and entry

checkParaLen = len(paragraph)
if len(typing)<len(paragraph):
  checkParaLen = len(typing)

for i in range(checkParaLen):#start with len(paragraph) then add after index error
  if paragraph[i] != typing[i]:
    letterError = letterError + 1

print(f"number of errors: {letterError}")


#check for accuracy of words
plist = paragraph.split()
tlist = typing.split()

checkListLen = len(plist)
if len(tlist) < len(plist):
  checkListLen = len(tlist)

wordError=abs(len(plist)-len(tlist)) #start with 0 then switch to absolute different to account for missing
for i in range(checkListLen): # start with len(plist) then add condition for shorter input
  if plist[i]!=tlist[i]:
    wordError = wordError + 1

print(f"number of word errors: {wordError}")