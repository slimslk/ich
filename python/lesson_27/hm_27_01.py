from functools import reduce


def sum_of_square_even_numbers(numbers_list: list[int]) -> int:
    numbers_list = filter(lambda x: x % 2 == 0, numbers_list)
    result = reduce(lambda x, y: x + y ** 2, numbers_list, next(numbers_list) ** 2)
    return result


numbers = list(map(int, input("Enter list of numbers: ").split()))
print(sum_of_square_even_numbers(numbers))
