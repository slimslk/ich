USE world;

-- 1. Используя ранжирующие функции, вывести количество городов  в каждой стране для каждой страны.
-- Результат должен содержать CountryCode, CityCount (количество городов в стране).
SELECT CountryCode,
    COUNT(*) OVER (PARTITION BY CountryCode) AS CityCount
FROM city;

-- Поменяйте запрос с использованием
-- джойнов так, чтобы выводилось название страны вместо CountryCode.
SELECT country.Name,
    COUNT(*) OVER (PARTITION BY CountryCode) AS CityCount
FROM city
INNER JOIN country
    ON city.CountryCode = country.Code;


-- 2. Используя ранжирующие функции, Вывести список стран с продолжительностью жизнью и средней продолжительностью жизни.
SELECT
    Name,
    LifeExpectancy,
    AVG(LifeExpectancy) OVER () AS avg_life_exp
FROM country;

-- 3. Используя ранжирующие функции, вывести страны по убыванию продолжительности жизни.
SELECT
    Name,
    LifeExpectancy,
    DENSE_RANK() OVER (ORDER BY LifeExpectancy DESC) AS life_exp_rank
FROM country;

-- 4. Используя ранжирующие функции, вывести третью страну с самой высокой продолжительностью жизни.
SELECT *
FROM    (SELECT
            Name,
            LifeExpectancy,
            ROW_NUMBER() OVER (ORDER BY LifeExpectancy DESC) AS life_exp_rank
        FROM country) tmp
WHERE life_exp_rank = 3;