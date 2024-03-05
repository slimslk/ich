n_number = int(input('Введите число N > 0: '))

while n_number < 0:
    print('Число должно быть больше нуля. Введите еще раз: ')

if n_number == 1:
    seq = '0'
else:
    seq = '0, 1'

print(f'Первые {n_number} чисел Фибоначчи: {seq}', end='')

if n_number > 2:
    num = 0
    result = 1
    while n_number > 2:
        n_number -= 1
        temp_number = result
        result += num
        num = temp_number
        print(f', {result}', end='')
