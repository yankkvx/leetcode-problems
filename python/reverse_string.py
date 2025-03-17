# 344. Reverse String (https://leetcode.com/problems/reverse-string/)
# Reverse a string in-place without using extra memory (O(1) extra space)
# Complexity: O(n) time, O(1) space


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1

        while left < right:
            # Swap characters at the left and right ponters
            s[left], s[right] = s[right], s[left]

            # Move the left pointer to the right, and the right to the left
            left += 1
            right -= 1
