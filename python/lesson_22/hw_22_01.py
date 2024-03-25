with open("two_numbers.txt", "r") as file:
    numbers = list(map(int, file.read().split()))

try:
    result = numbers[0] / numbers[1]
    if result < 0:
        raise ValueError
    print(result)
except ValueError:
    print("Число должно быть положительным")


