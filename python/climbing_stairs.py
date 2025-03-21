# 70. Climbing Stairs (https://leetcode.com/problems/climbing-stairs/)
# Given an integer n representing the number of steps, return the number of distinct ways to climb to the top.
# Each time you can either climb 1 or 2 steps.
# Complexity: O(n) time, O(1) space


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        first, second = 1, 2
        for i in range(2, n):
            current = first + second
            first = second
            second = current

        return current
