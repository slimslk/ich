# Напишите декоратор validate_args, который будет проверять типы аргументов функции и выводить сообщение об ошибке,
# если переданы аргументы неправильного типа. Декоратор должен принимать ожидаемые типы аргументов в качестве
# параметров.

def validate_args(*dec_args):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if len(dec_args) != len(args):
                length = len(dec_args) - len(args)
                err_msg = "меньше" if length > 0 else "больше"
                raise TypeError(f"Функция принимает на {abs(length)} {err_msg} аргументов")

            err_msg = ""
            for i in range(len(dec_args)):
                if dec_args[i] is not type(args[i]):
                    err_msg += f"Аргумент {args[i]} имеет неправильный тип {type(args[i])}. Ожидается {dec_args[i]}.\n"
            if err_msg:
                raise TypeError(err_msg)
            result = func(*args, *kwargs)
            return result

        return wrapper

    return decorator


@validate_args(int, str)
def greet(age, name):
    print(f"Привет, {name}! Тебе {age} лет.")


greet(25, "Anna")
greet("25", "Anna")
