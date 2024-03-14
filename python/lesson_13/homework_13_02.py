def sum_of_all_numbers(numbers):
    return sum(numbers)


def max_number(numbers):
    return max(numbers)


def min_number(numbers):
    return min(numbers)


nums = input('Введите числа: ').split(', ')
nums = list(map(int, nums))

print(f'Сумма чисел: {sum_of_all_numbers(nums)}')
print(f'Минимальное значение: {max_number(nums)}')
print(f'Максимальное значение: {min_number(nums)}')





