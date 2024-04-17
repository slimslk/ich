# Напишите программу, которая запрашивает у пользователя URL-адрес веб-страницы и уровень заголовков, а затем использует
# библиотеку Beautiful Soup для парсинга HTML и извлекает заголовки нужного уровня (теги h1, h2, h3 и т.д.) с их текстом
# url = "https://www.iana.org/domains/example"
from bs4 import BeautifulSoup
from requests import get

error_text = "{0} link not valid or page not found"
headings = ("h1", "h2", "h3", "h4", "h5", "h6")


def get_all_headings(page_url, head_level):
    if get(page_url).status_code != 200:
        return error_text.format(page_url)
    bs = BeautifulSoup(get(page_url).text, "html.parser")
    links = [(f"<{head_level}>", tag.text) for tag in bs.find_all(head_level)]
    return links


url = input("Enter a url: ")

heading_level = input(f"Enter a heading level {headings}: ").lower()
if heading_level not in headings:
    raise TypeError(f"You should enter only a valid heading level from the list {headings}")

print(get_all_headings(url, heading_level))
