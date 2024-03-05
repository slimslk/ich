prime_number = int(input('Введите целое положительное число: '))

while prime_number < 0:
    prime_number = int(input('Число отрицательное, целое положительное числ: '))

number = 2

while number < prime_number:
    if prime_number % number == 0:
        print(f'Число {prime_number} не является простым.')
        break
    number += 1
else:
    print(f'Число {prime_number} является простым.')
