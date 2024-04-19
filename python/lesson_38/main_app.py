from mysql_datasource import get_connection

import search_service
import input_service
import utils


def main():
    connection = get_connection()
    if connection is None:
        return None

    while True:

        user_choice = input_service.input_user_choice()

        if user_choice == "1":
            search_criteria = input_service.input_search_criteria_from_user()

            if search_criteria == "category":
                category_data = search_service.search_by_category(connection)
                utils.print_film_data(category_data)

            elif search_criteria == "year":
                films = search_service.search_by_year(connection)
                utils.print_film_data(films)

        elif user_choice == "2":
            table_description = search_service.search_table_description(connection)
            utils.print_table_description(table_description)

        if not input_service.input_exit_choice():
            break

    connection.close()


if __name__ == "__main__":
    main()
