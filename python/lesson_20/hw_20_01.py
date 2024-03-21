def merge_dicts(*args, **kwargs):
    new_dict = {}
    dict_list = list(args)
    dict_list.append(kwargs)
    for dictionary in dict_list:
        for key, value in dictionary.items():
            if key not in new_dict:
                new_dict[key] = [value]
            else:
                new_dict[key].append(value)
    return new_dict


a = {'a': 1, 'b': 2}
b = {'b': 3, 'c': 4}
c = {'c': 5, 'd': 6}

result = merge_dicts(a, b, c, k=1, v=2, d=4)
print(result)
