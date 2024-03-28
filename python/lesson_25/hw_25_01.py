# Напишите функцию find_longest_word, которая будет принимать список слов и возвращать самое длинное слово из
# списка. Аннотируйте типы аргументов и возвращаемого значения функции.

def find_longest_word(word_list: list[str]) -> str:
    """
    Return only one longest word from the words list even if there are multiple words of the same longest length
    """
    words_dict = {word: len(word) for word in word_list}
    sorted_word_dict = sorted(words_dict.items(), key=lambda item: item[1])
    return sorted_word_dict.pop()[0]


words = ["apple", "wwwwwwwwwww", "dragonfruit", "banana", "cherry"]
result = find_longest_word(words)
print(f"The longest word is: {result}")
