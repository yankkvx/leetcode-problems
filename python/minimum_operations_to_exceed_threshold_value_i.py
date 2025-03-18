# 3065. Minimum Operations to Exceed Threshold Value I (https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/)
# You are given a 0-indexed integer array nums, and an integer k.
# In one operation, you can remove one occurrence of the smallest element of nums.
# Return the minimum number of operations needed so that all elements of the array are greater than or equal to k.
# Complexity: O(n log n) time, O(n) space for the first solution. O(n) time, O(1) space for the second solution


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0

        while nums and nums[0] < k:
            nums.pop(0)
            count += 1

        return count


# Solution is simpler, but it has a slight issue. It counts all the elements that are smaller than k,
# but it doesn't remove them in order, which is part of the problem requirement
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        for num in nums:
            if num < k:
                count += 1
        return count
