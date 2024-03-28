-- Подключиться к базе данных world
USE world;

-- Вывести население в каждой стране. Результат содержит два поля: CountryCode,
-- sum(Population). Запрос по таблице city.
SELECT city.CountryCode, SUM(city.Population) AS amount_population
FROM city
GROUP BY city.CountryCode;


-- Изменить запрос выше так, чтобы выводились только страны с населением более 3 млн
-- человек.
SELECT city.CountryCode, SUM(city.Population) AS amount_population
FROM city
GROUP BY city.CountryCode
HAVING amount_population > 3000000;

-- Сколько всего записей в результате? 59 rows

-- Поменять запрос выше так, чтобы в результате вместо кода страны выводилось ее название.
SELECT country.Name, SUM(city.Population) AS amount_population
FROM city
INNER JOIN country
ON city.CountryCode = country.Code
GROUP BY city.CountryCode
HAVING amount_population > 3000000;

-- Вывести количество городов в каждой стране (CountryCode, amount of cities).
SELECT CountryCode, COUNT(*) AS amount_of_cities
FROM city
GROUP BY CountryCode;

-- Поменять запрос так, чтобы вместо кодов стран, было названия стран.
SELECT country.Name, COUNT(*) AS amount_of_cities
FROM city
INNER JOIN country
ON city.CountryCode = country.Code
GROUP BY CountryCode;

SELECT COUNT(*) as amount_of_cities
    FROM city;

SELECT COUNT(*) as countries
FROM country;


-- Поменять запрос так, чтобы выводилось среднее количество городов в странах.
SELECT ROUND(amount_of_cities / countries, 2) AS average_of_cities
FROM (
    SELECT CountryCode, COUNT(*) as amount_of_cities
    FROM city
    ) am_city
JOIN (
    SELECT COUNT(*) as countries
    FROM country
    ) am_coun;