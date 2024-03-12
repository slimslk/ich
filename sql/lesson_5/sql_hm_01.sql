-- Task 1
USE world;

-- Task 2
SELECT * FROM city;
SELECT * FROM country;

SELECT Name, Population
FROM city
UNION
SELECT Name, Population
FROM country;

-- Task3
SHOW CREATE TABLE goods;
/*  В таблице goods есть ограничение CONSTRAINT `goods_chk_1` CHECK ((`quantity` > 0)) которое означает,
    что если добавляется значение quantity, то оно должно быть больше 0 и есть ограничение
    CONSTRAINT `goods_chk_2` CHECK ((`in_stock` in (_utf8mb4'Y',_utf8mb4'N'))) означающее, что in_stock может принимать
    только значение Y или N
*/

