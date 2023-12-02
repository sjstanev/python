"""
Input:
7
Peter 5.20
Mark 5.50
Peter 3.20
Mark 2.50
Alex 2.00
Mark 3.46
Alex 3.00

Output:
{student's name} -> {grade1} {grade2} ... {gradeN} (avg: {average_grade})".
Mark -> 5.50 2.50 3.46 (avg: 3.82)
Peter -> 5.20 3.20 (avg: 4.20)
Alex -> 2.00 3.00 (avg: 2.50)
"""


def avg(values):
    return sum(values) / len(values)


number_of_students = int(input())
students_strings = [input() for _ in range(number_of_students)]
students_grades = {}

for student_string in students_strings:
    student, grade_string = student_string.split(' ')
    grade = float(grade_string)
    if student not in students_grades:
        students_grades[student] = []

    students_grades[student].append(grade)

for student_string, grades in students_grades.items():
    grade_formatted = ' '.join(f'{grade:.2f}' for grade in grades)
    average_grade = f'{avg(grades):.2f}'

    print(f'{student_string} -> {grade_formatted} (avg: {average_grade})')
