"""
Напишите программу, которая принимает строку от пользователя и подсчитывает количество уникальных символов
в этой строке. Создайте функцию count_unique_chars,
которая принимает строку и возвращает количество уникальных символов. Выведите результат на экран.
"""


def count_unique_chars(text):
    return len(set(text))


string = input('Введите строку: ')
number_of_unique_chars = count_unique_chars(string)
print(f'Количество уникальных символов: {number_of_unique_chars}')
