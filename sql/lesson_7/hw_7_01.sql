-- Подключитесь к базе данных hr (которая находится на удаленном сервере).
USE hr;

-- Выведите количество сотрудников в базе
SELECT COUNT(*) FROM employees;

-- Выведите количество департаментов (отделов) в базе
SELECT COUNT(*) FROM departments;

-- Подключитесь к базе данных World (которая находится на удаленном сервере).
USE world;

-- Выведите среднее население в городах Индии (таблица City, код Индии - IND)
SELECT AVG(city.Population)
FROM city
WHERE city.CountryCode = 'IND';

-- Выведите минимальное население в индийском городе и максимальное.
SELECT MIN(city.Population) as min_population, MAX(city.Population) as max_population
FROM city
WHERE city.CountryCode = 'IND';

-- Выведите самую большую площадь территории.
SELECT MAX(country.SurfaceArea) as max_surface_area
FROM country;

-- Выведите среднюю продолжительность жизни по странам.
SELECT AVG(country.LifeExpectancy) as avg_life_expectancy
FROM country;

-- Найдите самый населенный город (подсказка: использовать подзапросы)
SELECT city.Name
FROM city
WHERE Population = (SELECT MAX(Population) FROM city);