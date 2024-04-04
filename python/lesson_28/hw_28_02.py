# Напишите программу, которая принимает список чисел от пользователя и использует функцию reduce из модуля functools,
# чтобы найти произведение всех чисел в списке. Затем программа должна использовать функцию itertools.accumulate
# для накопления произведений чисел в новом списке. В результате программа должна вывести список,
# содержащий накопленные произведения.
from operator import mul
from functools import reduce
from itertools import accumulate

numbers_list = [1, 2, 3, 4]

reduced = reduce(mul, numbers_list)
accumulate_list = accumulate(numbers_list, mul)
print(f"The result of reduce: {reduced}")
print(f"The result of accumulate: {list(accumulate_list)}")

