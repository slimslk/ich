from os import getenv

import mysql.connector
from dotenv import load_dotenv

import messages

load_dotenv()

host = getenv("MYSQL_HOST")
user = getenv("MYSQL_USERNAME")
password = getenv("MYSQL_PASSWORD")
database = getenv("MYSQL_DATABASE")

db_config = {"host": host,
             "user": user,
             "password": password,
             "database": database}


def get_connection():
    connection = None
    try:
        connection = mysql.connector.connect(**db_config)
        print('Соединение с БД прошло успешно')
    except mysql.connector.Error as e:
        print(messages.DB_CONNECTION_ERROR.format(e))
    return connection


def execute_query(connection, query):
    result = None
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
    except mysql.connector.Error as e:
        print(f'Ошибка: \'{e}\' в запросе: {query}')
    finally:
        cursor.close()
    return result
