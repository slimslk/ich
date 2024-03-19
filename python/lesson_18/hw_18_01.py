"""
Написать программу, вычисляющую факториал числа.
Решить задачу с помощью рекурсии.
"""


def factorial(n):
    if n == 0:
        return 1
    n *= factorial(n - 1)
    return n


num = int(input('Enter a number: '))
result = factorial(num)
print(result)
