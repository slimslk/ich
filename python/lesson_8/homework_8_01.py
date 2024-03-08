def is_palindrome(num):
    reversed_number = 0
    tmp_number = num
    while tmp_number > 0:
        reversed_number *= 10
        reversed_number += tmp_number % 10
        tmp_number //= 10
    if num == reversed_number:
        print('Your number is palindrome')
    else:
        print('Your number is not palindrome')


count = 0
while True:
    count += 1
    number = input('Enter a natural number: ')
    if number.isdigit() and int(number) > 0:
        number = int(number)
        is_palindrome(number)
        break
    print('It is not a natural number. Try another.')
    if count == 5:
        print('There are no attempts left.')
        break
    else:
        print(f'You have {5 - count} attempts left.')
