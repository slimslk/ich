from mysql.connector import Connect

import films_dao
import tables_dao
import utils
import input_service

LIMIT = 10


def search_by_year(connection):
    year = input_service.input_year()
    operator = input_service.input_search_operator()
    films = films_dao.get_by_year(connection, operator, year, LIMIT)
    return films


def search_by_category(connection: Connect) -> list[tuple]:
    categories_data = films_dao.get_categories(connection)
    utils.print_categories_name(categories_data)
    category_id = input_service.input_category(utils.get_categories_id(categories_data))
    return films_dao.get_by_category_id(connection, category_id, LIMIT)


def search_table_description(connection: Connect):
    data = [names[0] for names in tables_dao.get_tables(connection)]
    utils.print_tables_name(data)
    table_name = input_service.input_tables_name(data)
    return tables_dao.get_table_description(connection, table_name)
