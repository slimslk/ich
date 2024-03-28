from collections import Counter
from string import punctuation, digits


def count_words(text):
    special_chars = punctuation + digits
    new_text = text.translate({ord(c): " " for c in special_chars})
    words = new_text.lower().split()
    return dict(Counter(words))


string = input("Введенный текст: ")
words_dict = count_words(string)
if words_dict:
    max_value = max(words_dict.values())
    max_occurring = [kv for kv in words_dict.items() if kv[1] == max_value]
    for el in max_occurring:
        print(f"{el[0]}: {el[1]}")
