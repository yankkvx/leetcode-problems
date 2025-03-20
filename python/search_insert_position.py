# 35. Search Insert Position (https://leetcode.com/problems/search-insert-position/)
# Given a sorted array of distinct integers and a target value, return the index if found, 
# or the position where it should be inserted to maintain order
# Complexity: O(log n) time, O(1) space


# Linear search
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] >= target:
                return i
            i += 1
        
        return i
    

# Binary search
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left