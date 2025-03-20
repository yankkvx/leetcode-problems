# 9. Palindrome Number (https://leetcode.com/problems/palindrome-number/)
# Given an integer x, return True if x is a palindrome, and False otherwise
# Complexity: O(n) time, O(n) space for string conversion


# dumbest solution ever:
class Solution:
    def isPalindrome(self, x: int) -> bool:
        nums = [num for num in str(x)]
        reversed_nums = nums[::-1]
        if ''.join(map(str, nums)) == ''.join(map(str, reversed_nums)):
            return True
        else:
            return False


# normal one:
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
