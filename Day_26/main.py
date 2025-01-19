# List Comprehension and the NATO Alphabet


import random
import pandas as pd

# list comprehension

numbers = [1, 2, 3]

numbers = [item+1 for item in numbers]
print(numbers)

x = [n * 2 for n in range(1,5) if n%2 == 0]
print(x)

Word = input("Word: ")

letters_list = [letter for letter in Word]

print(letters_list)

# dictionary comprehension

# new_dict = {new_key:new_value for (key, value) in dict.items() if test}

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_score = {name:random.randint(1, 100) for name in names}
passed_students = {student:score for (student, score) in student_score.items() if score > 50}
print(student_score)
print(passed_students)


#pandas iteration

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

for (key, value) in student_dict.items():
    print(value)

student_df = pd.DataFrame(student_dict)

for (index, row) in student_df.iterrows():
    print(row.student)