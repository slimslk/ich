def arithmetic_operations(numbers_list):
    summ = 0
    diff = 0
    mult = 1
    div = numbers_list[0]
    for number in numbers_list:
        summ += number
        diff -= number
        mult *= number
        if number == numbers_list[0]:
            continue
        div /= number
    print(f"Summ: {summ}, difference: {diff}, multiplication: {mult}, dividing: {div}")


my_file = None
file_name = "numbers.txt"
try:
    my_file = open(file_name, "r")
    numbers = list(map(int, my_file.read().split()))
    arithmetic_operations(numbers)
except FileNotFoundError:
    print(f"File \"{file_name}\" not found!")
except ValueError:
    print("Some values are not a numbers")
except ZeroDivisionError:
    print("You can not dividing by zero")
finally:
    if my_file is not None:
        my_file.close()
