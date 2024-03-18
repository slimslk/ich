"""
Напишите программу, которая принимает матрицу (вложенный список) от пользователя и
находит сумму всех элементов в матрице. Используйте вложенные списки и циклы для обхода элементов матрицы.
"""


def matrix_sum(mtx):
    result = 0
    for element in mtx:
        for sub_element in element:
            result += sub_element
    return result


def parse_input(string):
    string = string.strip('[]').split('], [')
    return [list(map(int, el.split(', '))) for el in string]


matrix = input('Enter matrix as a nested list: ')
matrix = parse_input(matrix)

print(f'Сумма элементов в матрице: {matrix_sum(matrix)}')
