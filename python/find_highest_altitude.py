# 1732. Find the Highest Altitude (https://leetcode.com/problems/find-the-highest-altitude/)
# Given a list of net altitude gains between consecutive points, return the highest altitude reached.
# Complexity: O(n) time, O(1) space

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_al = 0
        current = 0

        for i in gain:
            current += i
            if current >= max_al:
                max_al = current

        return max_al
