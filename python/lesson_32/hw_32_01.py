# Реализовать класс Counter, который представляет счетчик. Класс должен поддерживать следующие операции:
# - Увеличение значения счетчика на заданное число (оператор +=)
# - Уменьшение значения счетчика на заданное число (оператор -=)
# - Преобразование счетчика в строку (метод __str__)
# - Получение текущего значения счетчика (метод __int__)

class Counter:

    def __init__(self, counter):
        self.counter = counter

    def __int__(self):
        return self.counter

    def __str__(self):
        return str(self.counter)

    def __iadd__(self, other):
        self.counter = self.counter + other
        return self

    def __isub__(self, other):
        self.counter = self.counter - other
        return self


cnt = Counter(5)
cnt += 3
print(str(cnt))
cnt -= 2
print(int(cnt))

cnt = Counter(-1)
cnt += 3
print(str(cnt))
cnt -= 2
print(int(cnt))
