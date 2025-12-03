# Nested List Lecture Pt.2

# warmup: generate a nested list of 5 rows and 7 columns filled with random numbers 0 to 9 using loops
import random 

grid = []
for i in range(5):
  row = []
  for j in range(7):
    row.append(random.randint(0,9))
  grid.append(row)
print(grid)

# access the 1st row, 1st item and print it
print(grid[0][0])

# acces the 1st row, 2nd item and print it
print(grid[0][1])

# NOTICE pattern and use for loop
for column in range(7):
  print(grid[0][column])

# What do for each row now?
for row in range(5):
  for column in range(7):
    print(grid[row][column])

# CHALLENGE: count how many even numbers are in the grid