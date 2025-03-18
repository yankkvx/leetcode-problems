# 1365. How Many Numbers Are Smaller Than the Current Number (https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/)
# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
# That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
# Complexity: O(n^2) time, O(n) space


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            count = 0
            for n in nums:
                if n < num:
                    count += 1
            result.append(count)
        return result
