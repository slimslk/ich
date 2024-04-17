# В базе данных ich_edit три таблицы. Users с полями (id, name, age), Products с полями (pid, prod, quantity) и Sales
# с полями (sid, id, pid).
# Программа должна вывести все имена из таблицы users, дать пользователю выбрать одно из них и вывести все покупки
# этого пользователя.

from os import getenv

from dotenv import load_dotenv
from mysql.connector import connect, Error as MySqlError

load_dotenv()

HOST = getenv("MYSQL_HOST")
USER = getenv("MYSQL_USERNAME")
PASSWORD = getenv("MYSQL_PASSWORD")
DATABASE = getenv("MYSQL_DATABASE")

dbconfig = {"host": HOST,
            "user": USER,
            "password": PASSWORD,
            "database": DATABASE}

GET_USERS_QUERY = "SELECT name, id FROM users;"
GET_ORDERS_QUERY = """SELECT prod, quantity
                      FROM product
                      INNER JOIN sales
                      ON product.pid = sales.pid
                      WHERE sales.id = {0}"""


def get_connection():
    con = None
    try:
        con = connect(**dbconfig)
    except MySqlError as e:
        print(e)
    return con


def get_data(con, query) -> list[tuple]:
    cursor = con.cursor()
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except MySqlError as e:
        print(e)
    finally:
        cursor.close()


def validate_name(users_list, username):
    return username in users_list


def get_username_id(db_con):
    users = {key.lower(): value for key, value in get_data(db_con, GET_USERS_QUERY)}
    for user_key in users:
        print(user_key.capitalize())
    while True:
        name = input("Choose the name from list above: ").lower()
        if validate_name(users, name):
            break
        print(f"Incorrect name, you should choose the name from the list!")
    return name, users[name]


connection = get_connection()

while True:
    user, user_id = get_username_id(connection)
    lists = get_data(connection, GET_ORDERS_QUERY.format(user_id))
    if len(lists) == 0:
        print(f"User {user.capitalize()} has not any orders: ")
    else:
        print(f"User {user.capitalize()} has: ")
        for prod_name, quantity in lists:
            print(f"{prod_name} = {quantity}")
    q = input("Exit? (y/yes): ")
    if q.lower() in ("y", "yes", "ok"):
        break

connection.close()
