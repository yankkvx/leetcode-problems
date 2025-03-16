# 3467. Transform Array by Parity (https://leetcode.com/problems/transform-array-by-parity/)
# Transform an array by replacing even numbers with 0 and odd numbers with 1, then return the sorted result
# Complexity: O (n log n) time, O(n) space


# Using a list comprehension to transform and then sorting the result
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        result = [0 if num % 2 == 0 else 1 for num in nums]
        result.sort()
        return result


# Alternatively, using a for loop for the transformation:
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            if num % 2 == 0:
                result.append(0)
            else:
                result.append(1)
        result.sort()
        return result