# Write your MySQL query statement below
SELECT
    Employee.name as Employee
FROM
    Employee
INNER JOIN
    Employee as Manager
WHERE
    Employee.managerId = Manager.id AND Employee.salary > Manager.Salary