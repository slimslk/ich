from random import randint

rand_number = randint(1, 100)
print(rand_number)
number = int(input('Угадайте число от 1 до 100: '))

while number < 1 or number > 100:
    number = int(input('Число должно быть от 1 до 100! Попробуйте снова: '))

while True:
    if number == rand_number:
        break
    message = 'Загаданное число меньше.' if number > rand_number else 'Загаданное число больше.'
    print(message)
    number = int(input('Попробуйте снова: '))

print(f'Поздравляю! Вы угадали число {rand_number}!')
