# Напишите программу, которая принимает список слов от пользователя и использует генераторное выражение (comprehension)
# для создания нового списка, содержащего только те слова, которые начинаются с гласной буквы. Затем программа должна
# использовать функцию map, чтобы преобразовать каждое слово в верхний регистр. В результате программа должна вывести
# новый список, содержащий только слова, начинающиеся с гласной буквы и записанные в верхнем регистре.

vowels = "aeiouy"
words_list = ["Hello", "i", "am", "Jack", "Uizel"]

words_start_vowels = [word for word in words_list if word[0].lower() in vowels]
new_words_list = list(map(lambda w: w.upper(), words_start_vowels))
print(new_words_list)