# Shuffle the Array (https://leetcode.com/problems/shuffle-the-array/)
# Given an array nums of length 2n, where the first n elements are the first half (x1, x2, ..., xn) 
# and the last n elements are the second half (y1, y2, ..., yn), return the array in the form [x1, y1, x2, y2, ..., xn, yn].
# Complexity: O(n) time, O(n) space

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first_half = nums[:n]
        second_half = nums[n:]
        result = []
        for i in range(n):
            result.append(first_half[i])
            result.append(second_half[i])

        return result