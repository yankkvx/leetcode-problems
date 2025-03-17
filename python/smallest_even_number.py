# Smallest Even Number (https://leetcode.com/problems/smallest-even-multiple/)
# Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n. 
# Complexity: O(1) time, O(1) space

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        else:
            return n*2