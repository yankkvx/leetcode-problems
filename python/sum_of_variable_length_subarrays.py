# 3427. Sum of Variable Length Subarrays (https://leetcode.com/problems/sum-of-variable-length-subarrays)
# Given an integer array nums of size n. For each index i, define a subarray nums[start ... i]
# where start = max(0, i - nums[i]). Return the total sum of all elements from the subarrays.
# Complexity: O(n^2) time, O(1) space

class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        result = 0

        for i in range(len(nums)):
            start = max(0, i - nums[i])
            pairs_sum = sum(nums[start:i+1])  #Sum of elements from start to i
            result += pairs_sum

        return result
