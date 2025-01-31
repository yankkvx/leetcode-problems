# Final Array State After K Multiplication Operations I (https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/)
# Given an integer array nums, an integer k, and an integer multiplier, perform k operations on nums:
# 1. Find the minimum value x in nums. If there are multiple occurrences, select the first one.
# 2. Replace the selected minimum value x with x * multiplier.
# Return the final state of nums after k operations.
# Complexity: O(n*k) time (n - lenght of nums array, k - number of operations perfomed on the array), O(1) space


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            min_value = nums.index(min(nums)) # Find the first entry of the min value
            nums[min_value] *= multiplier # Multiply it by the given multiplier
        return nums
