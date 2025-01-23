# Check if a String Is an Acronym of Words (https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/)
# Given an array of strings words and a string s, determine if s is an acronym of words.
# The string s is considered an acronym of words if it can be formed by concatenating the first character of each string in words in order.
# Return true if s is an acronym of words, and false otherwise.
# Complexity: O(n) time, O(n) space


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        letters_list = []
        for word in words:
            f_letter = word[0]
            letters_list.append(f_letter)
        result = ''.join(letters_list)
        if result == s:
            return True
        else:
            return False
