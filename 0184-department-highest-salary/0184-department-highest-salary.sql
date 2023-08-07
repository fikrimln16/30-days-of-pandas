SELECT department.name AS department, employee.name AS employee, employee.salary
FROM employee
JOIN department ON employee.departmentId = department.id
WHERE (employee.departmentId, employee.salary) IN (
    SELECT departmentId, MAX(salary)
    FROM employee
    GROUP BY departmentId
);