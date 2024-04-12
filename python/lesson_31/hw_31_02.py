# Напишите декоратор log_args, который будет записывать аргументы и результаты вызовов функции в лог-файл.
# Каждый вызов функции должен быть записан на новой строке в формате "Аргументы: <аргументы>, Результат: <результат>".
# Используйте модуль logging для записи в лог-файл.
import datetime
from logging import basicConfig, info, INFO

basicConfig(filename="log.txt", filemode="a", format="%(message)s", level=INFO)


def log_args(func):
    def wrapper(*args, **kwargs):
        result = func(*args, *kwargs)
        info("Аргументы %s, Результат: %s", args, str(result))
        return result

    return wrapper


@log_args
def add(a, b):
    return a + b


@log_args
def sub(a, b, c):
    return a - b - c


add(2, 3)
add(5, 7)
add("Hello", "Jack")
sub(5, 2, 3)

