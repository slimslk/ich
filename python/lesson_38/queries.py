QUERY_CATEGORIES = "SELECT category_id, name FROM category"
FILM_BY_CATEGORY_QUERY = """
                            SELECT 
                            film.title, film.release_year, film.description 
                            FROM film
                            INNER JOIN film_category ON film_category.film_id = film.film_id
                            WHERE film_category.category_id = {0}
                            LIMIT {1}
                            """
FILM_BY_YEAR_QUERY = """
                        SELECT 
                        title, release_year, description 
                        FROM film
                        WHERE release_year {0} {1}
                        LIMIT {2}
                        """
TABLES_QUERY = "SHOW TABLES"
TABLE_DESCRIPTION_QUERY = "SHOW COLUMNS FROM {0}"
