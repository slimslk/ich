def get_value_from_dict_with_get(dictionary: dict, key):
    return dictionary.get(key, -1)


def get_value_from_dict_with_setdefault(dictionary, key):
    return dictionary.setdefault(key, -2)


my_dict = {'apple': 5, 'banana': 6, 'cherry': 7}

key_word = input("Введите ключ для поиска: ")
is_get = input("Использовать метод get (y/n)? ")
if is_get.lower() == "y":
    result = get_value_from_dict_with_get(my_dict, key_word)
else:
    result = get_value_from_dict_with_setdefault(my_dict, key_word)
print(f"Значение для ключа {key_word}: {result}")