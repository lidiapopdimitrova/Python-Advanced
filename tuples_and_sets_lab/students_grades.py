def average(values):
    return sum(values) / len(values)


number_of_students = int(input())
student_strings = [input() for _ in range(number_of_students)]
student_data = {}

for data in student_strings:
    student, grade_string = data.split()
    grade = float(grade_string)

    if student not in student_data:
        student_data[student] = []

    student_data[student].append(grade)

for student, grades in student_data.items():

    grades_formatted = ' '.join(f'{grade:.2f}' for grade in grades)

    # grades_formatted = ' '.join(map(str, f'{grades:.2f}'))
    print(f"{student} -> {grades_formatted} (avg: {average(grades):.2f})")

