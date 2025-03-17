# 3174. Clear Digits (https://leetcode.com/problems/clear-digits/)
# You are given a string s, and you must remove all digits by performing the following operation:
# - Delete the first digit and the closest non-digit character to its left
# - Return the resulting string after removing all digits
# Complexity: O(n) time,  O(n) space


class Solution:
    def clearDigits(self, s: str) -> str:
        result = []

        for char in s:
            if char.isdigit():
                if result:
                    result.pop()  # remove the non digit character before the digit
            else:
                result.append(char)  # add non digit characket to the result

        return ''.join(result)
