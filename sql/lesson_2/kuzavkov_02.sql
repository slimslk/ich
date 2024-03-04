-- Dmytro Kuzavkov

-- Task 1
SELECT * FROM employees;

-- Task 2
SELECT salary FROM employees;

-- Task 3
SELECT
    CASE
        WHEN salary > 10000 THEN 1
        WHEN salary < 10000 THEN 0
    END
    AS salary_group
FROM employees;

-- Task 4 : Выводится только один столбец так как в SELECT кроме условия CASE/END больше не указано никаких столбцов

-- Task 5
SELECT
    first_name,
    CASE
        WHEN salary > 10000 THEN 1
        WHEN salary < 10000 THEN 0
    END
    AS salary_group
FROM employees;

-- Task 6
SELECT AVG(
        CASE
            WHEN department_id = 60
            OR department_id = 90
            OR department_id = 100
            THEN salary
        END
        )
        AS avg_dp_60_90_100
FROM employees;

-- Task 7
SELECT
    first_name, last_name,
    CASE
        WHEN salary < 10000 THEN 'junior'
        WHEN salary > 10000 AND salary < 15000 THEN 'mid'
        WHEN salary > 15000 THEN 'senior'
    END
    AS level
FROM employees;

-- Task 8
SELECT * FROM jobs;

SELECT job_id,
    CASE
        WHEN max_salary > 10000 THEN 'high payer'
        WHEN max_salary < 10000 THEN 'low payer'
    END
    AS payer_rank
FROM jobs;

-- Task 9
SELECT job_id,
    IF(max_salary > 10000, 'high payer',
		IF(max_salary < 10000, 'low payer', null))
    AS payer_rank
FROM jobs;

-- Task 10
SELECT job_id,
    IF(max_salary > 10000, 'high payer',
		IF(max_salary < 10000, 'low payer', null))
    AS payer_rank,
    max_salary
FROM jobs
ORDER BY max_salary DESC;