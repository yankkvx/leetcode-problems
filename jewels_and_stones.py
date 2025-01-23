# Jewels and Stones (https://leetcode.com/problems/jewels-and-stones/)
# Given strings jewels representing the types of stones that are jewels and stones representing the stones you have. 
# Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
# Complexity: O(n+m) time(n - length of jewels, m - length of stones), O(n) memory

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        # Convert jewels string to a set for faster lookup time complexity.
        # Sets are implemented using hash tables. The average time complexity for checking element exists in a set is O(1)
        jewels_set = set(jewels)
        count = 0
        for stone in stones:
            if stone in jewels_set:
                count += 1
        return count