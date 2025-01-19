# fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape"]

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")
#     print(fruit + " juice")
#     print(fruit + " jam")

students_scores = [78, 65, 89, 86, 55, 91, 64, 89]

max_student_score = 0
total_student_score = sum(students_scores)

for score in students_scores:
    if score > max_student_score:
        max_student_score = score

print(f"The highest score in the class is: {max_student_score}")

for _ in range(len(students_scores)):
    for index in range(len(students_scores) - 1):
        if students_scores[index] > students_scores[index + 1]:
            temp = students_scores[index]
            students_scores[index] = students_scores[index + 1]
            students_scores[index + 1] = temp

print(students_scores)