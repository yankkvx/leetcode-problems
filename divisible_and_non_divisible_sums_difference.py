# Divisible and Non-divisible Sums Difference (https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/)
# Given two integers n and m, calculate the difference between the sum of integers in the range [1, n]
# that are not divisible by m and the sum of integers that are divisible by m.
# Complexity: O(n) time, O(1) space


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        not_divisible = 0
        divisible = 0
        for i in range(1, n+1):
            if i % m != 0:
                not_divisible += i
            if i % m == 0:
                divisible += i
        return not_divisible - divisible
