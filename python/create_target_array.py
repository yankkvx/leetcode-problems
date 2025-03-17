# 1389. Create Target Array in the Given Order (https://leetcode.com/problems/create-target-array-in-the-given-order/)
# Description:
# Given two integer arrays nums and index, create a target array following these rules:
# - Start with an empty target array
# - For each nums[i], insert it at position index[i] in the target array
# - Repeat until all elements are processed
# Complexity: O(n^2) time, O(n) space

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        for num, i in zip(nums, index):
            result.insert(i, num)
        return result
