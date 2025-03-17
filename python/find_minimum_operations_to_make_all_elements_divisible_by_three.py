# Find Minimum Operations to Make All Elements Divisible by Three (https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/)
# Given an integer array, find the minimum number of operations needed to make all elements divisible by 3.
# In each operation, you can add or subtract 1 from any element.
# Complexity: O(n) time, O(1) space


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        for i in nums:
            to_three = i % 3
            if to_three == 1:
                operations += 1
            elif to_three == 2:
                operations += 1
        return operations
