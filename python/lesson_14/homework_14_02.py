def add_numbers_to_array(array: list, args):
    array.extend(args)


def convert_string_to_int_array(string: str):
    return list(map(int, string.split(", ")))


result = []
nums = input("Введите список чисел: ")
nums = convert_string_to_int_array(nums)
add_numbers_to_array(result, nums)

while True:
    num = input("Введите числа (или 'Выход' для завершения): ")
    if num.lower() == 'выход':
        break
    add_numbers_to_array(result, [int(num)])

print(result)
