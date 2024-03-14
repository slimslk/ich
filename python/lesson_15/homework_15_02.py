def convert_words_into_length(words):
    length_list = []
    for word in words:
        length_list.append(len(word))
    return length_list


sentence = input('Введите предложение: ').split(' ')
print(f'Длины слов в предложении: {tuple(convert_words_into_length(sentence))}')
