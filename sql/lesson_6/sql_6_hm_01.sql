-- Task1 Подключитесь к базе данных world (которая находится на удаленном сервере).
USE world;

SELECT * FROM country;
SELECT * FROM countrylanguage;
SELECT * FROM city;

-- Task2 Выведите список стран с языками, на которых в них говорят.
SELECT country.Name, countrylanguage.Language FROM country
INNER JOIN countrylanguage
ON country.Code = countrylanguage.CountryCode;

-- Task3 Выведите список городов с их населением и названием стран
SELECT city.Name, city.Population, country.Name
FROM city
INNER JOIN country
ON city.CountryCode = country.Code;

-- Task4 Выведите список городов в South Africa
SELECT city.Name FROM city
INNER JOIN country
ON city.CountryCode = country.Code
WHERE country.Name = 'South Africa';

-- Task5 Выведите список стран с названиями столиц. Подсказка: в таблице country есть поле Capital, которое содержит номер города из таблицы City.
SELECT country.Name, city.Name FROM country
INNER JOIN city
ON country.Capital = city.ID;

-- Task6 Измените запрос 5 таким образом, чтобы выводилось население в столице.
SELECT country.Name, city.Name, city.Population FROM country
INNER JOIN city
ON country.Capital = city.ID;

-- Task7 Напишите запрос, который возвращает название столицы United States
SELECT country.Name, city.Name FROM country
INNER JOIN city
ON country.Capital = city.ID
WHERE country.Name = 'United States';

-- Task8 Используя базу hr_data.sql, вывести имя, фамилию и город сотрудника.
USE hr;

SELECT employees.first_name, employees.last_name, locations.city FROM employees
INNER JOIN departments
ON employees.department_id = departments.department_id
INNER JOIN locations
ON departments.location_id = locations.location_id;

-- Task9 Используя базу hr_data.sql, вывести города и соответствующие городам страны.
SELECT locations.city, countries.country_name FROM locations
INNER JOIN countries
ON locations.country_id = countries.country_id;