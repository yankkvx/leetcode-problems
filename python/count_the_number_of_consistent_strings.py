# Count the Number of Consistent Strings (https://leetcode.com/problems/count-the-number-of-consistent-strings/)
# Given a string allowed and an array of strings words, return the number of words that contain only characters from allowed.
# Complexity: O(n * m) time (n - number of words, m - average word length), O(1) space


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        counter = 0
        list_allowed = set(allowed)

        for word in words:
            allowed_symbols = True

            for char in word:
                if char not in list_allowed:
                    allowed_symbols = False

            if allowed_symbols:
                counter += 1

        return counter
