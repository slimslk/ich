def is_armstrong_number(num):
    tmp_num = num
    digit = 0
    while tmp_num > 0:
        tmp_num //= 10
        digit += 1
    armstrong_number = 0
    tmp_num = num
    while tmp_num > 0:
        armstrong_number += (tmp_num % 10) ** digit
        tmp_num //= 10
    if num == armstrong_number:
        print('Your number is an armstrong number')
    else:
        print('Your number is not an armstrong number')


count = 0
while True:
    count += 1
    number = input('Enter a natural number: ')
    if number.isdigit() and int(number) > 0:
        number = int(number)
        is_armstrong_number(number)
        break
    print('It is not a natural number. Try another.')
    if count == 5:
        print('There are no attempts left.')
        break
    else:
        print(f'You have {5 - count} attempts left.')
