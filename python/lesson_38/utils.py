
def print_tables_name(tables_data: list[str]):
    if tables_data is not None:
        i = 0
        col_count = 0
        while i < len(tables_data):
            print(f"|{tables_data[i][:10]:^14}", end='')
            col_count += 1
            if col_count > 2:
                print("")
                col_count = 0
            i += 1
        print("")


def print_film_data(category_data):
    if category_data is not None:
        print('-' * 150)
        print('   Название фильма   |  Год | Описание')
        print('-' * 150)
        for name, year, description in category_data:
            print(f'{name[:20]:>20} |{year:^6}| {description[:100]}')


def print_categories(data):
    for cat_id, name in data:
        print(f"{cat_id:3}  -{name:^15}")


def get_categories_id(categories_data) -> list[int]:
    categories_id = []
    for item in categories_data:
        categories_id.append(int(item[0]))
    return categories_id


def print_categories_name(categories_data):
    for cat_id, name in categories_data:
        print(f'{cat_id:3}  -{name:^15}')


def print_table_description(description):
    for row in description:
        print(row)
