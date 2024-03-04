qqUSE hr;

/* Task 1 */
SELECT * FROM employees WHERE job_id = 'IT_PROG';

/* Task 2 */
SELECT * FROM employees WHERE job_id = 'AD_VP';

/* Task 4 */
SELECT * FROM employees WHERE salary >= 10000 AND salary <= 20000;
SELECT * FROM employees WHERE department_id NOT IN (30, 60, 100);
SELECT * FROM employees WHERE first_name LIKE '_%ll%_';
SELECT * FROM employees WHERE last_name LIKE '%a';

/* Task 5 */
SELECT * FROM employees WHERE salary > 10000;

/* Task 6 */
SELECT * FROM employees WHERE salary > 10000 AND last_name LIKE 'L%';

/*	Task 7: select * from employees where salary > 10000 or salary <= 10000; -> Будет выдан список всех сотрудников в таблице
	Task 8: select *  from employees where salary > 10000 or salary < 10000; -> Выдаст список всех сотрудников у которых salary не равна 10000
	Task 9: select *  from employees where salary > 10000 and salary < 5000; -> Выдаст пустой список сотрудников