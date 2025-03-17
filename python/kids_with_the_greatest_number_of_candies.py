# Kids With the Greatest Number of Candies (https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/)
# Given an array of candies and an integer extraCandies, return a boolean array
# where each element indicates whether the corresponding kid would have the greatest number of candies if they received all the extra candies.
# Complexity: O(n) time, O(n) space

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = []

        for candy in candies:
            if candy + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)

        return result
