CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    dept VARCHAR(50),
    salary DECIMAL(10,2),
    joining DATE
);

CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(100),
    start_date DATE,
    end_date DATE
);

CREATE TABLE employee_project (
    emp_id INT,
    project_id INT,
    hours_worked INT,
    rating INT,
    PRIMARY KEY (emp_id, project_id),
    FOREIGN KEY (emp_id) REFERENCES employees(id),
    FOREIGN KEY (project_id) REFERENCES projects(id)
);