def reverse_join(words_list):
    return ' '.join(words_list[::-1])


words = input('Введите предложение: ').split(' ')
print(f'Перевернутое предложение: {reverse_join(words)}')
