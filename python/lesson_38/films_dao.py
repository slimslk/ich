from mysql.connector import Connect

import mysql_datasource
import queries


def get_categories(connection: Connect) -> list[tuple]:
    return mysql_datasource.execute_query(connection, queries.QUERY_CATEGORIES)


def get_by_category_id(connection: Connect, category_id: int, limit) -> list[tuple]:
    query = queries.FILM_BY_CATEGORY_QUERY.format(category_id, limit)
    return mysql_datasource.execute_query(connection, query)


def get_by_year(connection: Connect, operator: str,  year: int, limit) -> list[tuple]:
    query = queries.FILM_BY_YEAR_QUERY.format(operator, year, limit)
    return mysql_datasource.execute_query(connection, query)
