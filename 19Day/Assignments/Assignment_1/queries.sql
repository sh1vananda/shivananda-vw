SELECT emp_id
FROM employee_project
GROUP BY emp_id
HAVING COUNT(project_id) > 2;

SELECT emp_id
FROM employee_project
GROUP BY emp_id
HAVING AVG(rating) > 4;

SELECT *
FROM employees e
WHERE salary = (
    SELECT MAX(salary)
    FROM employees
    WHERE dept = e.dept
);

SELECT *
FROM employees
WHERE id NOT IN (
    SELECT emp_id
    FROM employee_project
);

SELECT project_id
FROM employee_project
GROUP BY project_id
ORDER BY SUM(hours_worked) DESC
LIMIT 1;