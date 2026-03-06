INSERT INTO employees (emp_id, emp_name, dept, salary, joining) VALUES
(1, 'Abc', 'HR', 50000, '2022-02-22'),
(2, 'Def', 'IT', 70000, '2021-01-11'),
(3, 'Ghi', 'IT', 90000, '2020-10-10'),
(4, 'Jkl', 'HR', 60000, '2023-03-03'),
(5, 'Mno', 'IT', 80000, '2021-01-01');

INSERT INTO projects (project_id, project_name, start_date, end_date) VALUES
(111, 'Website', '2023-01-01', '2023-06-01'),
(222, 'Mobile App', '2023-03-01', '2023-09-01'),
(333, 'CLI Tool', '2024-01-01', '2024-08-01');

INSERT INTO employee_project (emp_id, project_id, hours_worked, rating) VALUES
(1, 111, 120, 5),
(1, 222, 80, 4),
(2, 111, 150, 5),
(2, 333, 100, 3),
(3, 222, 200, 4),
(3, 333, 150, 5),
(4, 111, 90, 4),
(4, 222, 60, 3);