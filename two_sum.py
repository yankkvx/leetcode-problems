# Two Sum (https://leetcode.com/problems/two-sum/)
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Complexity: O(n) time, O(n) space


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dict for indexes and numbers
        seen = {}
        for k, v in enumerate(nums):
            balance = target - v
            # If the balance exists in the dict, return the indexes 
            if balance in seen:
                return [seen[balance], k]

            # If not save the currnet number and index in the dict
            seen[v] = k
