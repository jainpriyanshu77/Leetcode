# Write your MySQL query statement below
SELECT e.name, eid.unique_id FROM Employees e LEFT JOIN EmployeeUNI eid ON e.id = eid.id;