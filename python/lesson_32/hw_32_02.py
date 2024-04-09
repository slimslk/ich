# Реализовать класс Email, представляющий электронное письмо. Класс должен поддерживать следующие операции:
# - Сравнение писем по дате (операторы <, >, <=, >=, ==, !=)
# - Преобразование письма в строку (метод __str__)
# - Получение длины текста письма (метод __len__)
# - Получение хеш-значения письма (метод __hash__)
# - Проверка наличия текста в письме (метод __bool__)
from datetime import datetime
from functools import total_ordering


@total_ordering
class Email:

    def __init__(self, from_email, to_email, subject, message, send_date):
        self.send_date = datetime.strptime(send_date, "%Y-%m-%d")
        self.message = message
        self.subject = subject
        self.to_email = to_email
        self.from_email = from_email

    def __len__(self):
        return len(self.message)

    def __hash__(self):
        return hash(self.message)

    def __bool__(self):
        return bool(self.message)

    def __str__(self):
        return f"From: {self.from_email}\nTo: {self.to_email} \nSubject: {self.subject}\n*2{self.message}"

    def __eq__(self, other):
        return self.send_date == other.send_date

    def __gt__(self, other):
        return self.send_date > other.send_date


email1 = Email("john@example.com",
               "jane@example.com",
               "Meeting",
               "Hi Jane, let's have a meeting tomorrow.",
               "2022-05-10")

email2 = Email("jane@example.com",
               "john@example.com",
               "Re: Meeting",
               "Sure, let's meet at 2 PM.",
               "2022-05-10")

email3 = Email("alice@example.com",
               "bob@example.com",
               "Hello",
               "Hi Bob, how are you?",
               "2022-05-09")

print(len(email2))
print(hash(email3))
print(bool(email1))

print(email2 > email3)      # True
print(email2 == email2)     # True
print(email2 < email3)      # False
print(email2 != email3)     # True
print(email2 >= email3)     # True
print(email2 <= email3)     # False
