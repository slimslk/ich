import messages


def input_user_choice() -> str:
    while True:
        options = [messages.SEARCH_FILMS, messages.TABLE_DESCRIPTION]
        print("Что вы хотите сделать?")
        user_request = input(f"1 - \"{options[0]}\"\n2 - \"{options[1]}\"\nВведите номер: ").lower()
        if user_request.isdigit() and int(user_request) in [1, 2]:
            return user_request
        print(messages.INVALID_VALUE.format("введенные данные", user_request))


def input_search_criteria_from_user() -> str:
    while True:
        options = [messages.CATEGORY, messages.PRODUCTION_YEAR]
        user_input = input(f"Вы можете искать по: {options[0]} или {options[1]}\nВведите название в скобках: ").lower()
        if user_input in ['category', 'year']:
            return user_input
        print(messages.INVALID_VALUE.format("введенные данные", user_input))


def input_category(categories_id) -> int:
    while True:
        category = input('Выберите категорию: ')
        if category.isdigit() and int(category) in categories_id:
            return int(category)
        print('Ошибка, повторите ввод')


def input_year():
    while True:
        year = input(messages.ENTER_PRODUCTION_YEAR)
        if len(year) == 4:
            return int(year)
        print(messages.INVALID_VALUE.format("год", year))


def input_search_operator():
    while True:
        options = ['<', ">", '<=', '>=', '=', '!=']
        operator = input(f"Введите оператор для посика.\nВарианты {options}: ")
        if operator in options:
            return operator
        print(messages.INVALID_VALUE.format("оператор", operator))


def input_tables_name(tables):
    while True:
        table_name = input(messages.CHOICE_TABLE)
        if table_name in tables:
            return table_name
        print(messages.INVALID_VALUE.format("введенные данные", table_name))


def input_exit_choice():
    return True if input('Хотите повторить поиск? (Д/Y): ').lower() in ('д', 'y') else False
