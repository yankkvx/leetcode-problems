# Build Array from Permutation (https://leetcode.com/problems/build-array-from-permutation)
# Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]]
# for each 0 <= i < nums.length and return it.
# Complexity: O(n) time, O(n) space


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            result.append(nums[nums[i]])
        return result
