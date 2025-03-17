# Running Sum of 1D Array (https://leetcode.com/problems/running-sum-of-1d-array/)
# Given an array nums, we define a running sum where: runningSum[i] = sum(nums[0]…nums[i]). Return the running sum of nums.
# Complexity: O(n) time, O(n) space (new list is created).

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new_list = []
        sum = 0
        for i in nums:
            sum += i
            new_list.append(sum)
        return new_list
