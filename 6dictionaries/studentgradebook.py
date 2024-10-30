
students = {
    "Andy": 80,
    "Billy": 50,
    "Cody": 87,
    "Danny": 95,
    "Ellie": 73
}

def addStudent(name, grade):
    students[name] = grade

def changeGrade(name, grade):
    students[name]= grade

def average():
    names = list(students.keys())
    total = 0
    for i in range(len(names)):
        n = names[i]
        grade = students[n]
        total += grade
    return total/len(names)

def starStudent():
    names = list(students.keys())
    highest = names[0]
    for i in range(len(names)):
        n = names[i]
        if students[highest] < students[n]:
            highest = n
    return (highest, students[highest])

addStudent("Jimmy",53)
changeGrade("Danny", 100)

print(students)
print(average())
print(starStudent())