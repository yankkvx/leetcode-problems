# The Two Sneaky Numbers of Digitville (https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/)
# Given a list of numbers where each number from 0 to n - 1 should appear exactly once, but two numbers appear twice, find the two duplicate numbers.
# Complexity: O(n) time, O(n) space

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count = {}
        duplicates = []

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for num in count:
            if count[num] > 1:
                duplicates.append(num)
        
        return duplicates
                