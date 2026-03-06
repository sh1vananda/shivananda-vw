SELECT *
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);

SELECT *
FROM employees e
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
    WHERE dept = e.dept
);

SELECT *
FROM employees e
WHERE salary = (
    SELECT MAX(salary)
    FROM employees
    WHERE dept = e.dept
);

SELECT *
FROM employees
WHERE salary > (
    SELECT AVG(salary) FROM employees
)
AND salary < (
    SELECT MAX(salary) FROM employees
);

SELECT dept
FROM employees
GROUP BY dept
HAVING AVG(salary) > (
    SELECT AVG(salary)
    FROM employees
);