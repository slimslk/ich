# Создайте класс BankAccount для представления банковского счета. Класс должен иметь атрибуты account_number
# (номер счета) и balance (баланс), а также методы deposit() для внесения денег на счет и withdraw() для снятия
# денег со счета. Затем создайте экземпляр класса BankAccount, внесите на счет некоторую сумму и снимите часть денег.
# Выведите оставшийся баланс. Не забудьте предусмотреть вариант, при котором при снятии баланс может стать меньше нуля.
# В этом случае уходить в минус не будем, вместо чего будем возвращать сообщение "Недостаточно средств на счете".

class BankAccount:

    def __init__(self, account_number: int, balance: float = 0):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance - amount < 0:
            print("Недостаточно средств на счете")
        self.__balance -= amount

    def __str__(self):
        return f"Account number: {self.__account_number}\nBalance: {self.__balance}"


account = BankAccount(1000444332)
account.deposit(123.56)
print(account)
account.withdraw(20)
print(account)
