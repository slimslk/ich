-- SCHEMA 190224_Dmytro
USE 190224_Dmytro;

-- Task 1
SELECT * FROM orders
ORDER BY price DESC;

-- Task 2
SELECT * FROM customers
WHERE email LIKE '_%@gmail.com';

-- Task3
SELECT *,
    CASE
    WHEN price < 300 THEN 'low'
    WHEN price BETWEEN 300 AND 1500 THEN 'middle'
    WHEN price > 1500 THEN 'high'
    END AS status
FROM orders;

-- Task 4
SELECT *,
    CASE
        WHEN price < 300 THEN 'low'
        WHEN price BETWEEN 300 AND 1500 THEN 'middle'
        WHEN price > 1500 THEN 'high'
    END AS status
FROM orders
ORDER BY status DESC;

-- Task 5
SELECT *
FROM customers
WHERE city = 'South Agustinport';

-- Task 6
SELECT
    item_code, description, COUNT(item_code) AS sales_count
FROM orders
GROUP BY item_code, description
ORDER BY sales_count DESC
LIMIT 1;

-- Task 7
SELECT *, price - discounter_price AS discount
FROM orders
WHERE price - discounter_price = (
    SELECT MAX(price - discounter_price)
    FROM orders);

-- Task 8
-- Скидка определяется как разница между нормальной ценой и скидочной ценой.

-- Task 9
-- Да

-- Task 10
SELECT *, ROUND((1 - discounter_price / price) * 100, 1) AS discount_precent
FROM orders;