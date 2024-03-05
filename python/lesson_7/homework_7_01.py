number = int(input('Введите натуральное десятичное число: '))

while number < 0:
    number = int(input('Введенное число не натуральное, введите новое число: '))

result = 0
exp = 0

while number >= 1:
    modulus = number % 2
    number //= 2
    result += modulus * 10 ** exp
    exp += 1

print(f'Двоичное представление числа: {result}')
