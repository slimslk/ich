from mysql.connector import Connect

import mysql_datasource
import queries


def get_tables(connection: Connect):
    return mysql_datasource.execute_query(connection, queries.TABLES_QUERY)


def get_table_description(connection: Connect, table_name):
    query = queries.TABLE_DESCRIPTION_QUERY.format(table_name)
    return mysql_datasource.execute_query(connection, query)
