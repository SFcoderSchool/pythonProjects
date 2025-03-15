import random

#random name poem project!
#take a name, turn each letter into a word!
#for example JASON
#Jolly
#Adventurous
#Sassy
#Observant
#Nice

#make a list of adjectives for each letter
a = ["amazing", "astounding", "ardent", "articulate", "amiable"]
b = ["brilliant", "bold", "benevolent", "brisk", "breathtaking"]
c = ["charismatic", "charming", "courageous", "creative", "compassionate"]
d = ["diligent", "dynamic", "dedicated", "delightful", "dashing"]
e = ["elegant", "energetic", "enthusiastic", "empathetic", "enchanting"]
f = ["fearless", "friendly", "fabulous", "fantastic", "flawless"]
g = ["graceful", "generous", "genuine", "glorious", "gregarious"]
h = ["harmonious", "hopeful", "humble", "hilarious", "honest"]
i = ["innovative", "inspiring", "intelligent", "impressive", "invigorating"]
j = ["jovial", "judicious", "jubilant", "jaunty", "just"]
k = ["keen", "kindhearted", "knowledgeable", "kaleidoscopic", "kosher"]
l = ["lovely", "luminous", "loyal", "lively", "laudable"]
m = ["magnificent", "motivated", "mellow", "majestic", "meticulous"]
n = ["noble", "nurturing", "nice", "noteworthy", "nostalgic"]
o = ["outstanding", "optimistic", "original", "observant", "open-minded"]
p = ["passionate", "persistent", "polite", "powerful", "pragmatic"]
q = ["quaint", "quick-witted", "quiet", "quintessential", "quixotic"]
r = ["remarkable", "resilient", "radiant", "reliable", "rational"]
s = ["stunning", "sincere", "supportive", "spectacular", "steadfast"]
t = ["thoughtful", "tenacious", "talented", "trustworthy", "tactful"]
u = ["unique", "uplifting", "understanding", "unwavering", "upbeat"]
v = ["vibrant", "valiant", "versatile", "vivacious", "venerable"]
w = ["wise", "witty", "warm", "wonderful", "winsome"]
x = ["xenial", "xenodochial", "xenophilic", "xenogenetic", "xerophytic"]
y = ["youthful", "yummy", "yielding", "yare", "yearning"]
z = ["zealous", "zesty", "zany", "zen", "zippy"]

#take the name as an input
name = input("what is your name? ")

#iterate through each letter in the name
for i in range(len(name)):
  letter = name[i]
  #checking which letter it is then picking a random work from the corresponding list
  if letter == "a":
    print(a[random.randint(0,4)])
  elif letter == "b":
    print(b[random.randint(0,4)])
  elif letter == "c":
    print(c[random.randint(0,4)])
  elif letter == "d":
    print(d[random.randint(0,4)])
  elif letter == "e":
    print(e[random.randint(0,4)])
  elif letter == "f":
    print(f[random.randint(0,4)])
  elif letter == "g":
    print(g[random.randint(0,4)])
  elif letter == "h":
    print(h[random.randint(0,4)])
  elif letter == "i":
    print(i[random.randint(0,4)])
  elif letter == "j":
    print(j[random.randint(0,4)])
  elif letter == "k":
    print(k[random.randint(0,4)])
  elif letter == "l":
    print(l[random.randint(0,4)])
  elif letter == "m":
    print(m[random.randint(0,4)])
  elif letter == "n":
    print(n[random.randint(0,4)])
  elif letter == "o":
    print(o[random.randint(0,4)])
  elif letter == "p":
    print(p[random.randint(0,4)])
  elif letter == "q":
    print(q[random.randint(0,4)])
  elif letter == "r":
    print(r[random.randint(0,4)])
  elif letter == "s":
    print(s[random.randint(0,4)])
  elif letter == "t":
    print(t[random.randint(0,4)])
  elif letter == "u":
    print(u[random.randint(0,4)])
  elif letter == "v":
    print(v[random.randint(0,4)])
  elif letter == "w":
    print(w[random.randint(0,4)])
  elif letter == "x":
    print(x[random.randint(0,4)])
  elif letter == "y":
    print(y[random.randint(0,4)])
  elif letter == "z":
    print(z[random.randint(0,4)])
