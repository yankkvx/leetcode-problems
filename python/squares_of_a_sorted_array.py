# Squares of a Sorted Array (https://leetcode.com/problems/squares-of-a-sorted-array/)
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
# Complexity: O(n log n) time(because of the sort() func), O(n) space(because of the new_list storage)

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_list = []
        for i in nums:
            new_list.append(i**2)
        new_list.sort()
        return new_list