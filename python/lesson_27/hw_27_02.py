def compose_functions(functions, value):
    result = value
    for func in functions:
        result = func(result)
    return result


add_one = lambda x: x + 1
double = lambda x: x * 2
subtract_three = lambda x: x - 3

fun_list = [add_one, double, subtract_three]
val = 5
print(f"Конечный результат: {compose_functions(fun_list, val)}")
