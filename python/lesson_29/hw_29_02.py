# Создайте класс Student для представления студента. Класс должен иметь атрибуты name (имя) и age (возраст),
# а также метод display_info(), который выводит информацию о студенте. Затем создайте экземпляр класса Student
# с заданным именем и возрастом и вызовите метод display_info().

class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Student name is {self.name}, his/her age is {self.age}")


student_1 = Student("Jack", 21)
student_1.display_info()