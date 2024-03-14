def sum_numbers(number1, number2):
    return number1 + number2


def mult_numbers(number1, number2):
    return number1 * number2


num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

result = (sum_numbers(num1, num2), mult_numbers(num1, num2))
print(f'Сумма и произведение чисел: {result}')

