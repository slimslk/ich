first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
third_number = int(input('Введите третье число: '))

if first_number > second_number:
    if first_number > third_number:
        temp = third_number
        third_number = first_number
        first_number = temp
    if first_number > second_number:
        temp = second_number
        second_number = first_number
        first_number = temp
elif first_number > third_number:
    temp = third_number
    third_number = first_number
    first_number = temp
    if second_number > third_number:
        temp = second_number
        second_number = third_number
        third_number = temp
elif second_number > third_number:
    temp = second_number
    second_number = third_number
    third_number = temp

print(first_number, second_number, third_number)
