USE sakila;

# 1. Вывести названия фильмов с расшифровкой рейтинга для каждого. В таблице film хранятся годы
# рейтингов. Нужно воспользоваться оператором case чтобы определить для каждого кода условие, по которому будет
# выводится его развернутое описание (1 предложение).
SELECT title, rating,
       CASE
           WHEN rating = "G" THEN "All ages admitted."
           WHEN rating = "PG" THEN "Some material may not be suitable for children."
           WHEN rating = "PG-13" THEN "Some material may be inappropriate for children under 13."
           WHEN rating = "R" THEN "Under 17 requires accompanying parent or adult guardian."
           WHEN rating = "NC-17" THEN "No one 17 and under admitted."
           ELSE "unknown MPA rating"
           END AS rating_description
FROM film;

# 2. Выведите количество фильмов в каждой категории рейтинга. Используем group by.
SELECT rating,
       COUNT(film_id) AS amount_films
FROM film
GROUP BY rating;

# 3. Используя оконные функции и partition by, выведите список названий фильмов, рейтинг и количество фильмов в каждом
# рейтинге. Объясните, чем отличаются результаты предыдущего запроса и запроса в этой задаче.
SELECT title,
       rating,
       COUNT(film_id) OVER (PARTITION BY rating) AS rating_film_amount
FROM film;
# При использовании оконной функции у нас отображается результат COUNT для каждой строки,
# а группировка убирает дубликаты.


# 4. Изучите таблицы payment и customer. Выведите список всех платежей с указанием имени и фамилии каждого заказчика,
# датой платежа и суммой.
SELECT
    customer.first_name,
    customer.last_name,
    payment.payment_date,
    payment.amount
FROM payment
INNER JOIN customer
ON payment.customer_id = customer.customer_id;

# 5. Поменяйте предыдущий запрос так, чтобы дата выводилась в формате “число, название месяца, год” (без времени).
SELECT
    customer.first_name,
    customer.last_name,
    DATE_FORMAT(payment.payment_date, "%d %M %Y") as payment_date,
    payment.amount
FROM payment
INNER JOIN customer
ON payment.customer_id = customer.customer_id;