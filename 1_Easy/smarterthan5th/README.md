# Are you smarter than a 5th grader<br>⭐★★★★★★★★★

## Background

A series of questions to check if you are smarter than a 5th grader

## Steps

**IMPORTANT!** - Show the students how to do the first two questions which utilizes the **in** keyword and **.lower()** function

1. Ask the user a question and allow them to answer

```python
print("1. If a backyard is 50 feet long and 20 feet wide, how many square feet is the yard?")
answer = input()
```

2. Check to see if the user is corrrect or incorrect

```python
if "1000" == answer:
  print('you are correct')
else:
  print("you are incorrect")
```

3. will run into issue with answers like "1000 sqft"

```python
if "1000" in answer:
  print('you are correct')
else:
  print("you are incorrect")
```

4. Repeat with more questions

```python
print("2. On the periodic table, which element is represented by the letter N?")
answer = input()
if answer == "nitrogen":
  print('you are correct')
else:
  print("you are incorrect")
```

5. will run into issue with answers like "Nitrogen"

```python
answer = answer.lower()
```

6. provide questions and answers, allow students to work on more questions on their own

> Q: How many feet are there in 75 yards? <br>
> A: 225
>
> Q: What gas do humans need in order to live? <br>
> A: oxygen
>
> Q: Who invented the lightbulb? <br>
> A: thomas edison
>
> Q: What are the large rocks that orbit the sun between Mars and Jupiter called? <br>
> A: asteroid or asteroids
>
> Q: Maine borders which U.S. state? <br>
> A: New Hampshire
>
> Q: Whose picture is on the five-dollar bill? <br>
> A: Abraham Lincoln

7. Create a score variable
8. Keep track of how many correct the user got

```python
score = 0

...

if "1000" in answer:
  print('you are correct')
  score = score + 1
else:
  print("you are incorrect")

```

9. output if the user is smarter than a 5th grader or not

```python
if score > 6:
  print("You are smarter than a 5th grader")
else:
  print("You are not smarter than a 5th grader")

score = str(score)
print("Your score is " + score)
```
