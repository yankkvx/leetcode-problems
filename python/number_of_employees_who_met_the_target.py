# Number of Employees Who Met the Target (https://leetcode.com/problems/number-of-employees-who-met-the-target/)
# Given an array of hours worked by employees and a target, return the number of employees who worked at least the target number of hours.
# Complexity: O(n) time, O(1) space

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        counter = 0
        for item in hours:
            if item >= target:
                counter += 1
        return counter
