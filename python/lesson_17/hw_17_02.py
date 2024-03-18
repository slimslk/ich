def calculate_sum(*args):
    nums = [int(num) for num in args]
    return sum(nums)


numbers = input('Введите числа, разделенные пробелами: ') .split()
print(f'Сумма чисел: {calculate_sum(*numbers)}')
