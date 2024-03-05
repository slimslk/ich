number = float(input('Введите вещественное число: '))

if number > 0:
    number = int(number + 0.5)
else:
    number = int(number - 0.5)

print(f'Округленное значение: {number}')
