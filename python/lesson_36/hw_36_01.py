# Напишите программу, которая запрашивает у пользователя URL-адрес веб-страницы, использует библиотеку
# Beautiful Soup для парсинга HTML и выводит список всех ссылок на странице.
# url = "https://www.iana.org/domains/example"
from bs4 import BeautifulSoup
from requests import get

error_text = "{0} link not valid or page not found"


def get_all_links(page_url):
    if get(page_url).status_code != 200:
        return error_text.format(page_url)
    bs = BeautifulSoup(get(page_url).text, "html.parser")
    links = [link["href"] for link in bs.find_all("a") if link["href"][:4] == "http"]
    return links


url = input("Enter a url: ")
print(get_all_links(url))
