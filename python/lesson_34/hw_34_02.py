# Напишите функцию highlight_keywords(text, keywords), которая выделяет все вхождения заданных ключевых слов в
# тексте, окружая их символами *. Функция должна быть регистронезависимой при поиске ключевых слов.
from re import compile, IGNORECASE


def highlight_keywords(text, keywords):

    regex = compile('|'.join(keywords), IGNORECASE)
    return regex.sub(lambda match: '*' + match.group(0) + '*', text)


my_text = "This is a sample text. We need to highlight Python and programming."

keyword_list = ["python", "programming", "sample"]
highlighted_text = highlight_keywords(my_text, keyword_list)
print(highlighted_text)
