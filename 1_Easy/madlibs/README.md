# Mad Libs <br> ⭐★★★★★★★★★

## Background

Ask the user for words, output a story with those words

## Steps

1. allow the user to input data

```python
input("Enter a plural noun")
```

2. create a variable and save the data

```python
pluralNoun = input("Enter a plural noun: ")
```

3. using the variable, write a sentence or story

```python
print(pluralNoun + " are blue")
```

4. Extend madlibs to have 8+ inputs()

```python
pluralNoun = input("Enter a plural noun: ")
color = input("Enter a color: ")
celebrity = input("Enter a celebrity: ")

print("Roses are", color)
print(pluralNoun + " are blue")
print("I love", celebrity)
```

## Bonus

1. Reuse the variables more than once

```python
print("Roses are", color)
print(pluralNoun + " are " + color)
print("I love", celebrity)
```
