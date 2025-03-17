-- Combine Two Tables (https://leetcode.com/problems/combine-two-tables/)
-- Write a solution to report the first name, last name, city, and state of each person in the Person table
-- If the address of a personId is not present in the Address table, report null instead

SELECT
    Person.firstName,
    Person.lastName,
    Address.city,
    Address.state
FROM
    Person
    LEFT JOIN Address ON Person.personId = Address.personId