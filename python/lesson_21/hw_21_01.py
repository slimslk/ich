from collections import Counter


def count_words(text):
    words = text.lower().strip(".").strip(",").split()
    return dict(Counter(words))


text = input("Введенный текст: ")

words_dict = count_words(text)
max_value = max(words_dict.values())
max_occurring = [kv for kv in words_dict.items() if kv[1] == max_value]
for el in max_occurring:
    print(f"{el[0]}: {el[1]}")
