# Write your MySQL query statement below
SELECT employee_id FROM Employees WHERE salary < 30000 AND manager_id NOT IN (select distinct employee_id from employees)order by employee_id; 