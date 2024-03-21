"""
Напишите программу, которая создает словарь, содержащий информацию о студентах и их оценках.
Ключами словаря являются имена студентов, а значениями - списки оценок. Создайте функцию calculate_average_grade,
которая принимает словарь с оценками студентов и вычисляет средний балл для каждого студента.
Функция должна возвращать новый словарь, в котором ключами являются имена студентов, а значениями - их средний балл.
Выведите результат на экран.
"""


def calculate_average_grade(student_grades_dict):
    student_average_grade = {}
    for key, value in student_grades_dict.items():
        student_average_grade[key] = sum(value) / len(value)
    return student_average_grade


def add_new_student(student_grades_dict):
    while True:
        student_name = input('Enter student name. Enter quit or exit to compleat entry: ')
        if student_name.lower() in ('quit', 'exit'):
            break
        student_grades = list(map(int, input('Enter the student\'s grades separated by spaces: ').split()))
        student_grades_dict[student_name] = student_grades


student_dict = {'Alice': [85, 90, 92]}
add_new_student(student_dict)
average_grade_dict = calculate_average_grade(student_dict)
print(average_grade_dict)
