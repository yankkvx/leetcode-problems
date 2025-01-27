# 1913. Maximum Product Difference Between Two Pairs (https://leetcode.com/problems/maximum-product-difference-between-two-pairs/)
# Given an array `nums`, we need to choose four distinct indices w, x, y, and z such that
# the product difference between two pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.
# The product difference is defined as (a * b) - (c * d) for pairs (a, b) and (c, d).
# Complexity: O(n) time, O(1) space

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # Initializate variables for the two largest and two smalles numbers
        max1, max2 = float('-inf'), float('-inf')
        min1, min2 = float('inf'), float('inf')

        # Iterate to find the largest and smallest numbers
        for num in nums:
            if num > max1:
                max2, max1 = max1, num
            elif num > max2:
                max2 = num

            if num < min1:
                min2, min1 = min1, num
            elif num < min2:
                min2 = num
                
        return (max1*max2)-(min1*min2)
