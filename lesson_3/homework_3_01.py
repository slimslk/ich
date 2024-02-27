first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))


addition = first_number + second_number
difference = first_number - second_number
multiplication = first_number * second_number
power = first_number ** second_number

print('Сумма:', addition)
print('Разность:', difference)
print('Произведение:', multiplication)
print('Первое число в степени второго числа:', power)

if second_number != 0:
    print('Частное:', first_number / second_number)
    print('Остаток от деления:', first_number % second_number)
else:
    print('Невозможно поститать частное и остаток от деления. Деление на ноль недопустимо')
