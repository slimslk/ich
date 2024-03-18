def modify_list(nums):
    return [(lambda x: int(x / 2) if x % 2 == 0 else x * 2)(i) for i in nums]


numbers = list(map(int, input('Введите список чисел, разделенных пробелами: ').split()))

print(f'Измененный список чисел: {modify_list(numbers)}')
