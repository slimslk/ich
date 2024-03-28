def get_value_from_dict(dictionary: dict, key):
    is_get = input("Использовать метод get (y/n)? ")
    if is_get.lower() == "y":
        return dictionary.get(key, -1)
    return dictionary.setdefault(key, -2)


my_dict = {'apple': 5, 'banana': 6, 'cherry': 7}
key_word = input("Введите ключ для поиска: ")
result = get_value_from_dict(my_dict, key_word)
print(f"Значение для ключа {key_word}: {result}")
