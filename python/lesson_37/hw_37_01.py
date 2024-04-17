# В базе данных ich_edit три таблицы. Users с полями (id, name, age), Products с полями (pid, prod, quantity)
# и Sales с полями (sid, id, pid).
# Программа должна запросить у пользователя название таблицы и вывести все ее строки или
# сообщение, что такой таблицы нет.
from os import getenv

from dotenv import load_dotenv
from mysql.connector import connect, Error as MySqlError

load_dotenv()

HOST = getenv("MYSQL_HOST")
USER = getenv("MYSQL_USERNAME")
PASSWORD = getenv("MYSQL_PASSWORD")
DATABASE = getenv("MYSQL_DATABASE")


def get_connection():
    con = None
    try:
        con = connect(**dbconfig)
    except MySqlError as e:
        print(e)
    return con


def get_db_info(con, table_name: str) -> list[tuple]:
    query = f"SELECT * FROM {table_name};"
    cursor = None
    try:
        cursor = con.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    except MySqlError:
        print(f"Table {table_name} doesn't exist")
    finally:
        if cursor is not None:
            cursor.close()


def main():
    name = input("Enter a table name: ")
    if (connection := get_connection()) is None:
        return None
    print(get_db_info(connection, name))
    connection.close()


if __name__ == "__main__":
    dbconfig = {"host": HOST,
                "user": USER,
                "password": PASSWORD,
                "database": DATABASE}
    main()
