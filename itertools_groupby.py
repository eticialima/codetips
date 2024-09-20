import itertools
import operator

## Exemple 1 
words = ['apple', 'banana', 'cat', 'dog', 'dragon', 'ant]']

keyfunc = lambda x: x[0]

for key, group in itertools.groupby(sorted(words, key=keyfunc), keyfunc):
    print(key, list(group))
    
     
## Exemple 2 
# Define a list of students with their names and ages
students = [
    {"name": "John", "age": 20},
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 21},
    {"name": "Charlie", "age": 20},
    {"name": "David", "age": 21},
]

# Sort the list of students by age
students.sort(key=operator.itemgetter("age"))

# Use itertools.groupby to group the students by age
for age, group in itertools.groupby(students, key=operator.itemgetter("age")):
    print(f"Age: {age}")
    for student in group:
        print(f"- {student['name']}")