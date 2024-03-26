-- 1. Вывести текущую дату и время.
SELECT NOW() AS current;

-- 2. Вывести текущий год и месяц
SELECT DATE_FORMAT(NOW(), '%Y-%m') as current_year_month;

-- 3. Вывести текущее время
SELECT DATE_FORMAT(NOW(), '%H:%i:%s') as cur_time;

-- 4. Вывести название текущего дня недели
SELECT DAYNAME(NOW()) as name_of_the_day;

-- 5. Вывести номер текущего месяца
SELECT EXTRACT(MONTH FROM NOW()) as month_number;

-- 6. Вывести номер дня в дате “2020-03-18”
SELECT DAY('2020-03-18') as day_number;

-- 7. Подключиться к базе данных shop (которая находится на удаленном сервере).
USE shop;

-- 8. Определить какие из покупок были совершены апреле (4-й месяц)
SELECT *
FROM ORDERS
WHERE MONTH(ODATE) = 4;

SELECT * FROM ORDERS;

-- 9. Определить количество покупок в 2022-м году
SELECT COUNT(ORDER_ID) as orders_count
FROM ORDERS
WHERE ODATE BETWEEN '2022-01-01' AND '2022-12-31';

-- 10.  Определить, сколько покупок было совершено в каждый день.
--      Отсортировать строки в порядке возрастания количества покупок. Вывести два поля - дату и количество покупок
SELECT ODATE, COUNT(ODATE) as orders_count_by_day
FROM ORDERS
GROUP BY ODATE
ORDER BY orders_count_by_day;

# Определить среднюю стоимость покупок в апреле
SELECT ROUND(AVG(AMT), 3) as avg_cost
FROM ORDERS
WHERE EXTRACT(MONTH FROM ODATE) = 4;