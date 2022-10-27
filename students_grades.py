n = int(input())

students_info = {}

for _ in range(n):
    student, grade_string = input().split()
    grade = float(grade_string)
    if student not in students_info:
        students_info[student] = []
    students_info[student].append(grade)

for key, value in students_info.items():
    average_grade = sum(value) / len(value)
    values_as_str = " ".join(str(f'{v:.2f}')for v in value)
    print(f'{key} -> {values_as_str} (avg: {average_grade:.2f})')
