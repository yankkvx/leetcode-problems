# Find the Number of Good Pairs I (https://leetcode.com/problems/find-the-number-of-good-pairs-i/)
# Given two integer arrays nums1 of length n and nums2 of length m, and an integer k,
# a pair (i, j) is called "good" if nums1[i] is divisible by nums2[j] * k.
# Return the total number of good pairs.
# Time Complexity:
# Complexity:  O(n * m) time(n - nums1 length, m - nums2 lenght), O(1) space


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        count = 0
        for i, num1 in enumerate(nums1):
            for j, num2 in enumerate(nums2):
                if num1 % (num2*k) == 0:
                    count += 1

        return count
