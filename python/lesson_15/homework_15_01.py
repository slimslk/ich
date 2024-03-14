def get_high_score_students(students_list, score):
    high_score_students = []
    for student in students_list:
        if student[2] > score:
            high_score_students.append(student[0])
    return high_score_students


students = [("Alice", 20, 90), ("Bob", 19, 80), ("Charlie", 21, 95), ("David", 18, 85)]
aver_score = int(input('Введите пороговое значение среднего балла: '))
print(f'Студенты с средним баллом выше {aver_score}: {get_high_score_students(students, aver_score)}')
