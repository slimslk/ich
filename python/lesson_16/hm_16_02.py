numbers = list(map(int, input('Введите список чисел, разделенных пробелами: ').split()))

numbers.sort(reverse=True)

print(f'Отсортированный список чисел: {numbers}')
