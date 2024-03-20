
-- Подключитесь к базе данных Students (которая находится на удаленном сервере).
USE Students;

-- Найдите самого старшего студента
SELECT name, age
FROM Students
ORDER BY age DESC
LIMIT 1;

-- Найдите самого старшего преподавателя
SELECT name, age
FROM Teachers
ORDER BY age DESC
LIMIT 1;

-- Выведите список преподавателей с количеством компетенций у каждого
SELECT Teachers.name as teacher_name, COUNT(Teachers2Competencies.competencies_id)
FROM Teachers
LEFT JOIN Teachers2Competencies
ON Teachers.id = Teachers2Competencies.teacher_id
GROUP BY Teachers.id;

-- Выведите список курсов с количеством студентов в каждом
SELECT Courses.title, COUNT(Students2Courses.student_id)
FROM Courses
LEFT JOIN Students2Courses
ON Courses.id = Students2Courses.course_id
GROUP BY Courses.id;

-- Выведите список студентов, с количеством курсов, посещаемых каждым студентом.
SELECT Students.name, COUNT(Students2Courses.student_id)
FROM Students
LEFT JOIN Students2Courses
ON Students.id = Students2Courses.student_id
GROUP BY Students.id;
