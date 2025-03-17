# Number of Steps to Reduce a Number to Zero (https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/)
# Given an integer num, return the number of steps to reduce it to zero.
# - If the number is even, divide it by 2.
# - If the number is odd, subtract 1 from it.
# Complexity: O(log n) time, O(1) space (only a few variables are used)

class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num = num - 1
            steps += 1
        return steps
