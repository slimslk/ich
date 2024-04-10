# Напишите функцию extract_emails(text), которая извлекает все адреса электронной почты
# из заданного текста и возвращает их в виде списка.
from re import findall


def extract_emails(text):
    return findall(r"(\S+@\w[\w-]+\w.\w+)\s?", text)


my_text = "info2@gmail.com Contact us at info2@example.com or 2support2@exam-ple.com for assistance."
emails = extract_emails(my_text)
print(emails)  # Вывод: ['info@example.com', 'support@example.com']
