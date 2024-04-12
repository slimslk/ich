# Напишите функцию find_common_words(url_list), которая принимает список URL-адресов и возвращает список наиболее
# часто встречающихся слов на веб-страницах. Для каждого URL-адреса функция должна получить содержимое страницы с
# помощью запроса GET и использовать регулярные выражения для извлечения слов. Затем функция должна подсчитать
# количество вхождений каждого слова и вернуть наиболее часто встречающиеся слова в порядке убывания частоты.

from requests import get
from re import findall
from collections import Counter


def find_common_words(url_list):
    words_dict = {}
    for url in url_list:
        response = get(url).text
        words = findall(r"\b[a-zA-Z]+?\b", response)
        words_dict.update(Counter(words))
    words_dict = {key: value for key, value in words_dict.items() if value > 30}
    return sorted(words_dict.items(), key=lambda word: word[1], reverse=True)


urls = ["https://google.com", "https://yahoo.com", "https://www.bbc.com/news"]

for item in find_common_words(urls):
    print(f"Word: {item[0]}, times: {item[1]}")
