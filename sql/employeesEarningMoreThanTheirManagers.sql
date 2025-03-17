-- 181. Employees Earning More Than Their Managers (https://leetcode.com/problems/employees-earning-more-than-their-managers/)
-- Write a solution to find the employees who earn more than their managers


SELECT e.name as Employee
FROM Employee e
JOIN Employee m ON e.managerId = m.id
WHERE e.salary > m.salary