"""
Напишите функцию is_subset, которая принимает два множества set1 и set2 и проверяет, является ли set1 подмножеством set2.
Функция должна возвращать True, если все элементы из set1 содержатся в set2, и False в противном случае.
Функция должна быть реализована без использования встроенных методов issubset или <=.
"""


def is_subset(set1, set2):
    if len(set1) > len(set2):
        return False
    for el in set1:
        if el not in set2:
            return False
    return True


s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5}

result = is_subset(s1, s2)
print(result)
